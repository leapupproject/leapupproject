# save coordinate of hand to the list and vizualization on the chart

import json
import matplotlib.pyplot as plt

x = []
y = []
z = []
time = []

with open('example.json') as f:
    data = json.load(f)

for number_of_second in range(1, len(data['data'])):
    time.append(number_of_second)

for second in data['data']:
    try:
        if len(second['hands']) > 0:
            # print(second['hands'][0]['palmPosition'][0])
            # print(second['hands'][0]['palmPosition'][1])
            # print(second['hands'][0]['palmPosition'][2])
            x.append(second['hands'][0]['palmPosition'][0])
            y.append(second['hands'][0]['palmPosition'][1])
            z.append(second['hands'][0]['palmPosition'][2])
    except KeyError:
        continue

plt.plot(time, x, 'g')
plt.plot(time, y, 'b')
plt.plot(time, z, 'r')

plt.show()
