import random
import time

from model.project import Project


def test_del_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.add_new_project(Project(name="Del1", status="development", view_status="public", description="descr"))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.del_project_by_name(project.name)
    old_projects.remove(project)
    new_projects = app.project.get_projects_list()
    assert sorted(old_projects, key=lambda project:project.name) == sorted(new_projects, key=lambda project:project.name)