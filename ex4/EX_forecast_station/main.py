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
        
def get_data_from_xml(xml_file,xsd_file):
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        if not schema.is_valid(xml_file):
            log_errors(xml_file,xsd_file) #log validation errors
            return
        data = schema.to_dict(xml_file)
        return data
    
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)
        
def calculate_average(data, node):
    counter = 0
    tot = 0
    for measure in data["measures"]:
        tot += measure[node]
        counter += 1
        
    return tot/counter
        

def main():
    """
    To launch the script use the command prompt
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("file_xml", type=str)  # Argomento posizionale

    # Analizza i parametri
    args = parser.parse_args()

    xml_file = args.file_xml
    xsd_file = os.path.join(script_path, "forecast_station_schema.xsd")
    setup_logger()
    data = get_data_from_xml(xml_file,xsd_file)
    avg_temp = calculate_average(data, "temperature")
    print(f"Average temperature: {avg_temp}")
    
if __name__ == "__main__":
    main()