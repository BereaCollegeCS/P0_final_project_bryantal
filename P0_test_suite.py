######################################################################
# Author: Alex Bryant
# Username: bryantal
#
# Assignment: P0: Final Project Test Suite
# Purpose: Test Suite for the Final Project
#
######################################################################
from P0_bryantal import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def final_test_suite():
    """
    tests the different methods in the final code
    :return: None
    """
    
    testit(nim_gonna_win(4) == 4)
    testit(player_turn(5) == "Sorry, can't do that.  Choose another number (1-4):")


final_test_suite()

