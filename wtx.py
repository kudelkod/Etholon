import math
import func as m

import matplotlib.pyplot as plt


def ex():
    global a, b, c
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    for n in range(len(m.x_coords)):
        if m.categories[n] != "A" and m.categories[n] != "B" and m.categories[n] != "C":
            a = math.sqrt((math.pow((m.XA - m.x_coords[n]), 2)) + (math.pow((m.YA - m.y_coords[n]), 2)))
            b = math.sqrt((math.pow((m.XB - m.x_coords[n]), 2)) + (math.pow((m.YB - m.y_coords[n]), 2)))
            c = math.sqrt((math.pow((m.XC - m.x_coords[n]), 2)) + (math.pow((m.YC - m.y_coords[n]), 2)))
            if a < b and a < c:
                m.categories[n] = "A"
                plt.plot([m.x_coords[n], m.XA], [m.y_coords[n], m.YA], 'blue')
                plt.plot([m.x_coords[n], m.XB], [m.y_coords[n], m.YB], 'red')
                plt.plot([m.x_coords[n], m.XC], [m.y_coords[n], m.YC], 'green')
            if b < a and b < c:
                m.categories[n] = "B"
                plt.plot([m.x_coords[n], m.XA], [m.y_coords[n], m.YA], 'blue')
                plt.plot([m.x_coords[n], m.XB], [m.y_coords[n], m.YB], 'red')
                plt.plot([m.x_coords[n], m.XC], [m.y_coords[n], m.YC], 'green')
            elif c < a and c < b:
                m.categories[n] = "C"
                plt.plot([m.x_coords[n], m.XA], [m.y_coords[n], m.YA], 'blue')
                plt.plot([m.x_coords[n], m.XB], [m.y_coords[n], m.YB], 'red')
                plt.plot([m.x_coords[n], m.XC], [m.y_coords[n], m.YC], 'green')

    for n in range(len(m.x_coords)):
        plt.scatter(m.x_coords[n], m.y_coords[n], c=m.colors[m.categories[n]])

    plt.scatter(m.XA, m.YA, c='blue', linewidths=15)
    plt.scatter(m.XB, m.YB, c='red', linewidths=15)
    plt.scatter(m.XC, m.YC, c='green', linewidths=15)

    plt.show()
