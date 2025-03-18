class CompanyModel:
    
    def __init__(self, id, name, address, zip_code, country, employeeCount, industry, marketcap, domain, logo, ceoName):
        self.id = id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.country = country
        self.employeeCount = employeeCount
        self.industry = industry
        self.marketcap = marketcap
        self.domain = domain
        self.logo = logo
        self.ceoName = ceoName

    @classmethod
    def from_json(cls, data):
        return cls(
            id = data.get("id"),
            name = data.get("name"),
            address = data.get("address"),
            zip_code = data.get("zip"),
            country = data.get("country"),
            employeeCount = data.get("employeeCount"),
            industry = data.get("industry"),
            marketcap = data.get("marketcap"),
            domain = data.get("domain"),
            logo = data.get("logo"),
            ceoName = data.get("ceoName")
        )
        
    def __repr__(self):
        return f"CompanyModel(id={self.id}, name='{self.name}', employeeCount={self.employeeCount})"