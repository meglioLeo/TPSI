import json
from jsonschema import validate, ValidationError
import os

def validate_health(json_file_path, schema_file_path):
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
        print(f"The health data is not valid. See the log file: {error_log_file}")
    else:
        print("The health data is valid.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    json_file_path = os.path.join(script_dir, "health_monitoring.json")
    schema_file_path = os.path.join(script_dir, "health_monitoring.schema.json")
    
    validate_health(json_file_path, schema_file_path)