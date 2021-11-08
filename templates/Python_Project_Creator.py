#!/usr/bin/env python3

# PYTHON PROJECT_CREATE
#
# Create a python project from the template in this directory

import os, re
import Project_Creator

class Python_Project_Creator(Project_Creator.Project_Creator):


    def __init__(self):
        Project_Creator.__init__(self, "python")
        self.language = "python"


    def __create_main(app_name, src_dir):
        
        ##############################
        # READ TEMPLATE FILE
        ##############################

#     with open (_TEMPLATES_ABS_PATH_ + "/python/template_main.py", "r") as f_in:
#         template = f_in.readlines()
        template = __load_template(
                self.__TEMPLATES_ABS_PATH + "/python/template_main.py", 
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

        return 0


    def __create_init(app_name, src_dir):
        
        ##############################
        # READ TEMPLATE FILE
        ##############################

        template = __load_template(
                self.__TEMPLATES_ABS_PATH + "/python/template_init.py", 
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

        return 0


    def create_project(app_name, py_src_dir=False, **args):
        """Create a python project from the template in this directory

        :app_name:  The name for the application -> the main file
        :src_dir:   String or Bool; Handles the creation of a source directory within the project directory that gets imported by the top level file. If a string, the directory is named after the string, if True, the directory is named "src". If False or empty, no directory is created
        :returns:   TODO

        """

        __create_main(app_name, py_src_dir)
#         __create_init()

        return 0
