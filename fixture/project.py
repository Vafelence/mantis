import time

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_xpath("//a[contains(text(),'Manage')]").click()
            wd.find_element_by_xpath("// a[contains(text(), 'Manage Projects')]").click()

    def del_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("status").send_keys(project.status)
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_name("view_state").send_keys(project.view_status)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None
        try:
            if wd.find_element_by_xpath("//*/text()[normalize-space(.)='A project with that name already exists. Please go back and enter a different name.']/parent::*"):
                flag = False
        except:
            flag = True
        return flag

    project_cache = None

    def get_projects_list(self):
        wd = self.app.wd
        self.open_projects_page()
        self.project_cache = []
        for project in wd.find_elements_by_css_selector("tr[class*='row']"):
            cells = project.find_elements_by_tag_name("td")
            if len(cells) == 5:
                name = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, status=status, view_status=view_status, description=description))
        self.project_cache.pop(0)
        return list(self.project_cache)
