import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#import numpy as np



'''
柱状图
'''

length_pred_distribute = [[13, 29, 48, 70, 61, 73, 67, 57, 72, 63, 50, 46, 52, 42, 45, 32, 31, 31, 34, 22, 23, 17, 18, 14, 16, 13, 10, 10, 16, 8, 6, 6, 4, 2, 5, 4, 4, 2, 4, 2, 1, 6, 1, 0, 3, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                          [13, 43, 82, 84, 84, 89, 77, 59, 64, 50, 42, 54, 58, 41, 39, 23, 23, 21, 26, 18, 16, 17, 14, 12, 14, 12, 9, 3, 10, 5, 2, 5, 4, 4, 1, 5, 3, 4, 2, 3, 2, 0, 0, 1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                          [18, 83, 129, 139, 103, 102, 93, 79, 79, 37, 57, 41, 29, 27, 27, 17, 17, 9, 8, 9, 8, 7, 0, 5, 3, 1, 4, 3, 2, 4, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
distance_distribute = [[0, 0, 0, 9, 25, 64, 66, 62, 44, 45, 45, 50, 41, 63, 45, 51, 50, 40, 35, 35, 25, 37, 18, 30, 23, 24, 26, 19, 26, 13, 11, 8, 5, 10, 9, 8, 5, 6, 3, 8, 3, 2, 10, 3, 4, 5, 0, 5, 2, 0, 4, 3, 3, 3, 0, 0, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                       [0, 9, 25, 64, 66, 60, 46, 43, 43, 48, 45, 56, 44, 44, 57, 43, 35, 31, 25, 37, 25, 19, 27, 23, 34, 19, 21, 18, 11, 10, 12, 8, 11, 4, 10, 7, 7, 6, 7, 0, 1, 11, 4, 1, 5, 5, 2, 2, 2, 1, 1, 2, 1, 0, 1, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                       [0, 9, 25, 64, 66, 60, 46, 43, 43, 48, 45, 56, 44, 44, 57, 43, 35, 31, 25, 37, 25, 19, 27, 23, 34, 19, 21, 18, 11, 10, 12, 8, 11, 4, 10, 7, 7, 6, 7, 0, 1, 11, 4, 1, 5, 5, 2, 2, 2, 1, 1, 2, 1, 0, 1, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
actual_distribute = [[0, 0, 0, 0, 1, 89, 60, 58, 83, 55, 30, 63, 37, 49, 42, 48, 31, 42, 24, 42, 29, 28, 27, 28, 24, 24, 20, 23, 23, 16, 11, 10, 9, 18, 10, 8, 4, 6, 4, 5, 7, 5, 9, 2, 5, 6, 0, 4, 1, 0, 5, 1, 3, 2, 0, 1, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 1, 89, 60, 58, 83, 55, 30, 63, 37, 49, 42, 48, 31, 42, 24, 42, 29, 28, 27, 28, 24, 24, 20, 23, 23, 16, 11, 10, 9, 18, 10, 8, 4, 6, 4, 5, 7, 5, 9, 2, 5, 6, 0, 4, 1, 0, 5, 1, 3, 2, 0, 1, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                     [0, 0, 13, 154, 90, 46, 115, 67, 43, 87, 47, 41, 66, 60, 42, 39, 29, 26, 38, 24, 17, 15, 11, 13, 10, 8, 5, 5, 1, 5, 4, 3, 2, 7, 2, 3, 2, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

label = [x for x in range (100)]
label_space = [x for x in range (-10,990,10)]

for n,typ in enumerate(['full','removed','symbol']):
    ax = plt.gca()
    tick_spacing = 20
    plt.title('Predicted '+typ)
    plt.xlabel('Length')
    plt.ylabel('Count')
    plt.bar(label,length_pred_distribute[n],tick_label = label_space)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()
#    plt.savefig('./stats_pics/Predicted '+typ+'.png')
for n,typ in enumerate(['full','removed','symbol']):
    ax = plt.gca()
    tick_spacing = 20
    plt.bar(label,actual_distribute[n],tick_label = label_space)
    plt.title('Actual length '+typ)
    plt.xlabel('Length')
    plt.ylabel('Count')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()
#    plt.savefig('./stats_pics/Actual '+typ+'.png')
for n,typ in enumerate(['full','removed','symbol']):
    ax = plt.gca()
    tick_spacing = 20
    plt.bar(label,distance_distribute[n],tick_label = label_space)
    plt.title('Leveshstein distance '+typ)
    plt.xlabel('Length')
    plt.ylabel('Count')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()
#    plt.savefig('./stats_pics/Leveshstein distance '+typ+'.png')