from model.contact import Contact
from random import randrange
import random


def test_edit_first_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com"))
    old_contacts = db.get_contact_list()

    #index = randrange(len(old_contacts))
    contact = Contact(fname="first", lname="last", homeaddress="address", email="first.last@gmail.com")
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

