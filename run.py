#!/usr/bin/env python

import sys

class RunException(Exception):
    pass

class RunExceptionInvalidParameter(RunException):
    pass

def read_config(f):
    return int(f.readline())

def execute(param, base=1):
    try:
        return param + base
    except TypeError:
        raise RunExceptionInvalidParameter('invalid parameter')

if __name__ == "__main__":
    print(execute(int(sys.argv[1]), read_config(open('config', 'r'))))
