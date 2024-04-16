import matplotlib.pyplot as plt
import csv

x1 = []
x2 = []
x3 = []
x4 = []

with open('A2C_3.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x1.append(float(row[1]) / 41)
        x2.append(float(row[2]))

plt.plot(x1, x2, color='g', linestyle='dotted',
         marker='o', label="Episode Vs Reward")


plt.xticks(rotation=0)
plt.xlabel('Episodes', fontsize=20)
plt.ylabel('Rewards', fontsize=20)

plt.legend(fontsize=20)
plt.grid()


plt.tight_layout()
plt.show()
