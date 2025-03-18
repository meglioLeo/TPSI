class ContinentModel:
    def __init__(self, code, name, areaSqKm, population, lines, countries, oceans, developedCountries):
        self.code = code
        self.name = name
        self.areaSqKm = areaSqKm
        self.population = population
        self.lines = lines
        self.countries = countries
        self.oceans = oceans
        self.developedCountries = developedCountries

    @classmethod
    def from_json(cls, data):
        return cls(
            code = data.get("code"),
            name = data.get("name"),
            areaSqKm = data.get("areaSqKm"),
            population = data.get("population"),
            lines = data.get("lines"),
            countries = data.get("countries"),
            oceans = data.get("oceans"),
            developedCountries = data.get("developedCountries")
        )
    
    def __repr__(self):
        return f"{self.name} ({self.code})"