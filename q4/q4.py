import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

f = open('202303.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
next(data) 

dicIn = {}
dicOut = {}
dicAll = {}

for row in data:
    if row[2] in dicIn:
        dicIn[row[2]] += int(row[9]) + int(row[11])
        dicOut[row[2]] += int(row[10]) + int(row[12])
        dicAll[row[2]] += int(row[9]) + int(row[11]) + int(row[10]) + int(row[12])
    else:
        dicIn[row[2]] = int(row[9]) + int(row[11])
        dicOut[row[2]] = int(row[10]) + int(row[12])
        dicAll[row[2]] = int(row[9]) + int(row[11]) + int(row[10]) + int(row[12])

# 값에 따라 딕셔너리들 정렬
sorted_dicIn = sorted(dicIn.items(), key=lambda x: x[1], reverse=True)
sorted_dicOut = sorted(dicOut.items(), key=lambda x: x[1], reverse=True)
sorted_dicAll = sorted(dicAll.items(), key=lambda x: x[1], reverse=True)

# 상위 30개 데이터 추출
top30_dicIn = dict(sorted_dicIn[:30])
top30_dicOut = dict(sorted_dicOut[:30])
top30_dicAll = dict(sorted_dicAll[:30])

# 막대 그래프로 표현
plt.figure(figsize=(22, 6))
plt.subplot(1, 3, 1)
plt.bar(top30_dicIn.keys(), top30_dicIn.values())
plt.xticks(rotation=90)
plt.xlabel('역명')
plt.ylabel('승차 인원')
plt.title('상위 30개 역의 승차 인원')

plt.subplot(1, 3, 2)
plt.bar(top30_dicOut.keys(), top30_dicOut.values())
plt.xticks(rotation=90)
plt.xlabel('역명')
plt.ylabel('하차 인원')
plt.title('상위 30개 역의 하차 인원')

plt.subplot(1, 3, 3)
plt.bar(top30_dicAll.keys(), top30_dicAll.values())
plt.xticks(rotation=90)
plt.xlabel('역명')
plt.ylabel('전체 인원')
plt.title('상위 30개 역의 전체 인원')

plt.tight_layout()
plt.show()
