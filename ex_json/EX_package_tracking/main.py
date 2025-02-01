import json
import os
from jsonschema import validate, ValidationError

def validate_packages(json_file_path, schema_file_path):
    # Load the schema from the file
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)
        
    # Load the JSON data
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    
    errors = []
    
    for idx, package in enumerate(data.get("packageTracking", [])): #the empty array doesn't return an error
        try:
            validate(instance=package, schema=schema)
        except ValidationError as e:
            errors.append(f"Package {idx + 1} Error: {e.message}")
            
    if errors:
        error_log_file = json_file_path.replace(".json", "_errors.log")
        with open(error_log_file, "w") as err_file:
            err_file.write("\n".join(errors))
        print(f"Some packages are not valid. See the log file: {error_log_file}")
    else:
        print("All packages are valid.")
        
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    json_file_path = os.path.join(script_dir, "package_tracker.json")
    schema_file_path = os.path.join(script_dir, "package_tracker.schema.json")
    
    validate_packages(json_file_path, schema_file_path)