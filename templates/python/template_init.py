# Add this directory to the search path for imports
import sys, os
__T_SRC_DIR_T__ABS_PATH_ = os.path.realpath(__file__)
l_templates_path = __T_SRC_DIR_T__ABS_PATH_.split('/')[:-1]
sys.path.append( "/".join(l_templates_path) )

# handle import of classes or scripts
