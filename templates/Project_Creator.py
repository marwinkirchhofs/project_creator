#!/usr/bin/env python3

# PROJECT CREATOR
# This class is meant as a superclass for language-specific project creators.  
# The main reason is (kinda stupid): It's neat to have __TEMPLATES_ABS_PATH as a 
# variable accessible to all language-specific functions. As python doesn't have 
# global variables, initiating this during the import via the __init__.py 
# doesn't help the function within imported modules. So make everything classes, 
# have the subclasses calling this super-constructor which sets up the necessary 
# variable. Straightforward, huh?

import os, re


class Project_Creator():
    """Superclass for all language-specific Project_Creator classes.
    The main reason is to set up __TEMPLATES_ABS_PATH as a class variable such 
    that all language-specific functions have access...
    """

    def __init__(self, language):

        # __TEMPLATES_ABS_PATH path private for the class to let all called 
        # methods know where to find the templates
        s_class_file_path = os.path.realpath(__file__)
        l_templates_path = s_class_file_path.split('/')[:-1]
        s_templates_path = "/".join(l_templates_path)
        self.__TEMPLATES_ABS_PATH = os.path.join(s_templates_path, language)


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
        s_lines = s_lines.replace("_TC_APP_NAME_TC_", app_name.upper())
        s_lines = s_lines.replace("_T_SRC_DIR_T_", src_dir)
        s_lines = s_lines.replace("_TC_SRC_DIR_TC_", src_dir.upper())

        return s_lines_all


    def create_project(self):
        print("Please implement this function for each language-specific Project_Creator!")
        

        
