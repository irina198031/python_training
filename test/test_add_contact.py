# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize
import pytest
import random
import string

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

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_test_add_contact(app, contact):


    old_contacts = app.contact.get_contact_list()
    #contact = Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com")
    app.contact.create(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



