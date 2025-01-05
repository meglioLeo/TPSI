import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system
from datetime import datetime,timedelta #module for working with dates and times
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
        
def calculate_available_percentage(data, selected_month, selcted_year):
    """
    This function calculates the percentage of available rooms in the selected month,
    by multipling the number of available rooms by the number of days in the selected month,
    and then dividing by the total number of rooms multiplied by the number of days.
    """
    room_count = len(data["available_rooms"]["room"])
    if room_count == 0:
        error_message = "No rooms available"
        logging.error(error_message)
        print("No rooms available")
        
    first_day_of_month = datetime(selcted_year, selected_month, 1)
    last_day_of_month = (first_day_of_month+timedelta(days=32)).replace(day=1)-timedelta(days=1)
    total_month_days = (last_day_of_month-first_day_of_month).days
    available_rooms_monthly = room_count * total_month_days
    reservation_days = 0
    
    for reservation in data["reservations"]["reservation"]:
        reservation_start = datetime.fromisoformat(reservation["start_date"])
        reservation_end = datetime.fromisoformat(reservation["end_date"])
        if reservation_start.year == selcted_year and reservation_start.month == selected_month \
        or reservation_end.year == selcted_year and reservation_end.month == selected_month \
        or reservation_start < first_day_of_month and reservation_end > last_day_of_month:
            overlap_start = max(reservation_start, first_day_of_month)
            overlap_end = min(reservation_end, last_day_of_month)          
            reservation_days += (overlap_end-overlap_start).days + 1
    
    occupancy_percentage = reservation_days/available_rooms_monthly*100 
    print(f"The occupancy percentage for {selected_month}/{selcted_year} is: {occupancy_percentage}%")
        
    
        
class reservation_in_xml:
    def __init__(self):
        self.reservations = []

def main():
    xml_file = os.path.join(script_path, "hotel_reservation.xml")
    xsd_file = os.path.join(script_path, "hotel_reservation_schema.xsd")
    setup_logger()
    data = get_data_from_xml(xml_file,xsd_file)
    if data is None:
        return
    calculate_available_percentage(data, 3, 2025)  #data, month, year
        
if __name__ == "__main__":
    main()