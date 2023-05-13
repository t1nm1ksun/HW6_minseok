import csv
import matplotlib.pyplot as plt
import numpy as np

f22 = open('Jeju_2022.csv', 'r', encoding='cp949')
f21 = open('Jeju_2021.csv', 'r', encoding='cp949')
f20 = open('Jeju_2020.csv', 'r', encoding='cp949')
f19 = open('Jeju_2019.csv', 'r', encoding='cp949')

data22 = csv.reader(f22, delimiter=',')
next(data22)  # 헤더 행 건너뛰기

data21 = csv.reader(f21, delimiter=',')
next(data21)  # 헤더 행 건너뛰기

data20 = csv.reader(f20, delimiter=',')
next(data20)  # 헤더 행 건너뛰기

data19 = csv.reader(f19, delimiter=',')
next(data19)  # 헤더 행 건너뛰기

man22 = 0
woman22 = 0
man21 = 0
woman21 = 0
man20 = 0
woman20 = 0
man19 = 0
woman19 = 0

for row in data22:
    man22 += int(row[3])
    woman22 += int(row[4])
for row in data21:
    man21 += int(row[3])
    woman21 += int(row[4])
for row in data20:
    man20 += int(row[3])
    woman20 += int(row[4])
for row in data19:
    man19 += int(row[3])
    woman19 += int(row[4])

years = ['Man   Woman\n2019', 'Man   Woman\n2020', 'Man   Woman\n2021', 'Man   Woman\n2022']
men = [man19, man20, man21, man22]
women = [woman19, woman20, woman21, woman22]

bar_width = 0.35
index = np.arange(len(years))

# 막대 그래프 그리기
plt.bar(index, men, bar_width, label='MAN', color='skyblue')
plt.bar(index + bar_width, women, bar_width, label='WOMAN', color='pink')

plt.xlabel('YEAR')
plt.ylabel('POPULATION')
plt.title('POPULATION IN JEJU')
plt.xticks(index + bar_width / 2, years)
plt.legend()
plt.show()
