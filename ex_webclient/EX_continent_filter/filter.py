class ContinentFilter:
    
    @staticmethod
    def find_most_populated_continent(continents):
        most_populated_continent = None
        for continent in continents:
            if most_populated_continent is None or continent.population > most_populated_continent.population:
                most_populated_continent = continent
        return most_populated_continent