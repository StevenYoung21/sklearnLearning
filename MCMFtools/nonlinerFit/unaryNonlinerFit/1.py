from scipy.optimize import curve_fit
import pandas as pd
import numpy as np


# data = pd.read_excel(r'D:\Desk\nonlinerFitData\Cu-Fcc.xlsx') 
data = pd.read_excel(r'.\Cu-Fcc.xlsx')

# np.seterr(divide='ignore', invalid='ignore')

def func(x,a,b,c,d,e,f):
    res = a + b*x*np.log(x) + c*x**2 + d*x**3 + e*x**(-1) + f*x
    return res

xdata = data.iloc[:,0:1]
ydata = data.iloc[:,1:2]


xArr = np.array(xdata).ravel()
yArr = np.array(ydata).ravel()

popt, pcov = curve_fit(func, xArr, yArr)

## 输出拟合结果
dis = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

## 系数
for index, val in dis.items():
    print(f'{index} : {popt[val]:+.4e}')

## 公式
print(f'G={popt[0]:+.4e}{popt[1]:+.4e}*T*ln(T){popt[2]:+.4e}*T**3{popt[3]:+.4e}*T**2{popt[4]:+.4e}*T**(-1){popt[5]:+.4e}*T')


