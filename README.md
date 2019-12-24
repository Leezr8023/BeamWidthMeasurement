# BeamWidthMeasurement
正常是运行interface.py文件，
出现界面两个按钮一个文本框，
点击相应的按钮通过槽函数调用锁相和位移 以及 算法。
现在槽函数触发好像有点问题，
我给改成了分别print提示语句去debug。
只要分别调用相应的函数就行。
另外，main.py里的startmeasure函数和algorithm.py中的qtoutput单独调用都是可以运行的

包：pyvisa，numpy,scikit-learn,pyqt5,
