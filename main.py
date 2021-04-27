import math

import matplotlib.pyplot as plt
import pandas as pd

XA = 0
YA = 0
XB = 0
YB = 0
XC = 0
YC = 0

data = pd.read_excel('list.xlsx', sheet_name='lab')

new_Ny = float(input('Enter Ny: '))
new_Nk = float(input('Enter Nk: '))

print("Ny, Nk: ", [new_Ny, new_Nk])

colors = {"A": "blue", "B": "red", "C": "green"}
x_coords = list(data['Ny'])
y_coords = list(data["Nk"])
categories = list(data['classes'])

for i in range(len(x_coords)):
    if categories[i] == "A":
        XA += x_coords[i] / categories.count("A")
        YA += y_coords[i] / categories.count("A")
    if categories[i] == "B":
        XB += x_coords[i] / categories.count("B")
        YB += y_coords[i] / categories.count("B")
    if categories[i] == "C":
        XC += x_coords[i] / categories.count("C")
        YC += y_coords[i] / categories.count("C")

print("Coord first et: ", [XA, YA], "\n""Coord second et:", [XB, YB], "\n""Coord third et:", [XC, YC])

rast_A = math.sqrt((math.pow((XA - new_Ny), 2)) + (math.pow((YA - new_Nk), 2)))
rast_B = math.sqrt((math.pow((XB - new_Ny), 2)) + (math.pow((YB - new_Nk), 2)))
rast_C = math.sqrt((math.pow((XC - new_Ny), 2)) + (math.pow((YC - new_Nk), 2)))

print("First size: ", rast_A, "\n""Second size: ", rast_B, "\n""Third size: ", rast_C)

plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

if rast_A < rast_B and rast_A < rast_C:
    categories.append("A")
    y_coords.append(new_Nk)
    x_coords.append(new_Ny)
    plt.plot([new_Ny, XA], [new_Nk, YA], 'blue')
    plt.plot([new_Ny, XB], [new_Nk, YB], 'red')
    plt.plot([new_Ny, XC], [new_Nk, YC], 'green')
elif rast_B < rast_A and rast_B < rast_C:
    categories.append("B")
    y_coords.append(new_Nk)
    x_coords.append(new_Ny)
    plt.plot([new_Ny, XA], [new_Nk, YA], 'blue')
    plt.plot([new_Ny, XB], [new_Nk, YB], 'red')
    plt.plot([new_Ny, XC], [new_Nk, YC], 'green')
elif rast_C < rast_A and rast_C < rast_B:
    categories.append("C")
    y_coords.append(new_Nk)
    x_coords.append(new_Ny)
    plt.plot([new_Ny, XA], [new_Nk, YA], 'blue')
    plt.plot([new_Ny, XB], [new_Nk, YB], 'red')
    plt.plot([new_Ny, XC], [new_Nk, YC], 'green')
else:
    categories.append("Unknown")
    y_coords.append(new_Nk)
    x_coords.append(new_Ny)

for i in range(len(x_coords)):
    plt.scatter(x_coords[i], y_coords[i], c=colors[categories[i]])

plt.scatter(XA, YA, c='blue', linewidths=15)
plt.scatter(XB, YB, c='red', linewidths=15)
plt.scatter(XC, YC, c='green', linewidths=15)

plt.show()
