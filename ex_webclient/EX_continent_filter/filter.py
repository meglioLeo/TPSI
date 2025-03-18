class ContinentFilter:
    @staticmethod
    def find_most_populated_continent(continents):
        max_population = 0
        most_populated_code = ""
        for continent in continents:
            if continent.population > max_population:
                max_population = continent.population
                most_populated_code = continent.code
        return (continent for continent in continents if continent.code == most_populated_code)