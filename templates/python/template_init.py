# Add this directory to the search path for imports
import sys, os
__TC_SRC_DIR_TC__ABS_PATH_ = os.path.realpath(__file__)
l__T_SCR_DIR_T__path = __TC_SRC_DIR_TC__ABS_PATH_.split('/')[:-1]
__TC_SRC_DIR_TC__ABS_PATH_ = "/".join(l__T_SCR_DIR_T__path)
sys.path.append( __TC_SRC_DIR_TC__ABS_PATH_ )

# handle import of classes or scripts
