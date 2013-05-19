#! /usr/bin/env python

import os

files = ["test1.pyc", "test2.pyc", "test~", "#test.pyc#"]
rep_OK = []
rep_FAIL = []

def print_report(ok, fail):
    """ok and fail - seq"""
    print "in report: {} ; {}".format(str(ok), str(fail))

    print "{0} files deleted:{1}".format(len(ok), " ,".join([str(s) for s in ok]))
    print "{0} files not deleted:{1}".format(len(fail), " ,".join([str(s) for s in fail]))

def rem(files):
    """removes all files in seq"""
    rep_OK, rep_FAIL = [],[]
    for f in files:
        try:
            print "removing.. ", f
            os.remove(f)
        except OSError:
            print f, "exception"
            rep_FAIL.append(f)
            continue
        else:
            print f, "its OK, else branch"
            rep_OK.append(f)
        finally:
            print "returning..."
    return (rep_OK, rep_FAIL)
        
#if __name__ == "main":
rep_OK, rep_FAIL = rem(files)
print_report(rep_OK, rep_FAIL)
