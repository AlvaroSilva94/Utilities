#include <setjmp.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include "cmocka.h"

/******************************************************************************
 * Externals
 *****************************************************************************/
extern something order;
/******************************************************************************
 * Locals
 *****************************************************************************/

/******************************************************************************
 * Tests
 *****************************************************************************/

/**
* @brief Information from the plan in what to be tested
* 
* @componentname @componentName@
* @testfilename{@fileNameC@}
* @swrslink{@requirement@}
* @requirementstatus{@coverage@}
* ```
* @requirement@:
*
* @requirementTxt@
*
* @param state unused
* @sourcecode
**/

/* A test case that does nothing and succeeds. */
static void @test_case_id@(void **state) {

//Function to be tested
@functionFromReq@()

}


/******************************************************************************
 * Test Driver
 *****************************************************************************/
int main(int argc, char *argv[])
{
    int res = 0;
    struct CMUnitTest const utils_tests[] = {
        cmocka_unit_test(@test_case_id@),
        // TESTCASE_MULTIPLIER_INSERT_TESTCASES_HERE
    };

    res = cmocka_run_group_tests(utils_tests, 0, 0);

    return res;
    (void)argc;
    (void)argv;
}