import xmlschema
import logging
import pprint
import os

global script_path
script_path = os.path.dirname(os.path.abspath(__file__))

def setup_logger():
    logging.basicConfig(
        filename=os.path.join(script_path, "log.log"),
        level=logging.ERROR,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"  #
    )
    
def log_errors(xml_file, xsd_file):
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
        
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)
        
def get_locations(data):
    locations = []

    if "shipments" in data and "shipment" in data["shipments"]:
        shipments = data["shipments"]["shipment"]

        if isinstance(shipments, list):  #check if shipments is a list
            for shipment in shipments:
                if "location" in shipment:
                    locations.extend(shipment["location"])
        else:
            if "location" in shipments:
                locations = shipments["location"]

    return locations