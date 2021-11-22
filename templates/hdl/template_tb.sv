`timescale 1ns/1ps

/*
* testbench for _T_APP_NAME_T_
* 
* company:
* author/engineer:
* creation date:
* project name:
* tool versions:
*/

import _T_APP_NAME_T__pkg::*;


module tb__T_APP_NAME_T__top;

    //----------------------------------------------------------
    // PARAMETERS
    //----------------------------------------------------------
   
    localparam              TB_DATAWIDTH        = 32; 


    //----------------------------------------------------------
    // TEST VECTORS
    //----------------------------------------------------------

    logic   [TB_DATAWIDTH-1:0]          test_vec_kernel    [ NUM_TESTS-1:0 ];

    // load stimuli files to variables
    initial begin
        test_vec_kernel         = '{NUM_TESTS {32'h0}};
        $readmemb(FILE_TEST_VEC_ENGINE_CONFIG, test_vec_engine_config);
    end


    //----------------------------------------------------------
    // SIGNALS
    //----------------------------------------------------------

    // clock period length
    int                     TC = 10;

    logic                   reset_done;

    //----------------------------
    // GLOBAL SIGNALS
    //----------------------------
    
	logic					clk;
	logic					rst_n;
	logic					clear;

    //----------------------------
    // RESULTS
    //----------------------------

        
    //----------------------------
    // DUT CONTROL STRUCTS
    //----------------------------
    
    ctrl_t                  ctrl__T_APP_NAME_T_;
    flags_t                 flags__T_APP_NAME_T_;
    
    
    //----------------------------------------------------------
    // OPERATION
    //----------------------------------------------------------
    
    //----------------------------
    // CLOCK
    //----------------------------
    
    task cycle(input int num_cycles=1);
        for (int i=0; i<num_cycles; i++) begin
            #TC;
        end
    endtask

    initial begin
        clk = 1;
    end

    always begin
        #(TC/2) clk = ~clk;
    end

    //----------------------------
    // RESET
    //----------------------------
    
    initial begin

        // defined state for engine control
        ctrl__T_APP_NAME_T_.start_valid             <= 0;

        // reset procedure
        rst_n      <= 1;
        reset_done <= 0;
        cycle(2);
        rst_n      <= 0;
        cycle(4);
        rst_n      <= 1;
        reset_done <= 1;
    end

    //----------------------------
    // OPERATION TASKS
    //----------------------------

    
    //----------------------------------------------------------
    // STIMULI
    //----------------------------------------------------------


    initial begin
        cycle(2);

        // WAIT FOR COMPLETED RESET
        while (~reset_done) cycle();
        cycle(2);

	end


    //----------------------------------------------------------
    // MODULES
    //----------------------------------------------------------

    //----------------------------
    // DUT
    //----------------------------

    _T_APP_NAME_T__top mod__T_APP_NAME_T__top (
        .clk					(clk),
        .rst_n					(rst_n),

        .ctrl_i					(ctrl__T_APP_NAME_T_),
        .flags_o				(flags__T_APP_NAME_T_)
    );

endmodule
