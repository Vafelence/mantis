

def test_add_project(app, json_projects):
    project = json_projects
    config = app.config['web']
    old_projects = app.soap.get_projects(config['username'], config['password'])
    app.project.add_new_project(project)
    new_projects = app.soap.get_projects(config['username'], config['password'])
    flag = app.project.add_new_project(project)
    if flag:
        old_projects.append(json_projects)
    assert sorted(old_projects, key=lambda project:project.name) == sorted(new_projects, key=lambda project:project.name)
