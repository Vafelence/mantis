from model.project import Project
import random


def test_delete_project(app):
    app.session.ensure_login()
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name="test"))
    old_projects = app.soap.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects = app.soap.get_projects_list()
    old_projects.remove(project)
    assert old_projects == new_projects
