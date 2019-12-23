import sys
import time

sys.path.append(r'C:\Windows\Microsoft.NET\assembly\GAC_64\Newport.XPS.CommandInterface\v4.0_1.3.0.0__9a267756cf640dcf')
import clr
clr.AddReference("Newport.XPS.CommandInterface")
from CommandInterfaceXPS import *
import System
xps = XPS()
class MyXPS:
    def __init__(self):
        address = "192.168.254.254"
        port = 5001

        result = xps.OpenInstrument(address, port, 1000)
        if result == 0:
            print('Connection ', address, ":", port, " => Successful")
        else:
            print('Connection ', address, ":", port, " => failure ", result)
        result,errstring = xps.GroupInitialize('Group1','')
        if result == 0 :
            print('group initialize successful')
        else:
            print('group initialize fail')
        xps.GroupMotionEnable('Group1', '')
    def measureMove(self,move):
        xps.GroupMoveRelative('Group1', move, 1, '')
    def close(self):
        xps.CloseInstrument()