from scipy.optimize import curve_fit
import pandas as pd
import numpy as np

## 读取 T-P-G 数据
# data = pd.read_excel(r'D:\Desk\nonlinerFitData\Al-Ti-V-Omega_20211126\VV2-1400-2200K.xlsx')   ## 绝对路径, 指定数据表的文件路径
data = pd.read_excel(r'./VV2-1400-2200K.xlsx')      ## 相对路径, 数据表格在当前目录下

## 定义拟合函数的表达式, xdata 为自变量数据, 这里 x0 是表格中的第一列 温度数据, x1 是表格的第二列 压力数据
def func(xdata,a,b,c,d,e,f):  
    p = xdata[1]                                     ## 注意 p,t 取值的列号
    t = xdata[0]
    res = a*t + b*p + c*t**2 + d*p**2 + e*p*t + f    ## 自定义函数时, 需要注意 x 的取值范围, 如: 表达式中有 lnx时, x 取 0 会报错
    return np.array(res).ravel()

## 数据预处理: 从表格提取的数据为 DataFrame 格式, 需要转换成 np 的数组格式进行运算
xdata = data.iloc[:,0:2]
ydata = data.iloc[:,2:3]

x1 = np.array(data.iloc[:,0:1]).reshape(1, -1)
x2 = np.array(data.iloc[:,1:2]).reshape(1, -1)

xArr = np.append(x1, x2, axis=0)
yArr = np.array(ydata).ravel()

## 数据拟合
## popt: 参数的最佳值，残差平方和最小化。
## popt: 估计协方差, 对角线提供参数估计的方差。
## 详细参数参考 scipy.optimize.curve_fit 文档

popt, pcov = curve_fit(func, xArr, yArr)   

## 输出拟合结果
dis = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

## 系数
for index, val in dis.items():
    print(f'{index} : {popt[val]:+.4e}')

## 公式
print(f'G={popt[0]:+.4e}*T{popt[1]:+.4e}*P{popt[2]:+.4e}*T**2{popt[3]:+.4e}*P**2{popt[4]:+.4e}*P*T{popt[5]:+.4e}')

