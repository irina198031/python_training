from sys import maxsize



class Contact:
    def __init__(self, fname=None, lname=None, homeaddress=None, phone=None, email=None, id=None, mobilephone=None, workphone=None, secondaryphone=None):
    #def __init__(self, fname=None, lname=None, id=None):
        self.fname=fname
        self.lname=lname
        self.homeaddress=homeaddress
        self.phone=phone
        self.email=email
        self.id = id
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.secondaryphone=secondaryphone

    def __repr__(self):
        return "%s:%s" % (self.id, self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fname == other.fname and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
