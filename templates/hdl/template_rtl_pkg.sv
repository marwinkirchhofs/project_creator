
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
*/


package _T_APP_NAME_T__pkg;

    //----------------------------
    // PARAMETER
    //----------------------------

    parameter           DUMMY   = 32;

    //----------------------------
    // FLAGS/CTRL
    //----------------------------

    typedef struct packed {
        logic               start_ready; 
    } flags_t;

    typedef struct packed {
        logic               start_valid; 
    } ctrl_t;

    //----------------------------
    // STATE MACHINE
    //----------------------------

    typedef enum {
        READY,
        BUSY
    } state_t;


endpackage: _T_APP_NAME_T__pkg
