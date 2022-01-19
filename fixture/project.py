from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_overview_page.php"):
            wd.find_element_by_link_text("Управление").click()

    def open_manage_projects_page(self):
        wd = self.app.wd
        self.open_manage_page()
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Управление проектами").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_xpath(field_name).click()
            wd.find_element_by_xpath(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        #wd.find_element_by_xpath("//select[@id='project-status']").click()
        #wd.find_element_by_xpath("//select[@id='project-status']").send_keys("выпущен")
        self.change_select_value("//select[@id='project-status']", project.status)
        self.change_select_value("//select[@id='project-view-state']", project.view_status)
        #wd.find_element_by_xpath("//select[@id='project-view-state']").click()
        #wd.find_element_by_xpath("//select[@id='project-view-state']").send_keys("публичный")
        self.change_field_value("description", project.description)

    def create_project(self, project_data):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div/form/button").click()
        self.fill_project_form(project_data)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        self.project_cache = None

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

    def delete_project(self, name):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.select_project_by_name(name)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.project_cache = None

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_cache = []
            self.open_manage_projects_page()
            table = wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div/form/button")
            rows = table.find_elements_by_css_selector("tr")[2:]
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                project_name = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=project_name,
                                                  status=status,
                                                  view_status=view_status,
                                                  description=description))
        return list(self.project_cache)
