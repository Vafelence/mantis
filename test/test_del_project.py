import random
from model.project import Project


def test_del_project(app):
    config = app.config['web']
    if len(app.soap.get_projects(config['username'], config['password'])) == 0:
        app.project.add_new_project(Project(name="Del1", description="descr"))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.del_project_by_name(project.name)
    old_projects.remove(project)
    new_projects = app.soap.get_projects(config['username'], config['password'])
    assert sorted(old_projects, key=lambda project:project.name) == sorted(new_projects, key=lambda project:project.name)
