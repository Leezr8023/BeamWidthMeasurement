import numpy as np
from sklearn.linear_model import LassoCV, ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import random

def TestDataGenerate():#测试用，数据是由matlab生成的
    file = np.loadtxt('M_tab3.0.txt',dtype=np.float32,delimiter='\t')
    file_new = np.zeros(shape = (200,3))
    np.random.seed(0)
    for i in range(0,200):
        file_new[i] = file[i*100+random.randint(-75,85)]
    return np.linspace(-1,1,200),file_new[...,2]

def DataGet1():#返回可以有两种方式，一种只返回锁相的数据，位移量均匀生成
    file = np.loadtxt('data.txt',dtype=np.float32,delimiter='\t')
    return np.linspace(-1,1,200),file[...,2]

def DataGet2():#返回锁相和位移
    file = np.loadtxt('data.txt', dtype=np.float32, delimiter='\t')
    return file[...,0],file[...,1]

def DatapreprocessY(y):
    for i in len(y)-2:
        if(abs(y[i]-y[i+1]) < 0.000001):  #判别的系数需要根据实际测得数据一致
            y[i] = -1   #标记数据
    y_new = np.setdiff1d(y,[-1])
    return y_new

if __name__=='__main__':
    [x,y] = TestDataGenerate()
    # [x,y] = DataGet1()
    # [x,y] = DataGet2()
    N = 6       #6次幂
    x.shape = -1,1
    y.shape = -1,1

    # 两个模型LassoCV，ElasticNetCV，分别运行
    models = [Pipeline([('poly', PolynomialFeatures()),
                        ('linear', LassoCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))]),
              Pipeline([('poly', PolynomialFeatures()),
                        ('linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50),l1_ratio=[.1, .5, .7, .9, .95, .99, 1],fit_intercept=False))])]
    for t in range(2):
        model = models[t]
        model.set_params(poly__degree=N)
        model.fit(x, y.ravel())
        lin = model.get_params('linear')['linear']
        print("lin.coef_.ravel():\n", lin.coef_.ravel())#系数输出

        x_hat = np.linspace(x.min(), x.max(), num=500)
        x_hat.shape = -1, 1
        y_hat = model.predict(x_hat)
        M_max = max(y_hat)
        M_min = min(y_hat)
        r0 = (M_max - M_min)/2
        hfwm_tuble = np.where(abs(y_hat-r0)<0.002)#判断相等，0.001时LassoCV无结果，ElasticNetCV正常

        #半高宽计算
        sum = 0
        a_array = hfwm_tuble[0]
        for i in range(0,int(len(a_array))):
            sum = sum + abs(a_array[i] - a_array[len(a_array)-1-i])
        result = sum/(len(a_array)*500+1)
        print(result)

# def qtoutput():
#     [x,y] = TestDataGenerate()
#     # [x,y] = DataGet1()
#     # [x,y] = DataGet2()
#     N = 6       #6次幂
#     x.shape = -1,1
#     y.shape = -1,1
#
#     # 两个模型LassoCV，ElasticNetCV，分别运行
#     models = [Pipeline([('poly', PolynomialFeatures()),
#                         ('linear', LassoCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))]),
#               Pipeline([('poly', PolynomialFeatures()),
#                         ('linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50),l1_ratio=[.1, .5, .7, .9, .95, .99, 1],fit_intercept=False))])]
#     #for t in range(2):
#     model = models[1]
#     model.set_params(poly__degree=N)
#     model.fit(x, y.ravel())
#     lin = model.get_params('linear')['linear']
#     print("lin.coef_.ravel():\n", lin.coef_.ravel())#系数输出
#
#     x_hat = np.linspace(x.min(), x.max(), num=500)
#     x_hat.shape = -1, 1
#     y_hat = model.predict(x_hat)
#     M_max = max(y_hat)
#     M_min = min(y_hat)
#     r0 = (M_max - M_min)/2
#     hfwm_tuble = np.where(abs(y_hat-r0)<0.002)#判断相等，0.001时LassoCV无结果，ElasticNetCV正常
#
#     #半高宽计算
#     sum = 0
#     a_array = hfwm_tuble[0]
#     for i in range(0,int(len(a_array))):
#         sum = sum + abs(a_array[i] - a_array[len(a_array)-1-i])
#     result = sum/(len(a_array)*500+1)
#     print(result)
# return result
