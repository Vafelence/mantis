from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, inherit_global_categories=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global_categories = inherit_global_categories
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s;%s" % (self.name, self.status, self.view_status)

    def __eq__(self, other):
        return self.name is None or other.name is None or self.name == other.name

    def name_or_max(self):
        if self.name:
            return self.name
        else:
            return maxsize