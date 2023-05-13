import random
import matplotlib.pyplot as plt
import csv

result100 = []
result1000 = []
result10000 = []
result100000 = []

for i in range(100):
    random_number = random.randint(1, 6)
    result100.append(random_number)
for i in range(1000):
    random_number = random.randint(1, 6)
    result1000.append(random_number)
for i in range(10000):
    random_number = random.randint(1, 6)
    result10000.append(random_number)
for i in range(100000):
    random_number = random.randint(1, 6)
    result100000.append(random_number)


plt.figure(figsize=(8, 6))

plt.subplot(2, 2, 1)
plt.hist(result100, bins=6, range=(0.5, 6.5) ,edgecolor='black')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram - 100')

plt.subplot(2, 2, 2)
plt.hist(result1000, bins=6, range=(0.5, 6.5), edgecolor='black')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram - 1000')

plt.subplot(2, 2, 3)
plt.hist(result10000, bins=6, range=(0.5, 6.5), edgecolor='black')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram - 10000')

plt.subplot(2, 2, 4)
plt.hist(result100000, bins=6, range=(0.5, 6.5), edgecolor='black')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram - 100000')

plt.tight_layout()
plt.show()


with open('result_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sample', 'Data'])
    for i, result in enumerate([result100, result1000, result10000, result100000], start=1):
        for data in result:
            writer.writerow([f'Sample {i}', data])

csvfile.close()

