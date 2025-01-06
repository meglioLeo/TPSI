import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system
from datetime import datetime #module for handling dates

"""
This exercise does not involve two different xml files,
as I did  all the checks in the python script.
"""

#get the path of the script
global script_path
script_path = os.path.dirname(os.path.abspath(__file__))

global authorised_operators  #dictionary with authorised operators and the machines they can use
authorised_operators = {"123456789": [12345, 67890], 
                        "234567891": [54321], 
                        "345678912": [98765, 44556], 
                        "456789123": [11223], 
                        "567891234": [12345, 44556, 54321]}

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
        #print(f"\nValid data:")
        #pprint.pprint(data, indent=2, width=100) #pretty print the entire data structure
        return data
    
    except Exception as e:
        error_message = f"An unexpected error occurred while processing {xml_file}: {e}"
        logging.error(error_message)
        
def check_authentity(data, patient_fc):
    is_valid = True
    for outcome in data["outcome"]:
        #for patient_code in outcome["patient_code"]:
            #print(f"Patient code: {patient_code}")
            #print(f"Patient fc: {patient_fc}")
            #print(f"Outcome[patient_code]: {outcome['patient_code']}")
            if outcome["patient_code"] == patient_fc:
                blood_sample_date_str = outcome["date"]
                analysis_date_str = outcome["exams"]["exam_date"]
                operator_code = str(outcome["exams"]["operator_id"])
                #print(f"Operator code: {operator_code}")
                machine_serial = outcome["exams"]["machine_serial_number"]
                blood_sample_date = datetime.fromisoformat(blood_sample_date_str)
                analysis_date = datetime.fromisoformat(analysis_date_str)
                #print(f"Blood sample date: {blood_sample_date}")
                #print(f"Analysis date: {analysis_date}")
                #print(f"Machine serial: {machine_serial}")
                #print(f"authorised_operators[operator_code]: {authorised_operators[operator_code]}")
                if(analysis_date - blood_sample_date).days > 1:
                    #print((analysis_date - blood_sample_date).days)
                    is_valid = False
                    error_message = f"Analysis date is more than 2 days after blood sample date"
                    print(error_message)
                    logging.error(error_message)
                if operator_code not in authorised_operators:
                    is_valid = False
                    error_message = f"Operator code {operator_code} is not found"
                    print(error_message)
                    logging.error(error_message)
                if operator_code in authorised_operators:
                    if isinstance(machine_serial, list):
                        for i in range(len(machine_serial)):
                            if machine_serial[i] not in authorised_operators[operator_code]:
                                is_valid = False
                                error_message = f"Operator code {operator_code} is not authorized to use machine {machine_serial[i]}"
                                print(error_message)
                                logging.error(error_message)
                    else:
                        if machine_serial not in authorised_operators[operator_code]:
                            is_valid = False
                            error_message = f"Operator code {operator_code} is not authorized to use machine {machine_serial}"
                            print(error_message)
                            logging.error(error_message)                 
    return is_valid

def validate_exams(data, patient_fc):
    for outcome in data["outcome"]:
        if outcome["patient_code"] == patient_fc:
            result = float(outcome["exams"]["exam_result"])
            min_value = float(outcome["exams"]["exam_result_min"])
            max_value = float(outcome["exams"]["exam_result_max"])
            if result >= min_value and result <= max_value:
                print(f"Exam result is within the range: {result} [{min_value}-{max_value}]")
            else:
                print(f"Exam result is not within the range: {result} [{min_value}-{max_value}]")
                error_message = f"Exam result is not within the range: {result} [{min_value}-{max_value}]"
                logging.error(error_message)
        
def main():
    xmlfile = os.path.join(script_path, "medical_analysis.xml")
    xsdfile = os.path.join(script_path, "medical_analysis_schema.xsd")
    setup_logger()
    data = get_data_from_xml(xmlfile,xsdfile)
    if data is None:
        return
    authentity = check_authentity(data, "VRDLGU65C01F205T")
    print(f"The analysis is valid: {authentity}")
    if authentity:
        validate_exams(data, "VRDLGU65C01F205T")
    
if __name__ == "__main__":
    main()