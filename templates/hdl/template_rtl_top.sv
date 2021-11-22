
/*
* company:
* author/engineer:
* creation date:
* project name:
* target devices:
* tool versions:
*
*
* * description:
*
*
* * interface:
*
*		[port name]		- [port description]
* * inputs:
*       clk
*       rst_n
* * outputs:
*/

import _T_APP_NAME_T__pkg::*;

module _T_APP_NAME_T__top (

`ifdef DEBUG
    // debug-only signals for wiring to a top-level block design ILA
`endif

	input                               clk,
	input                               rst_n,

    input   ctrl_t                      ctrl_i,
    output  flags_t                     flags_o
);


    //----------------------------------------------------------
    // INTERNAL SIGNALS
    //----------------------------------------------------------

    //----------------------------
    // FSM
    //----------------------------

    state_t                                 state;

`ifdef DEBUG
`endif


    //----------------------------------------------------------
    // OPERATION
    //----------------------------------------------------------


    //----------------------------------------------------------
    // SUBMODULES
    //----------------------------------------------------------
    

endmodule

