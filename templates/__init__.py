# Add this directory to the search path for imports
import sys, os
_TEMPLATES_ABS_PATH_ = os.path.realpath(__file__)
l_templates_path = _TEMPLATES_ABS_PATH_.split('/')[:-1]
sys.path.append( "/".join(l_templates_path) )

# from create_project_python import Project_Creator_Python
from create_project_python import create_project_python
