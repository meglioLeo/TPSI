import json
import os
from jsonschema import validate, ValidationError


def validate_result (json_file_path, schema_file_path):
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)
        
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        
    errors = []
    
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"Error: {e.message}")
        
    if errors:
        error_log_file = json_file_path.replace(".json", "_errors.log")
        with open(error_log_file, "w") as err_file:
            err_file.write("\n".join(errors))
        print(f"The medical result data is not valid. See the log file: {error_log_file}")
    else:
        print("The medical result data is valid.")
        
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    json_file_path = os.path.join(script_dir, "medical_result.json")
    schema_file_path = os.path.join(script_dir, "medical_result.schema.json")
    
    validate_result(json_file_path, schema_file_path)