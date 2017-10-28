
from model.contact import Contact
import random
import string

constant = [
    Contact(fname="fname1", lname="lname1", homeaddress="address1", phone="phone1", email="email1"),
    Contact(fname="fname1", lname="lname1", homeaddress="address1", phone="phone1", email="email1")

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata =   [Contact(fname= "", lname="", homeaddress="", phone="", email="")] + [
    Contact(fname=random_string("fname", 5), lname=random_string("lname", 5),
            homeaddress=random_string("address", 5), phone=random_phone(10), email=random_string("email", 5))

    for i in range(5)
]