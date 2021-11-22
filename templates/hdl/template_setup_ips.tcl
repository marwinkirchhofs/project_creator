#
# configuration and output target generatio for Xilinx IPs used in the 
# _T_APP_NAME_T_ project
#
# This script needs to be run by Vivado in batch mode which is usually triggered 
# by an according make target.
#


############################################################
# SETUP
############################################################

# create ip output directory 
set	dir_ips ips_xilinx
file mkdir $dir_ips

# !!!TODO!!!
# adapt the part
set_part xc7z020clg484-1

# needed to avoid "non-existing project" error
current_fileset


############################################################
# IP CONFIGURATION
############################################################

#############################
# ILA
#############################

# AXI_LITE_2_NPE_ENGINE
create_ip -force -name ila -dir $dir_ips -module_name ila__T_APP_NAME_T_
set_property -dict [list                    \
    CONFIG.C_NUM_OF_PROBES  {16}            \
    CONFIG.C_ENABLE_ILA_AXI_MON  {false}            \
    CONFIG.C_MONITOR_TYPE  {Native}            \
    ] [get_ips ila__T_APP_NAME_T_]


############################################################
# GENERATE TARGETS
############################################################

generate_target all [get_ips]
