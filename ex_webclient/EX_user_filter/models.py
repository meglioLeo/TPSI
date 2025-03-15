class UserModel:
    def __init__(self, id, name, company, username, email, address, zip, state, country, phone, photo):
        self.id = id
        self.name = name
        self.company = company
        self.username = username
        self.email = email
        self.address = address
        self.zip = zip
        self.state = state
        self.country = country
        self.phone = phone
        self.photo = photo

    @classmethod
    def from_json(cls, data):
        return cls(
            id = data.get("id"),
            name = data.get("name"),
            company = data.get("company"),
            username = data.get("username"),
            email = data.get("email"),
            address = data.get("address"),
            zip = data.get("zip"),
            state = data.get("state"),
            country = data.get("country"),
            phone = data.get("phone"),
            photo = data.get("photo")
        )
        