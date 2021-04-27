import pandas as pd


XA = 0
YA = 0
XB = 0
YB = 0
XC = 0
YC = 0

data = pd.read_excel('list.xlsx', sheet_name='lab')

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