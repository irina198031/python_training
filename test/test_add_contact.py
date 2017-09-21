# -*- coding: utf-8 -*-

from model.contact import Contact

def test_test_add_contact(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com"))
    app.session.logout()



