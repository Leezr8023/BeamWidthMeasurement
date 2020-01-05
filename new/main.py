import SR830
import xpsclass
#import Algorithm
import array
import numpy as np
#from data import data1,data2
def startmeasure():
    sr = SR830.SR830()
    xps = xpsclass.MyXPS()
    sr.setIT(i=19)  # or sr.setIT(i=11)
    sr.setSens(i=24)  # or sr.setSens(i=17)

    data = np.zeros(shape=(1000, 2))  # 也可以三列+位移
    #GroupMoveRelative移动的参数只接受double型，python中不能直接定义double
    for j in range(2):
        for i in range(0, 100):
            xps.measureMove(0.01 * i)
            #print("done")
            postion = xps.GetPosition()
            #print(postion)
            sum = 0.0;
            for k in range(6):
                res = sr.getOut(3)
                sum = sum + res
            #print("X out : {0}".format(res))
            # print(i)
            # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
            global data1
            global data2
            data1.append(sum/6)
            data2.append(postion)

        xps.measureMove(10)

        for i in range(100, 200):
            xps.measureMove(10 + i * 0.01)
            postion = xps.GetPosition()
            sum = 0.0;
            for k in range(6):
                res = sr.getOut(3)
                print(res)
                sum = sum + res
            #print("X out : {0}".format(res))
            # print(i)
            # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
            print(sum/6)
            print("")
            global data1
            global data2
            data1.append(sum/6)
            data2.append(postion)
    sr.close()
    xps.close()
    num = np.loadtxt('count.txt')
    title = "data/data{0}.txt".format(num)
    np.savetxt(title, [data1,data2], fmt='%f', delimiter='\t')
    np.savetxt("count.txt",[num+1])
    # sr = SR830.SR830()
    # xps = xpsclass.MyXPS()
    # sr.setIT(i=19)#or sr.setIT(i=11)
    # sr.setSens(i=24)#or sr.setSens(i=17)
    #
    # data = np.zeros(shape = (1000,2))#也可以三列+位移
    # # GroupMoveRelative移动的参数只接受double型，python中不能直接定义double
    # for i in range(0, 100):
    #     xps.measureMove(0.01*i)
    #     print("done")
    #     res = sr.getOut(3)
    #     print("X out : {0}".format(res))
    #     # print(i)
    #     # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
    #     data[i,0] = res
    #     data[i + 500*j, 1] = postion
    #
    # xps.measureMove(10)
    #
    # for i in range(100, 200):
    #     xps.measureMove(10 + i*0.01)
    #     res = sr.getOut(3)
    #     print("X out : {0}".format(res))
    #     # print(i)
    #     # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
    #     data[i+500,0] = res
    #     data[i + 500*j, 1] = postion
    # sr.close()
    # xps.close()
    # num = np.loadtxt('count.txt')
    # title = "data/data{0}.txt".format(num)
    # np.savetxt(title, data, fmt='%f', delimiter='\t')
    # np.savetxt("count.txt",[num+1])


if __name__=='__main__':
    sr = SR830.SR830()
    xps = xpsclass.MyXPS()
    sr.setIT(i=19)  # or sr.setIT(i=11)
    sr.setSens(i=24)  # or sr.setSens(i=17)

    data = np.zeros(shape=(1000, 2))  # 也可以三列+位移
    #GroupMoveRelative移动的参数只接受double型，python中不能直接定义double
    for j in range(2):
        for i in range(0, 100):
            xps.measureMove(0.01 * i)
            #print("done")
            postion = xps.GetPosition()
            #print(postion)
            sum = 0.0;
            for k in range(6):
                res = sr.getOut(3)
                sum = sum + res
            #print("X out : {0}".format(res))
            # print(i)
            # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
            data[i + 500*j, 0] = sum/6
            data[i + 500*j, 1] = postion

        xps.measureMove(10)

        for i in range(100, 200):
            xps.measureMove(10 + i * 0.01)
            postion = xps.GetPosition()
            sum = 0.0;
            for k in range(6):
                res = sr.getOut(3)
                print(res)
                sum = sum + res
            #print("X out : {0}".format(res))
            # print(i)
            # print("Signal RMS: {0}V with phase {1} deg".format(res[0],int(res[1])))
            print(sum/6)
            print("")
            data[i + 500*j, 0] = sum/6
            data[i + 500*j, 1] = postion
    sr.close()
    xps.close()
    num = np.loadtxt('count.txt')
    title = "data/data{0}.txt".format(num)
    np.savetxt(title, data, fmt='%f', delimiter='\t')
    np.savetxt("count.txt",[num+1])


