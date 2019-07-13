#!/usr/bin/env python

class RunException(Exception):
    pass

class RunExceptionInvalidParameter(RunException):
    pass

def execute(param):
    try:
        return param + 1
    except TypeError:
        raise RunExceptionInvalidParameter('invalid parameter')

if __name__ == "__main__":
    print(execute(1))
