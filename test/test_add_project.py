def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.project.get_projects_list()
    flag = app.project.add_new_project(project)
    if flag:
        old_projects.append(json_projects)
    new_projects = app.project.get_projects_list()
    assert sorted(old_projects, key=lambda project:project.name) == sorted(new_projects, key=lambda project:project.name)