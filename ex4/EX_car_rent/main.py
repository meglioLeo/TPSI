import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system
import argparse #module for parsing command line arguments

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
        
def pprint_valid_data(xml_file,xsd_file):
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        if not schema.is_valid(xml_file):
            log_errors(xml_file,xsd_file) #log validation errors
            return
        data = schema.to_dict(xml_file)
        print(f"\nValid data:")
        pprint.pprint(data, indent=2, width=100) #pretty print the entire data structure
    
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)
        
def find_hybrid_agencies(xml_file,xsd_file,Class):   #find the agencies that offer hybrid cars of a specified class
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        if not schema.is_valid(xml_file):
            log_errors(xml_file,xsd_file)
            return
        data = schema.to_dict(xml_file)
        for car in data["car"]:
            for agency in car["agencies"]:
                if car["fueling"] == "hybrid" and car["class"] == Class:
                    #print(f"Agency: {car['agencies'].attribute['name']}, Car: {car['model']}")
                    agency = car["agencies"]
                    #print(agency)
                    for ag in agency:
                        attribute_value = ag["@name"]
                    print(f"Agency: {attribute_value}")
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)

def main():
    """
    To launch the script use the command prompt
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("file_xml", type=str)  # Argomento posizionale
    parser.add_argument("Class", type=str)  # Argomento posizionale

    # Analizza i parametri
    args = parser.parse_args()

    # Usa i parametri
    #print(f"Ciao {args.nome}, hai {args.eta} anni!")

    xml_file = args.file_xml
    xsd_file = os.path.join(script_path, "car_rent_schema.xsd")
    setup_logger()
    #pprint_valid_data(xml_file,xsd_file)
    find_hybrid_agencies(xml_file,xsd_file,args.Class)
    
if __name__ == "__main__":
    main()