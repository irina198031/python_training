from sys import maxsize



class Contact:
    def __init__(self, fname=None, lname=None, homeaddress=None, phone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None, id=None,):

    #def __init__(self, fname=None, lname=None, id=None):
        self.fname=fname
        self.lname=lname
        self.homeaddress=homeaddress
        self.phone=phone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.secondaryphone=secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s" % (self.id, self.fname, self.lname, self.homeaddress, self.phone, self.email)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
