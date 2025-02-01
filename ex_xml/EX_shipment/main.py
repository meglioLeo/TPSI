import xmlschema
import logging
import pprint
import os
from datetime import datetime
import xml.etree.ElementTree as ET

"""
This code does not follow the instructions properly: 
it doesn't show the list of just the following locations of a shipment,
but it shows all the locations of all the shipments.
"""

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
                    
        except Exception as e:
            error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
            logging.error(error_message)
            
    def print_shipments(self):
        for i, shipment in enumerate(self.shipments, start=1):
            print(f"Shipment {i}:")
            for loc in shipment:
                print(f"  {loc}")
            
    def calculate_shipment_time(self, index):
        try:
            shipment = self.shipments[index]
            if not shipment:
                print("No locations found for this shipment")
                return
            
            first_date_str = shipment[0].date
            last_date_str = shipment[-1].date  #takes the last element of the array
            
            # Converti le date in oggetti datetime
            first_date = datetime.fromisoformat(first_date_str)  #converts the string to a datetime object format=ISO 8601
            last_date = datetime.fromisoformat(last_date_str)
            
            total_time = last_date - first_date
            print(f"Total delivery time: {total_time}")
        
        except IndexError:
            print(f"Shipment index {index} is out of range")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
class time_in_xml:
    def __init__(self):
        self.times = []

    def get_time(self, shipments_arr):
        for shipment in shipments_arr:
            shipment_time = []
            for i in range(len(shipment) - 1):  # Iterate over indices, stopping at the second-last element
                date1 = shipment[i].date  # Access current shipment's date
                date2 = shipment[i + 1].date  # Access next shipment's date
                
                # Convert string dates to datetime objects
                date1 = datetime.fromisoformat(date1)
                date2 = datetime.fromisoformat(date2)
                difference_in_seconds = (date2 - date1).total_seconds()
                shipment_time.append(difference_in_seconds)
            self.times.append(shipment_time)
        """     
        print("Times between locations:")
        pprint.pprint(self.times)
        """
    
    def to_xml(self, xml_file):
        root = ET.Element("times")
        for shipment_times in self.times:
            shipment_element = ET.SubElement(root, "shipment")
            for time in shipment_times:
                time_element = ET.SubElement(shipment_element, "time")
                time_element.text = str(time)
        
        tree = ET.ElementTree(root)
        with open(xml_file, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
            

def main():
    xmlfile = os.path.join(script_path, "shipment.xml")
    xsdfile = os.path.join(script_path, "shipment_schema.xsd")
    setup_logger()
    spedizioni = handle_shipment()   #creates an object of the class handle_shipment
    spedizioni.get_Locations(xmlfile, xsdfile)   #fills an array with the arrays of Location objects
    spedizioni.print_shipments()   #prints the array of Location objects
    spedizioni.calculate_shipment_time(0)   #calculates the time between the first and the last location of the selected shipment
    time_calculator = time_in_xml()   #creates an object of the class time_in_xml
    time_calculator.get_time(spedizioni.shipments)   #fills an array with the time between the locations of each shipment
    time_calculator.to_xml(os.path.join(script_path, "times.xml"))   #creates an xml file with the datas of the array
    
if __name__ == "__main__":
    main()