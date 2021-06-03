class Contacts:
    all_contacts = list()

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class AddressHolder:

    def __init__(self, street="", city="", state="", country="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Friends(AddressHolder, Contacts):
    """
    This class will maintain the contact details of friends
    Here you have the followings option to enter
    ph, name, email, street, city, state, country
    """

    def __init__(self, ph='', **kwargs):
        super().__init__(**kwargs)
        self.ph_no = ph


Jin = Friends( ph=8129960815, name="jinshah", email='email1', street="str", state='state1', country='country')


print(Jin.city)