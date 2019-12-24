import sys
import time
import array
sys.path.append(r'C:\Windows\Microsoft.NET\assembly\GAC_64\Newport.XPS.CommandInterface\v4.0_1.3.0.0__9a267756cf640dcf')
import clr
clr.AddReference("Newport.XPS.CommandInterface")
from CommandInterfaceXPS import *
import System
address="192.168.254.254"
port=5001
xps = XPS()
result = xps. OpenInstrument(address, port, 1000)
if result == 0 :
    print('Connection ', address, ":", port, " => Successful")
else:
    print('Connection ', address, ":", port, " => failure ", result)

# print('---------------- Object list ----------------')
# result, response, errString = xps.ObjectsListGet('','')
# objectList = response.split(';')
# nbObjects = len(objectList)
# if result == 0 :
#     for i in range(nbObjects):
#         print(i+1, ') ', objectList[i])
# else:
#     print('Error=>', result, " : ", errString)

result,errstring = xps.GroupInitialize('Group1','')
if result == 0 :
    print('group initialize successful')
else:
    print('group initialize fail')

result,errstring = xps.GroupHomeSearch('Group1','')
xps.GroupMotionEnable('Group1','')
# arr = array.array('d',[(x+1)/100 for x in range(0,99)])
arr = array.array('d',[0.01])
#
for i in range(0,500):
    xps.GroupMoveRelative('Group1',arr,1,'')
xps.CloseInstrument()


