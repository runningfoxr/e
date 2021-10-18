import csv
from collections import Counter

with open('height-weight.csv',newline='') as f:
    read=csv.reader(f)
    filedata=list(read)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    n=filedata[i][1]
    newdata.append(float(n))

N=len(newdata)
total=0
for x in newdata:
    total+=x

mean=total/N
print("mean"+str(mean))

newdata.sort()
if N % 2==0:
    median1=float(newdata[N//2])
    median2=float(newdata[N//2 -1])
    median=(median1 + median2)//2

else:
    median=float(newdata[N//2])

print("median"+str(median))

data=Counter(newdata)
mode={
    "50-60":0,
    "60-70":0,
    "70,80":0,
}

for height, occurrence in data.items():
    if 50<float(height)<60:
        mode["50-60"]+=occurrence
    elif 60<float(height)<70:
        mode["60-70"]+=occurrence
    elif 70<float(height)<80:
        mode["70-80"]+=occurrence

print(occurrence)