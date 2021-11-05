#!/usr/bin/env python3

# TOP-LEVEL SCRIPT PROJECT_CREATE
#
# The script is used to load the language-specific template scripts, call the 
# respective create_project function and pass the given parameters to it

from optparse import OptionParser
import os, sys

# IMPORT LANGUAGE-SPECIFIC SCRIPTS
# add templates path to python's search path
def add_templates_path():
    s_abs_path = os.path.realpath(__file__)
    l_templates_path = s_abs_path.split('/')[:-1] + ["templates"]
    system.path.append( "/".join(l_templates_path) )

# add_templates_path()
from templates import *


############################################################
# "GLOBAL" VARS
############################################################

supported_languages = "c cpp python".split()


############################################################
# FUNCTION DEFINITIONS
############################################################


def create_project(language, app_name, create_dir=True, **args):
    """Create a project for the given language -> basically calls the respective 
    create_project_* function

    By default, the project is created 

    :language:      The language to create a project for
    :create_dir:    If True, a new top-level project is created whose name is 
    equal to the application name (default: True)
    :args:          language-specific arguments as defined in the respective 
    create_project_* functions
    :returns: TODO

    """

    if not language in supported_languages:
        # TODO: make this an error message
        print("'" + language + "' is not a supported language!")
        return 1

    ##############################
    # GENERAL ACTIONS
    ##############################
    
    # PROJECT DIRECTORY
    # The application directory gets created if not disabled and afterwards it 
    # is ensured that the application directory (newly created or not) is the 
    # working directory when calling the language-specific function
    if create_dir:
        if not os.path.isdir(app_name):
            os.mkdir(app_name)
        os.chdir(app_name)
 
    ##############################
    # LANGUAGE-SPECIFIC PROJECT CREATION
    ##############################

    if language == "c":
        pass
    elif language == "cpp":
        pass
    elif language == "python":
        create_project_python(app_name)
    
    return 0


############################################################
# MAIN
############################################################

if __name__ == "__main__":
    
    ##############################
    # OPTION PARSING
    ##############################
    
    parser = OptionParser()
    parser.add_option("-l",
            dest="language",
            help="""the language for which to build a project; valid options:
""" + ", ".join(supported_languages)
)
    parser.add_option("-p",
            action="store_true",
            dest="renew_plot",
            help="if set, the corresponding plot will be renewed using \
plot_template_single_layer",
            )

    (options, args) = parser.parse_args()

    ##############################
    # CHECK REQUIRED ARGUMENTS
    ##############################

    # LANGUAGE
    if not options.language:
        parser.error("Language not specified!")
    # APP NAME
    if not args:
        parser.error("Application name not specified!")

    language = options.language
    app_name = args[0]

    ##############################
    # PROJECT CREATION
    ##############################
    # use the function exit code as the script exit code

    sys.exit( create_project(language, app_name, options) )

