#!/usr/bin/env python

class RunException(Exception):
    pass

class RunExceptionInvalidParameter(RunException):
    pass

def read_config():
    return int(open('config', 'r').readline())

def execute(param, base=1):
    try:
        return param + base
    except TypeError:
        raise RunExceptionInvalidParameter('invalid parameter')

if __name__ == "__main__":
    print(execute(1, read_config()))
