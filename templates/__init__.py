# Add this directory to the search path for imports
import sys, os
s_init_file_path = os.path.realpath(__file__)
l_templates_path = s_init_file_path.split('/')[:-1]
_TEMPLATES_ABS_PATH_ = "/".join(l_templates_path)
sys.path.append( _TEMPLATES_ABS_PATH_ )

# from create_project_python import Project_Creator_Python
from Project_Creator import Project_Creator
from Python_Project_Creator import Python_Project_Creator
