from django.shortcuts import render
arr=[]
import numpy as np
import matplotlib.pyplot as plt
numof=int(0.4*50)
first=np.random.randint(00,50,numof)
last=np.random.randint(00,59,numof)
#print(first)
#print(last)

string=''
for i in range(0,numof):

    if(len(str(last[i]))==1):
        string='.0'+str(last[i])
        #print(string)
    else:
        string='.'+str(last[i])
    arr.append(float(str(first[i])+string))
#print('found at points:')
#print(np.sort(arr))
arr1=np.ones(numof,int)
#print(arr1)
#plt.scatter(arr,arr1)
#plt.show()

count =0
#for i in arr:
#    if(i>=int(0.2*numof)):
#        for j in range(i,len(arr):
#            if(j<=i+int(0.2*numof)
from sklearn.neighbors import KernelDensity

#kde_skl = KernelDensity(bandwidth=0.5)
    #kde_skl.fit(arr[:, np.newaxis])
    # score_samples() returns the log-likelihood of the samples
    #log_pdf = kde_skl.score_samples(x_grid[:, np.newaxis])
          
from scipy.stats import kde
import matplotlib.pyplot as plt     
density = kde.gaussian_kde(arr) # x: list of price
xgrid = np.linspace(np.array(arr).min(), np.array(arr).max(),len(arr))  
#print(xgrid)
#print(density)
darr=[]
for i in xgrid:
    darr.append(density(i)[0])
#print(darr) 
denindex=darr.index(np.array(darr).max())
xgridindex=xgrid[darr.index(np.array(darr).max())]
#print(denindex)
#print(xgridindex)
answer='0'
if(xgridindex+int(0.10*50)>=50):
    print("vals=${xgridindex} to ${50}")
    answer="vals=${xgridindex} to ${50}"
if(xgridindex-int(0.10*50)<=0):
    print("vals=${0} to ${xgridindex}")
    answer="vals=${0} to ${xgridindex}"
if(xgridindex>int(0.10*50) and xgridindex<50-int(0.10*50)):
    temp=xgridindex-int(0.10*50)
    temp1=xgridindex+int(0.10*50)
    print("vals={} to {}".format(temp,temp1))
    answer="vals={} to {}".format(temp,temp1)
    

#plt.style.use('dark_background')
#plt.scatter(arr,arr1*0)
#plt.plot(xgrid, density(xgrid))
#plt.show()
answer=answer+' values were found at the following timestamps '+str(np.sort(arr))
print(answer)
#python manage.py runserver 127.0.0.1:8001


def button(request):
    return(render(request,'home.html'))
def output(request):
    print("heres data")

    plt.style.use('dark_background')
    plt.scatter(arr,arr1*0)
    plt.plot(xgrid, density(xgrid))
    plt.show()
    plt.savefig('de.png')






    return(render(request,'home.html',{'data':answer}))