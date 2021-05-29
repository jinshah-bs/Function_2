class Contact:
    all_contacts = []

    def __init__(self, name, ph_no, email, ph_2=None):
        self.name = name
        self.ph_no = ph_no
        self.email = email
        self.ph_2 = ph_2
        Contact.all_contacts.append(self)

    def print_Contact(self):
        print(self.name, self.ph_no, self.email)


class SubContact(Contact):

    def message(self, text):
        print("Ya this class , subclass is inheriting")
        print("the proof is the name, {}, {}".format(self.name, text))
        print("Since LHS = RHS, the hypothesis is proved")


jb = Contact("Bala", 123456, "bala123")
div = SubContact('divak', 789456, "div789")

jb.print_Contact()
div.print_Contact()
print(Contact.all_contacts)

div.message('Hai div')
# jb.message('Hai div')

# jb = Contact('Bala', 123456789, 'bala@gmail.com', 4561237589)
# div = Contact('Div', 987654321, 'Div@div.com')
# div2 = Contact('Jin', 987654321, 'Div@div.com')
# print(jb.__dict__)
# print(div.__dict__)
# jb.print_Contact()
# div.print_Contact()
#
# for obj in Contact.all_contacts:
#     print(obj.name, obj.ph_no, obj.email, obj.ph_2)
