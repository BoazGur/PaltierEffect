import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import math

def main():
    paths = sys.argv[1:]

    for idx, path in enumerate(paths):
        temp0 = []
        temp1 = []
        delta = []

        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line != '\n':
                    splited = line.split()

                    if '1AMPER.txt' in path:
                        temp0.append(float(splited[4]))
                        temp1.append(float(splited[1]))
                        delta.append(float(splited[4]) - float(splited[1]))
                    else:                       
                        temp0.append(float(splited[1]))
                        temp1.append(float(splited[4]))
                        delta.append(float(splited[1]) - float(splited[4]))

        time = np.arange(0, max(len(temp1), len(temp0)) * 0.5, 0.5) # Sampled every 500ms

        data = {'temp0': temp0, 'temp1': temp1, 'time': time, 'delta': delta}
        df = pd.DataFrame(data)

        sns.set_theme(style="darkgrid")
        sns.scatterplot(x='time', y='temp0', data=df)
        sns.scatterplot(x='time', y='temp1', data=df)
        sns.scatterplot(x='time', y='delta', data=df)
        plt.errorbar(df.time, df.temp0, yerr=0.5, alpha=0.2)
        plt.errorbar(df.time, df.temp1, yerr=0.5, alpha=0.2)
        plt.errorbar(df.time, df.delta, yerr=math.sqrt(2)/2, alpha=0.2)
        plt.legend(labels=["temp0", "temp1", 'delta'])
        plt.xlabel('time [s]')
        plt.ylabel('temprature [C]')
        plt.title(f'{(idx + 1) * 0.5} Amper')
        plt.savefig(f'{(idx + 1) * 0.5}AMPER.png')
        plt.show()
    

if __name__ == '__main__':
    main()
