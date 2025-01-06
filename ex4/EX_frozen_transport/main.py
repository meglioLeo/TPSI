import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system
from datetime import datetime #module for handling dates

#get the path of the script
global script_path
script_path = os.path.dirname(os.path.abspath(__file__))

global threshold  #global variable for the temperature threshold
threshold = -30.0

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
        
class measure:
    def __init__(self, temperature, date):
        self.temp = temperature
        self.date = date
    
    def __str__(self):
        return f"Temperature: {self.temp}, Timestamp: {self.date}"
    
class truck:
    def __init__(self, ID):
        self.ID = ID
        self.measures = []
        
    def add_measure(self, temperature, date):
        x = measure(temperature, date)
        self.measures.append(x)

def main():
    setup_logger()
    xml_file = os.path.join(script_path, "frozen_transport.xml")
    xsd_file = os.path.join(script_path, "frozen_transport_schema.xsd")
    is_over_threshold = False
    
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        if not schema.is_valid(xml_file):
            return
        data = schema.to_dict(xml_file)
        
        trucks = []
        exeeded_temperatures = []
        for truck_data in data["veichle"]:
            t = truck(truck_data["ID"])
            for measure_data in truck_data["measure"]:
                t.add_measure(measure_data["temperature"], measure_data["timestamp"])
                if measure_data["temperature"] > threshold:
                    is_over_threshold = True
                    time = datetime.fromisoformat(measure_data["timestamp"])
                    exeeded_temperatures.append((time - datetime(1970,1,1,00,00,00)).total_seconds())
            trucks.append(t)
            """for t in trucks:
            print(f"\nTruck ID: {t.ID}")
            for m in t.measures:
                print(m)"""
        print(f"\nThreshold exceeded: {is_over_threshold}")
        print(f"Timestamps of exceeded temperatures: {exeeded_temperatures}")
                
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        logging.error(error_message)
        
if __name__ == "__main__":
    main()