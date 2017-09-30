from model.contact import Contact

def test_edit_first_contact(app):

    if app.contact.count() == 0:
        app.contact.create(Contact(fname="first", lname="last", homeaddress="address", phone="789456123", email="first.last@gmail.com"))

    #app.open_home_page()

    app.contact.edit_first_contact()
    # app.session.logout()
