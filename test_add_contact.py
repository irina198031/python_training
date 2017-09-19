# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):

    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com"))
    app.logout()



