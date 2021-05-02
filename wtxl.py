import math
import func as m
import pandas as pd

import matplotlib.pyplot as plt


def no_ex():
    global info1, info2, info3, info4, et, rast_et
    new_Ny = float(input('Enter Ny: '))
    new_Nk = float(input('Enter Nk: '))

    print("Ny, Nk: ", [new_Ny, new_Nk])

    rast_A = math.sqrt((math.pow((m.XA - new_Ny), 2)) + (math.pow((m.YA - new_Nk), 2)))
    rast_B = math.sqrt((math.pow((m.XB - new_Ny), 2)) + (math.pow((m.YB - new_Nk), 2)))
    rast_C = math.sqrt((math.pow((m.XC - new_Ny), 2)) + (math.pow((m.YC - new_Nk), 2)))

    print("First size: ", rast_A, "\n""Second size: ", rast_B, "\n""Third size: ", rast_C)

    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    if rast_A < rast_B and rast_A < rast_C:
        et = 'A'
        m.categories.append("A")
        m.y_coords.append(new_Nk)
        m.x_coords.append(new_Ny)
        plt.plot([new_Ny, m.XA], [new_Nk, m.YA], 'blue')
        plt.plot([new_Ny, m.XB], [new_Nk, m.YB], 'red')
        plt.plot([new_Ny, m.XC], [new_Nk, m.YC], 'green')
    elif rast_B < rast_A and rast_B < rast_C:
        et = 'B'
        m.categories.append("B")
        m.y_coords.append(new_Nk)
        m.x_coords.append(new_Ny)
        plt.plot([new_Ny, m.XA], [new_Nk, m.YA], 'blue')
        plt.plot([new_Ny, m.XB], [new_Nk, m.YB], 'red')
        plt.plot([new_Ny, m.XC], [new_Nk, m.YC], 'green')
    elif rast_C < rast_A and rast_C < rast_B:
        et = 'C'
        m.categories.append("C")
        m.y_coords.append(new_Nk)
        m.x_coords.append(new_Ny)
        plt.plot([new_Ny, m.XA], [new_Nk, m.YA], 'blue')
        plt.plot([new_Ny, m.XB], [new_Nk, m.YB], 'red')
        plt.plot([new_Ny, m.XC], [new_Nk, m.YC], 'green')


    for n in range(len(m.x_coords)):
        plt.scatter(m.x_coords[n], m.y_coords[n], c=m.colors[m.categories[n]])

    plt.scatter(m.XA, m.YA, c='blue', linewidths=15)
    plt.scatter(m.XB, m.YB, c='red', linewidths=15)
    plt.scatter(m.XC, m.YC, c='green', linewidths=15)

    plt.show()

    info = ['Distance to A: %f' % rast_A, 'Distance to B: %f' % rast_B, 'Distance to C: %f' % rast_C, 'last class: {0}'.format(et)]
    # info_et = ['last et coord: (Ny: %f, Nk: %f)' % new_Ny % new_Nk, 'last et: %s' % et]

    d1 = m.x_coords
    d2 = m.y_coords
    d3 = m.categories
    i = info
    # ie = info_et

    s1 = pd.Series(d1, name='Ny')
    s2 = pd.Series(d2, name='Nk')
    s3 = pd.Series(d3, name='class')
    s4 = pd.Series(i, name='info')
    # s5 = pd.Series(ie, name='info et')
    df = pd.concat([s1, s2, s3, s4], axis=1)
    df.to_excel('list.xlsx', index=False)
