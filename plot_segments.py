


import numpy as np
import matplotlib.pyplot as plt
import csv

with open('tcp_segments.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list_RX = []
    list_TX = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #print(row[1])
            line_count += 1
            list_RX.append(row[1])
            list_TX.append(row[2])
    
    y_pos = np.arange(len(list_RX))
    

    
    list_RX = np.gradient(np.asarray(list_RX, dtype=np.int))
    list_TX = np.gradient(np.asarray(list_TX, dtype=np.int))
    X = np.arange(len(list_RX))

    plt.bar((X + 0.00)*5, list_RX, color = 'b', width = 0.25*5)
    plt.bar((X + 0.25)*5, list_TX, color = 'g', width = 0.25*5)

    
     
    # Custom Axis title
    plt.ylabel('TCP Segments. Blue: RX, Green: TX (#)', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')

    plt.xlabel('Time past beginning of capture (s)', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')

    plt.title('Alex McGinnis', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')
    
    plt.xticks(np.arange(0, len(list_RX)*5, step=5))

    plt.savefig('tcp_segments.png')
    #print(f'Processed {line_count} lines.')

    plt.show()






