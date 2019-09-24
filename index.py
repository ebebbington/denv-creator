from classes.validate import Validate
from classes.project import Project

Project = Project()
attrs = vars(Project)
print(','.join('%s: %s' % item for item in attrs.items()))
Project.create_base_files()

# todo :: implement checks for which containers are asked to create
# create dockerfiles
# create necessary files based on container
# initialise git repo