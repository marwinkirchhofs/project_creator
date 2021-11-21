# It performs the automated hardware build with and without a debug core for the 
# _TT_BOARD_NAME_TT_
# The plain hardware build uses Vivado's non-project workflow for a maximum of 
# configurability. However, Vivado does not support debug cores at block-design 
# level in non-project mode.  Hence, the debug hardware build is performed using 
# an in-memory-project workflow. For this reason, hardware configurations, even 
# clock frequency, may differ between the two build options.
#
# arguments:
#   0: if "debug", the hardware setup with ILA core is built; otherwise (or if 
#   not given), the plain hardware is built


# source helper functions for implementation steps (also sets up input and 
# output directories)
source [file join [file dirname [info script]] vivado_hw_build_helper.tcl]

# debug setup
if {[lindex $argv 0] == "debug"} {
    set prj_name _T_APP_NAME_T__hw_debug
    set debug 1
} else {
    set prj_name _T_APP_NAME_T_
    set debug 0
}

# set part for the zedboard 
# (also automatically creating an in-memory design)
_TT_APP_ABBREV_TT_set_hw_platform _TT_BOARD_NAME_TT_


###########################################################
# HARDWARE BUILD
###########################################################

# LOG DIR
# create directory for build logs (nothing happens if directory exists)
create_log_dir $prj_name

if {[lindex $argv 0] != "debug"} {

    #############################
    # NON-DEBUG
    #############################

    # READ SOURCES
    # required for e.g. block design
    set_property source_mgmt_mode All [current_project]

    # rtl sources
    _TT_APP_ABBREV_TT__nonproj_read_src_files

    # load block design (complain if not present)
    if {[_TT_APP_ABBREV_TT_load_block_design $prj_name] == 1} {
        puts "No block design is present for $prj_name! You first need to set up 
        and export a block design via the open_bd_* scripts (or more likely the 
        open_bd_* make targets)"

        exit
    }

    _TT_APP_ABBREV_TT_nonproj_generate_bd $prj_name

    # compile order
    update_compile_order -fileset sources_1

    # SYNTHESIS
    _TT_APP_ABBREV_TT_nonproj_synth_design $prj_name

    # PLACEMENT AND OPTIMIZATION
    _TT_APP_ABBREV_TT_nonproj_opt_place_design $prj_name

    # ROUTING
    _TT_APP_ABBREV_TT_nonproj_route_design $prj_name

    # HARDWARE OUTPUT FILES
    _TT_APP_ABBREV_TT_nonproj_write_hw $prj_name

} else {

    #############################
    # DEBUG
    #############################

    _TT_APP_ABBREV_TT_create_proj $prj_name _TT_BOARD_NAME_TT_

    # READ SOURCES

#     # required for e.g. block design
#     set_property source_mgmt_mode All [current_project]

    # rtl sources
    _TT_APP_ABBREV_TT_proj_read_src_files

    # enable debug include option
    _TT_APP_ABBREV_TT_proj_set_debug

    # load block design (complain if not present)
    if {[_TT_APP_ABBREV_TT_load_block_design $prj_name] == 1} {
        puts "No block design is present for $prj_name! You first need to set up 
        and export a block design via the open_bd_* scripts (or more likely the 
        open_bd_* make targets)"

        exit
    }

    _TT_APP_ABBREV_TT_proj_generate_bd $prj_name

    # compile order
    set_property top bd_${prj_name}_wrapper [get_filesets sources_1]
    update_compile_order -fileset sources_1

    # SYNTHESIS
    _TT_APP_ABBREV_TT_proj_synth_design $prj_name

    # IMPLEMENTATION
    _TT_APP_ABBREV_TT_proj_impl_design $prj_name

    # HARDWARE OUTPUT FILES
    _TT_APP_ABBREV_TT_proj_write_hw $prj_name
}

