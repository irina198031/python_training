from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # app.session.logout()



def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    old_groups = app.group.get_group_list()
    #app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # app.session.logout()









#def test_edit_first_group(app):
    #app.session.login(username="admin", password="secret")
    #app.group.edit_first_group()
    #app.session.logout()