import json
import os
from jsonschema import validate, ValidationError

#this class represents a single medical exam, not the whole JSON data
class MedicalResult:
    def __init__(self, patientName, patientSurname, samplingDate, analysisType, result, unitOfMeasure, resultRange, outcome):
        self.patientName = patientName
        self.patientSurname = patientSurname
        self.samplingDate = samplingDate
        self.analysisType = analysisType
        self.result = result
        self.unitOfMeasure = unitOfMeasure
        self.resultRange = resultRange
        self.outcome = outcome
        
    #this method is used to convert the object to a dictionary
    def to_dict(self):
        return {
            "patientName": self.patientName,
            "patientSurname": self.patientSurname,
            "samplingDate": self.samplingDate,
            "analysisType": self.analysisType,
            "result": self.result,
            "unitOfMeasure": self.unitOfMeasure,
            "resultRange": self.resultRange,
            "outcome": self.outcome
        }
        
    #this method is used to create an object from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            patientName=data["patientName"],
            patientSurname=data["patientSurname"],
            samplingDate=data["samplingDate"],
            analysisType=data["analysisType"],
            result=data["result"],
            unitOfMeasure=data["unitOfMeasure"],
            resultRange=data["resultRange"],
            outcome=data["outcome"]
        )
        
    #this method is used to update the outcome of the exam after the calculation
    def update_outcome(self, outcome):
        self.outcome = outcome

def validate_result (json_file_path, schema_file_path):
    #load the schema from the file
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)
        
    #load the JSON data file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        
    errors = []
    
    #validate the whole JSON data
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"Error: {e.message}")
        
    #if there are errors, write them to a log file
    if errors:
        error_log_file = json_file_path.replace(".json", "_errors.log")
        with open(error_log_file, "w") as err_file:
            err_file.write("\n".join(errors))
        print(f"The medical result data is not valid. See the log file: {error_log_file}")
    else:
        print("The medical result data is valid.")
        
def calculate_outcome(json_file_path):
    
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        
    medical_results = []
    
    for exams in data["medicalExams"]:
        for exam in exams:
            medical_result = MedicalResult.from_dict(exam)
            medical_results.append(medical_result)
            
    for exam in medical_results:
        result_range = exam.resultRange
        min_value = result_range["min"]
        max_value = result_range["max"]
        result = exam.result
        if result < min_value:
            outcome = "Low"
        elif result > max_value:
            outcome = "High"
        else:
            outcome = "Normal"
        exam.update_outcome(outcome)
    
    # print("Medical results with outcomes:")
    # for idx, exam in enumerate(medical_results):
    #     print(f"Exam {idx + 1}: {exam.to_dict()}")
    
    update_json_file(json_file_path, medical_results)
    
def update_json_file(json_file_path, medical_results):
    
    updated_exams_group = [exam.to_dict() for exam in medical_results]
    updated_data = {
        "medicalExams": updated_exams_group
    }
    
    with open(json_file_path, "w") as json_file:
        json.dump(updated_data, json_file, indent=4)  #delete the old data and write the new one
    print(f"Il file {json_file_path} è stato aggiornato.")
        
        
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    json_file_path = os.path.join(script_dir, "medical_result.json")
    schema_file_path = os.path.join(script_dir, "medical_result.schema.json")
    
    validate_result(json_file_path, schema_file_path)
    calculate_outcome(json_file_path)