class Contacts:
    all_contacts = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class AddressHolder:

    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Friends(Contacts, AddressHolder):

    def __init__(self, name, email, ph, street, city, state, country):
        Contacts.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, country)
        self.ph_no = ph


jin = Friends("jin", "email", 8129960815, "a", "b", 'Kerala', "India")
print(Contacts.all_contacts)
jin2 = Contacts("Jin", "email2")
print(Contacts.all_contacts)
