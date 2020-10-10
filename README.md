# BeamWidthMeasurement
正常是运行interface.py文件，
出现界面两个按钮一个文本框，
点击相应的按钮通过槽函数调用锁相和位移 以及 算法。

algorithm.py中数据是从M_tab中读取的假数据，实际文本数据是由main.py中生成的data.txt文件改一下就可以了

main.py里的startmeasure函数和algorithm.py中的qtoutput单独调用都是可以运行的

包：pyvisa，numpy,scikit-learn,pyqt5,clr
