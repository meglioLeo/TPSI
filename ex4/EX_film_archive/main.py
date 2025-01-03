import pprint #module for pretty printing
import xmlschema #module for validating xml files
import logging #module for logging
import os #module for interacting with the operating system

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
        
def get_best_film(data):
    best_films = []
    for film in data["film"]:
        #pprint.pprint(film, indent=2, width=100)

        avg = 0
        counter = 0
        film_actors = []
        film_directors = []
        
        for rating in film["ratings"]["rating"]:
            #pprint.pprint(rating["value"], indent=2, width=100)
            review_value = int(rating["value"])  # Convertilo in un intero
            avg += review_value
            counter += 1
        if counter > 0:
            avg = avg / counter
            if avg > 8:
                for director in film["directors"]["director"]:
                    director_name = director["name"] + " " + director["surname"]
                    film_directors.append(director_name)
                for actor in film["actors"]["actor"]:
                    actor_name = actor["name"] + " " + actor["surname"]
                    film_actors.append(actor_name)
                print(f"Film: {film['title']}")
                print(f"Directors: {film_directors}")
                print(f"Actors: {film_actors}")
                print(f"Average rating: {avg}")
                print("\n")

def main():
    xml_file = os.path.join(script_path, "film_archive.xml")
    xsd_file = os.path.join(script_path, "film_archive_schema.xsd")
    setup_logger()
    data = get_data_from_xml(xml_file, xsd_file)
    #pprint.pprint(data, indent=2, width=100)
    if data is None:
        return
    get_best_film(data)    
    
if __name__ == "__main__":
    main()
    
    
    
"""
            #pprint.pprint(film["ratings"], indent=2, width=100)
            pprint.pprint(pippo, indent=2, width=100)
            review_value = int(rating["value"])
            avg += review_value
            #print(f"Rating value: {rating["value"]}")
            #pprint.pprint(f"pippo: {film['ratings']}", indent=2, width=100)
            counter += 1
        avg = avg/counter
        if avg > 8:
            for director in film["directors"]:
                director_name = director["name"] + " " + director["surname"]
                film_directors.append(director_name)
            for actor in film["actors"]:
                actor_name = actor["name"] + " " + actor["surname"]
                film_actors.append(actor_name)
            print(f"Film: {film['title']}, \nDirectors: {film_directors}, \nActors: {film_actors}, \nAverage rating: {avg}")
"""