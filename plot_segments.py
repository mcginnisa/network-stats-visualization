


import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import subprocess
import os.path
os.path.exists("guru99.txt")

def reject_outliers_2(data, m=2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / (mdev if mdev else 1.)
    data[s > m] = 0
    return data


#data_points = np.array([10, 10, 10, 17, 10, 10])
#print(reject_outliers_2(data_points))

while True:
    
    subprocess.run("/home/ssuee/5hw_11_11/get_segments.sh", shell=True)
    time.sleep(5)

    with open('tcp_segments.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        list_RX = []
        list_TX = []
        for row in csv_reader:
            line_count += 1
            list_RX.append(row[1])
            list_TX.append(row[2])
        
        y_pos = np.arange(len(list_RX))
        

        
        list_RX = reject_outliers_2(np.gradient(np.asarray(list_RX, dtype=np.int)))
        list_TX = reject_outliers_2(np.gradient(np.asarray(list_TX, dtype=np.int)))
        
        X = np.arange(len(list_RX))

        plt.bar((X + 0.00)*5, list_RX, color = 'b', width = 0.25*5)
        plt.bar((X + 0.25)*5, list_TX, color = 'g', width = 0.25*5)

        
         
        # Custom Axis title
        plt.ylabel('TCP Segments. Blue: RX, Green: TX (#)', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')

        plt.xlabel('Time past beginning of capture (s)', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')

        plt.title('Alex McGinnis', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')
        
        plt.xticks(np.arange(0, len(list_RX)*5, step=5))

        plt.savefig('tcp_segments.png')
        print(f'Processed {line_count} lines.')

        #plt.show()

   # time.sleep(5)




