import csv
import matplotlib.pyplot as plt

# 파일 열기
f1 = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
f2 = open('2022_Dajeon_Temp.csv','r',encoding='cp949')
f3 = open('2022_Busan_Temp.csv','r',encoding='cp949')
f4 = open('2022_Jeju_Temp.csv','r',encoding='cp949')
f5 = open('2022_Korea_Temp.csv','r',encoding='cp949')

data1 = csv.reader(f1, delimiter=',')
data2 = csv.reader(f2,delimiter=',')
data3 = csv.reader(f3,delimiter=',')
data4 = csv.reader(f4,delimiter=',')
data5 = csv.reader(f5,delimiter=',')
header = next(data1)
header = next(data2)
header = next(data3)
header = next(data4)
header = next(data5)

x1 = []
x2=[]
x3=[]
x4=[]
x5=[]
for row in data1:
    x1.append(float(row[2]))
for row in data2:
    x2.append(float(row[2]))
for row in data3:
    x3.append(float(row[2]))
for row in data4:
    x4.append(float(row[2]))
for row in data5:
    x5.append(float(row[2]))

# 월별 라벨 생성
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

plt.plot(labels, x1,label='Seoul')
plt.plot(labels, x2,label='Dajeon')
plt.plot(labels, x3, label='Busan')
plt.plot(labels, x4, label='Jeju')
plt.plot(labels, x5, label='korea')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperature 2022')
plt.legend()

plt.show()

# 파일 닫기
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
