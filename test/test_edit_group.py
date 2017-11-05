from model.group import Group
from random import randrange
import random




def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    #group=random.choice(old_groups)
    #index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = random.choice(old_groups).id
    # app.session.login(username="admin", password="secret")
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.id = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # app.session.logout()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(header="test"))
    #old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)










#def test_edit_first_group(app):
    #app.session.login(username="admin", password="secret")
    #app.group.edit_first_group()
    #app.session.logout()