from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


        # создание контактов

    def create(self, contact):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):

        # init contact creation
            wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.fname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.homeaddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        #wd.find_element_by_name("DeleteSel()").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("test")
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def count(self):
        wd = self.app.wd
        #self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_contact_list(self):

        wd = self.app.wd
        self.app.open_home_page()
        contact_l = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = element.find_element_by_tag_name("td").get_attribute("id")
            contact_l.append(Contact(fname=firstname, lname=lastname, id=id))
        return contact_l



