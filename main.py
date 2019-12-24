import SR830
import xpsclass
#import Algorithm
import array
import numpy as np

def startmeasure():
    sr = SR830.SR830()
    xps = xpsclass.MyXPS()
    sr.setIT(i=6)#or sr.setIT(i=11)
    sr.setSens(i=8)#or sr.setSens(i=17)
    xps.measureMove()
    data = np.zeros(shape = (1000,2))#也可以三列+位移
    stepmove = array.array('d', [0.01])  # GroupMoveRelative移动的参数只接受double型，python中不能直接定义double
    for i in range(0, 500):
        xps.measureMove(stepmove)
        res = sr.getRTh()
        print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
        data[i,0] = res[0]
        data[i,1] = res[1]

    fastmove = array.array('d', [1])
    xps.measureMove(fastmove)

    moveback = array.array('d', [-0.01])
    for i in range(0, 500):
        xps.measureMove(stepmove)
        res = sr.getRTh()
        print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
        data[i+500,0] = res[0]
        data[i+500,1] = res[1]
    sr.close()
    xps.close()
    np.savetxt("data.txt", data, fmt='%f', delimiter='\t')


