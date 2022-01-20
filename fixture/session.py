class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(self.app.username)
        wd.find_element_by_css_selector("input[type='submit']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(self.app.password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/a/span").click()
        wd.find_element_by_link_text("Выход").click()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[contains(@href, 'logout')]")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//span[@class = 'user-info']").text

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self):
        if self.is_logged_in():
            if self.is_logged_in_as(self.app.username):
                return
            else:
                self.logout()
        self.login()
