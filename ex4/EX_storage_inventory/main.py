import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system

#get the path of the script
global script_path
script_path = os.path.dirname(os.path.abspath(__file__))

def setup_logger():
    logging.basicConfig(
        filename=os.path.join(script_path, "log.log"),
        level=logging.ERROR,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  
    )
    
def log_errors(xml_file, xsd_file):
    """
    Logs all validation errors.
    """
    schema = xmlschema.XMLSchema(xsd_file)
    for error in schema.iter_errors(xml_file): #iter_errors to avoid raising an exception -> the program doesn't stop
        error_message = f"File: {xml_file}, Error: {error}\n\n\n"
        logging.error(error_message)    #log the errors without stopping the program
        
def get_data_from_xml(xml_file,xsd_file):
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        if not schema.is_valid(xml_file):
            log_errors(xml_file,xsd_file) #log validation errors
            return
        data = schema.to_dict(xml_file)
        #pprint.pprint(data, indent=2, width=100) #pretty print the entire data structure
        return data
    
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)

def calculate_total_value(data):
    for category in data["categories"]["category"]:
        total_value = 0
        for product in category["products"]["product"]:
            price = product["price"]
            quantity = product["quantity"]
            value = price * quantity
            total_value += value
        print(f"Total value of {category['category_name']}: {total_value}")
        
def calculate_stock(data):
    for category in data["categories"]["category"]:
        for product in category["products"]["product"]:
            stock = int(product["quantity"])
            product_code = product["product_code"]
            product_name = product["product_name"]
            for operation in data["operation_register"]["operation"]:
                if product_code == operation["operation_product"]:          
                    if operation["operation_type"] == "in":
                        stock += int(operation["operation_quantity"])
                    elif operation["operation_type"] == "out":
                        stock -= int(operation["operation_quantity"])
            print(f"Product {product_name} with code {product_code} has {stock} units in stock")
                        
def main():
    xml_file = os.path.join(script_path, "storage_inventory.xml")
    xsd_file = os.path.join(script_path, "storage_inventory_schema.xsd")
    setup_logger()
    data = get_data_from_xml(xml_file,xsd_file)
    if data is None:
        return
    calculate_total_value(data)
    calculate_stock(data)
    
if __name__ == "__main__":
    main()