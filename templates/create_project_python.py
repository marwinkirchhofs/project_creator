#!/usr/bin/env python3

# PYTHON PROJECT_CREATE
#
# Create a python project from the template in this directory

import os, re


def __load_template(f_template, app_name, src_dir=""):
    """loads the respective template file and correctly replaces all 
    placeholders according to the parameters

    :f_template: TODO
    :returns: TODO

    """
    # TODO: for e.g. the python __init__ file we might need identifiers if a 
    # placeholder shall be inserted in caps or not since there we have the same 
    # placeholder in caps and small...

    ##############################
    # READ FILE
    ##############################
    
    with open(f_template, "r") as f_in:
        s_lines_all = f_in.readlines()

    ##############################
    # PROCESS
    ##############################
    # -> parameterize the placeholders

    # TODO: if we know that this is useful, replace it by a dictionary. Or two 
    # dictionaries, a global one for all languages and then a second 
    # language-specific one. In this case, we can make this function a global 
    # one...
    s_lines = s_lines.replace("_T_APP_NAME_T_", app_name)
    s_lines = s_lines.replace("_T_SRC_DIR_T_", src_dir)

    return s_lines_all


def __create_main(app_name, src_dir):
    
    ##############################
    # READ TEMPLATE FILE
    ##############################

#     with open (_TEMPLATES_ABS_PATH_ + "/python/template_main.py", "r") as f_in:
#         template = f_in.readlines()
    template = __load_template(
            _TEMPLATES_ABS_PATH_ + "/python/template_main.py", 
            app_name, src_dir)

    ##############################
    # ADAPT
    ##############################
    # basically handle the special template placeholders (indicated by 
    # '_TT_*_TT_' instead of '_T_*_T_')

    template_out = ""

    for line in template:

        # SOURCE DIRECTORY
        if re.match(r'.*_TT_IMPORT_SRC_DIR_TT_.*', line):
            if src_dir:
                template_out.append(
"""# import """ + src_dir + """package
from """ + src_dir + """import *""")
            else:
                pass

        # SOME DUMMY OPTION
        elif re.match(r'some_dummy', line):
            pass

        # NOTHING SPECIAL
        # -> copy the line over
        else:
            template_out.append(line)


    ##############################
    # WRITE PROJECT FILE
    ##############################

    with open (app_name + ".py", "w") as f_out:
        f_out.writelines(template_out)


def __create_init(app_name, src_dir):
    
    ##############################
    # READ TEMPLATE FILE
    ##############################

#     with open (_TEMPLATES_ABS_PATH_ + "/python/template_main.py", "r") as f_in:
#         template = f_in.readlines()
    # TODO: use src_dir in capitals for this one
    template = __load_template(
            _TEMPLATES_ABS_PATH_ + "/python/template_init.py", 
            app_name, src_dir)

    ##############################
    # CREATE SOURCE DIRECTORY
    ##############################

    # (normally src_dir shouldn't exist, but why not check)
    if not os.path.isdir(src_dir):
        os.mkdir(src_dir)

    ##############################
    # ADAPT
    ##############################
    # basically handle the special template placeholders (indicated by 
    # '_TT_*_TT_' instead of '_T_*_T_')

    template_out = ""

    for line in template:

        # SOURCE DIRECTORY
        if re.match(r'.*_TT_IMPORT_SRC_DIR_TT_.*', line):
            if src_dir:
                template_out.append(
"""# import """ + src_dir + """package
from """ + src_dir + """import *""")
            else:
                pass

        # SOME DUMMY OPTION
        elif re.match(r'some_dummy', line):
            pass

        # NOTHING SPECIAL
        # -> copy the line over
        else:
            template_out.append(line)


    ##############################
    # WRITE PROJECT FILE
    ##############################

    with open (src_dir + "__init__.py", "w") as f_out:
        f_out.writelines(template_out)


def create_project_python(app_name, src_dir=False):
    """Create a python project from the template in this directory

    :app_name:  The name for the application -> the main file
    :src_dir:   String or Bool; Handles the creation of a source directory within the project directory that gets imported by the top level file. If a string, the directory is named after the string, if True, the directory is named "src". If False or empty, no directory is created
    :returns:   TODO

    """

    __create_main(app_name, src_dir)

    return 0
