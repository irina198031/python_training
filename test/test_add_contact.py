# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize

def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com")
    app.contact.create(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




