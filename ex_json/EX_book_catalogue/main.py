import json
import os
from jsonschema import validate, ValidationError

def validate_books(json_file_path, schema_file_path):
    # Carica lo schema dal file
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)

    # Carica i dati JSON
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    errors = []

    # Valida ogni libro nel catalogo
    for idx, book in enumerate(data.get("bookCatalogue", [])):
        try:
            validate(instance=book, schema=schema)
        except ValidationError as e:
            errors.append(f"Libro {idx + 1} Errore: {e.message}")

    # Se ci sono errori, scrivili in un file di log
    if errors:
        error_log_file = json_file_path.replace(".json", "_errors.log")
        with open(error_log_file, "w") as err_file:
            err_file.write("\n".join(errors))
        print(f"Alcuni libri non sono validi. Vedi il file di log: {error_log_file}")
    else:
        print("Tutti i libri sono validi.")

if __name__ == "__main__":
    # Determina la directory dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Percorsi dei file JSON e dello schema
    json_file_path = os.path.join(script_dir, "book_catalogue.json")
    schema_file_path = os.path.join(script_dir, "book_catalogue.schema.json")

    # Esegui la validazione
    validate_books(json_file_path, schema_file_path)
