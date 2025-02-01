import json
import os
from jsonschema import validate, ValidationError

def validate_books(json_file_path, schema_file_path):
    # Load the schema from the file
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)

    # Load the JSON data
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    errors = []

    # Validate each book in the catalog
    for idx, book in enumerate(data.get("bookCatalogue", [])):
        try:
            validate(instance=book, schema=schema)
        except ValidationError as e:
            errors.append(f"Book {idx + 1} Error: {e.message}")

    # If there are errors, write them to a log file
    if errors:
        error_log_file = json_file_path.replace(".json", "_errors.log")
        with open(error_log_file, "w") as err_file:
            err_file.write("\n".join(errors))
        print(f"Some books are not valid. See the log file: {error_log_file}")
    else:
        print("All books are valid.")

if __name__ == "__main__":
    # Determine the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths to the JSON file and the schema file
    json_file_path = os.path.join(script_dir, "book_catalogue.json")
    schema_file_path = os.path.join(script_dir, "book_catalogue.schema.json")

    # Run the validation
    validate_books(json_file_path, schema_file_path)
