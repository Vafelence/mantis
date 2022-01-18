import jsonpickle
from model.project import Project
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_status():
    status = ['development', 'release', 'stable', 'obsolete']
    return "".join([random.choice(status)])


def random_view_status():
    view_status = ['public', 'private']
    return "".join([random.choice(view_status)])


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name1", 10), status=random_status(), view_status=random_view_status(),
            description=random_string("description", 15))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
