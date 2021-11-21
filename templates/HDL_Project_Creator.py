#!/usr/bin/env python3

# HDL PROJECT_CREATE
#
# Create an HDL project from the template in this directory

import os, re, shutil
import Project_Creator

class HDL_Project_Creator(Project_Creator.Project_Creator):


    def __init__(self):
        super().__init__("hdl")
        self.language = "hdl"


    def __create_main(self, app_name):

        ##############################
        # PROJECT DIRECTORIES
        ##############################
        
        name_rtl_dir = "rtl"

        for name_dir in [name_rtl_dir]:
            if not os.path.isdir(name_dir):
                os.mkdir(name_dir)

        ##############################
        # MAIN 
        ##############################

        # TODO

#         shutil.copy(f"{self.TEMPLATES_ABS_PATH}/template_main.cpp",
#                     f"{name_rtl_dir}/main.cpp")
        
#         ##############################
#         # READ TEMPLATE FILE
#         ##############################
# 
# #     with open (TEMPLATES_ABS_PATH_ + "/python/template_main.py", "r") as f_in:
# #         template = f_in.readlines()
#         template = self._load_template(
#                 self.TEMPLATES_ABS_PATH + "/template_main.cpp", # TODO: os.path.join()
#                 app_name)
# 
#         ##############################
#         # ADAPT
#         ##############################
#         # basically handle the special template placeholders (indicated by 
#         # '_TT_*_TT_' instead of '_T_*_T_')
# 
#         template_out = template
# 
#         ##############################
#         # WRITE PROJECT FILE
#         ##############################
# 
#         with open ("main.cpp", "w") as f_out:
#             f_out.writelines(template_out)

        return 0


    def __create_tb(self, app_name):
        # TODO
        pass


    def __create_bd_scripts(self, app_name):
        # TODO
        pass


    def __create_sim_questa(self, app_name):
        # TODO
        pass


    def __create_sim_verilator(self, app_name):
        # TODO
        pass


    def __create_xip_scripts(self, app_name):
        # TODO
        pass


    def __create_xsdk_scripts(self, app_name):
        # TODO
        pass


    def create_project(self, app_name, 
            vimspector=False, git=False, cuda=False,
            **args):
        """Create an HDL project from the template in this directory

        :app_name:  The name for the application -> the main file
        :returns:   TODO

        """

        # LAUNCH FILE CREATION
        self.__create_main(app_name)
        self.__create_tb(app_name)

        # set up
#         self.__run_cmake()


        return 0
