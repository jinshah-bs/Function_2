class Contacts:
    all_contacts = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)

    def print(self):
        print("hai")


class Mailer:
    def sent_mail(self, message):
        print("Sending mail to {}".format(self.email))
        print(message)


class EmailContacts(Contacts, Mailer):
    pass


jin1 = EmailContacts("Jin1", "email@1")
jin2 = EmailContacts("Jin2", "email@2")

jin1.sent_mail("hai bro")
jin1.print()
print()
jin2.sent_mail("This is a spam mail")

