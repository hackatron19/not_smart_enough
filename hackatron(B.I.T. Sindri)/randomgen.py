arr=[]
import numpy as np
import matplotlib.pyplot as plt
numof=int(0.4*50)
first=np.random.randint(00,50,numof)
last=np.random.randint(00,59,numof)
print(first)
print(last)

string=''
for i in range(0,numof):

    if(len(str(last[i]))==1):
        string='.0'+str(last[i])
        #print(string)
    else:
        string='.'+str(last[i])
    arr.append(float(str(first[i])+string))
print('found at points:')
print(np.sort(arr))
arr1=np.ones(numof,int)
print(arr1)
#plt.scatter(arr,arr1)
#plt.show()
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.2, min_samples=10).fit([arr])
print(db.labels_)
print(db.fit_predict([arr]))
count =0
for i in arr:
    if(i>=int(0.2*numof)):
        for j in range(i,i+int(0.2*numof)):
            print()

