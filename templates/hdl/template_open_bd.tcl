
# Script to be sourced by Vivado in batch or tcl mode.
# It opens the block design associated with the app either with or without a 
# debug core. If no block design is present, it just opens Vivado with a new 
# empty block design.
#
# The designs opened via this script are only meant for setting up and 
# afterwards exporting the top level block design. Building the hardware is done 
# via the 'build_hw_*' scripts
#
# Although the plain non-debug hardware build itself uses a non-project 
# workflow, the respective block design modification and setting up is done in 
# the GUI with an in-memory project. This way, automatic adaptations take place 
# like for example slightly tuning the clock frequencies such that they are 
# compliant with the available clock dividers. 
# 
#
# arguments:
#   0: if "debug", the block design with ILA core is loaded (and exported); 
#   otherwise (or if not given), the plain hardware is configured


###########################################################
# SETUP
###########################################################

# source helper functions for implementation steps (also sets up input and 
# output directories)
source [file join [file dirname [info script]] vivado_hw_build_helper.tcl]

# set part for the _TT_BOARD_NAME_TT_
# (also automatically creating an in-memory design)
_TT_APP_ABBREV_TT__set_hw_platform _TT_BOARD_NAME_TT_

_TT_APP_ABBREV_TT__create_in_memory_proj _TT_BOARD_NAME_TT_

# debug setup
if {[lindex $argv 0] == "debug"} {
    set prj_name _T_APP_NAME_T__hw_debug
    set debug 1
} else {
    set prj_name _T_APP_NAME_T_
    set debug 0
}


###########################################################
# DESIGN LOADING
###########################################################

if {$debug == 0} {

    #############################
    # NON-DEBUG
    #############################

    # READ SOURCES

    # required for e.g. block design
    set_property source_mgmt_mode All [current_project]

    # rtl sources
    _TT_APP_ABBREV_TT__proj_read_src_files

    # load block design (complain if not present)
    if {[_TT_APP_ABBREV_TT__load_block_design $prj_name] == 1} {
        _TT_APP_ABBREV_TT__new_block_design $prj_name
    }

    start_gui

    _TT_APP_ABBREV_TT__open_block_design $prj_name

} else {

    #############################
    # DEBUG
    #############################

    # READ SOURCES

    # required for e.g. block design
    set_property source_mgmt_mode All [current_project]

    # rtl sources
    _TT_APP_ABBREV_TT__proj_read_src_files

    # load block design (complain if not present)
    if {[_TT_APP_ABBREV_TT__load_block_design $prj_name] == 1} {
        _TT_APP_ABBREV_TT__new_block_design $prj_name
    }

    start_gui

    _TT_APP_ABBREV_TT__open_block_design $prj_name
}

