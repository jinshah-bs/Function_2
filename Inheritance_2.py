class SearchContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name.casefold() in contact.name.casefold():
                matching_contacts.append(contact)
        return matching_contacts


class Contacts:
    all_contacts = SearchContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class Friends(Contacts):

    def __init__(self, name, email, ph_no):
        super().__init__(name, email)
        self.ph_no = ph_no


f = Friends("Jin1", "email.jin", 8129960815)
c = Contacts("Jin2", "email2")

for contacts in Contacts.all_contacts:
    print(contacts.name)

# c1 = Contacts("Jin A", "email")
# c2 = Contacts("lalu", "email")
# c3 = Contacts("Div", "email")
# c4 = Contacts("JB", "email")
# c5 = Contacts("Jin B", "email")
# c6 = Contacts("Kottala Rajin", "email")
#
# unselected = Contacts.all_contacts
# lis = unselected.search('jin')
# for contact in lis:
#     print(contact.name, contact.email)

# for contact in Contacts.all_contacts:
#     print(contact.name, contact.email)
#
# print(type(Contacts.all_contacts))
