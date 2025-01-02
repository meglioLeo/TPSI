import xmlschema
import logging
import pprint
import os
from datetime import datetime

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
       
class Location:
    def __init__(self, place, date):
        self.place = place
        self.date = date
    
    def __str__(self):
        return f"Place: {self.place}, Timestamp: {self.date}"
        

class handle_shipment:
    def __init__(self):
        self.shipments = []  # Lista di spedizioni, ognuna è una lista di Location
        
    def get_Locations(self, xml_file, xsd_file):
        try:
            schema = xmlschema.XMLSchema(xsd_file)
            if not schema.is_valid(xml_file):
                log_errors(xml_file, xsd_file)  # Logga eventuali errori di validazione
                return
            data = schema.to_dict(xml_file)
            
            # Itera sulle spedizioni e raccogli i dati di location
            for shipment in data["shipment"]:
                shipment_locations = []  # Array per le Location di una spedizione
                for location in shipment["location"]:
                    place = location["place"]
                    date = location["date"]
                    x = Location(place, date)   #TODO refactor the variable name
                    shipment_locations.append(x)
                self.shipments.append(shipment_locations)  # Aggiungi la spedizione all'array principale
            return self.shipments
            
            """
            for i, shipment in enumerate(self.shipments, start=1):
                print(f"Shipment {i}:")
                for loc in shipment:
                    print(f"  {loc}")
            """
                    
        except Exception as e:
            error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
            logging.error(error_message)
            
    def calculate_shipment_time(self, index):
        try:
            shipment = self.shipments[index]
            if not shipment:
                print("No locations found for this shipment")
                return
            
            # Estrai la prima e l'ultima data
            first_date_str = shipment[0].date
            last_date_str = shipment[-1].date  #takes the last element of the array
            
            # Converti le date in oggetti datetime
            first_date = datetime.fromisoformat(first_date_str)  #converts the string to a datetime object format=ISO 8601
            last_date = datetime.fromisoformat(last_date_str)
            
            total_time = last_date - first_date
            print(f"Total delivery time: {total_time}")
        
        except IndexError:
            print(f"Shipment index {index} is out of range")
        except ValueError as e:
            print(f"Date format error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
class times_to_xml:
    pass

def main():
    xmlfile = os.path.join(script_path, "shipment.xml")
    xsdfile = os.path.join(script_path, "shipment_schema.xsd")
    setup_logger()
    spedizioni = handle_shipment()
    shipments = []
    shipments = spedizioni.get_Locations(xmlfile, xsdfile)
    for i, shipment in enumerate(shipments, start=1):
        print(f"Shipment {i}:")
        for loc in shipment:
            print(f"  {loc}")
    spedizioni.calculate_shipment_time(0)
                
if __name__ == "__main__":
    main()