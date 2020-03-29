import numpy as np
import matplotlib.pyplot as plt
import statistics
 
#グラフの点数
N=100
 
#x,y座標の作製
x=np.array(range(0, N, 1))
y=np.array(list(1*i + 10*np.random.randn() for i in x))
 
#外れ値の導入
#y[95]=1000
 
#Passing-Bablock法
def Passing_Bablok(x,y):
    ng_count=0
    PB_list=[]
 
    for i in range(N):
        for j in range(N):
            if i < j:
                slope=(y[i]-y[j])/(x[i]-x[j])
                PB_list.append(slope)
                if slope<-1:
                    ng_count+=1
            else :
                pass
 
    shift=ng_count
    PB_list.sort()
 
    print(shift)
    del PB_list[:shift]
 
#信頼区間の計算(今は95%信頼区間)
    C_alpha=(1-0.95/2)*np.sqrt(N*(N-1)*(2*N+5)/18)
    N_PB_list=len(PB_list)
    M1=int(round((N_PB_list-C_alpha)/2))
    M2=N_PB_list-M1+1
     
#傾き(中央値)、上下信頼区間の出力    
    PB_coef=statistics.median(PB_list)
    PB_upper=PB_list[M2]
    PB_lower=PB_list[M1]
 
    return PB_coef,PB_upper,PB_lower
 
#最小二乗法
def least_square(x,y):
    x_ave=np.average(x)
    y_ave=np.average(y)
    ls_coef=np.dot((x-x_ave),(y-y_ave))/ ((x-x_ave)**2).sum()
    return ls_coef
 
#最小二乗法とPB法の傾き(と上下信頼区間)
a=least_square(x,y)
a_PB, a_PB_upper, a_PB_lower=Passing_Bablok(x,y)
 
print(a)
print(a_PB, a_PB_upper, a_PB_lower)
 
# 最小二乗法とPB法の計算結果のグラフ化
plt.scatter(x, y, color="k")
plt.plot([0, x.max()], [0, a*x.max()],color="b",label="least square")
plt.plot([0, x.max()], [0, a*x.max()],color="b",label="slope is " + str(a))
plt.plot([0, x.max()], [0, a_PB*x.max()],color="r", label="Passing-Bablok")
plt.plot([0, x.max()], [0, a_PB*x.max()],color="r", label="slope is " + str(a_PB))
plt.title("y=x fitting")
plt.legend()
plt.show()