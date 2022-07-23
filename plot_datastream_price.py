import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


if __name__ == '__main__':

    TAIL_NUMBER = 50
    DATA_FILE_NAME = 'data/EUR_USD_1m.csv'

    plt.ion()
    
    while True:
        df_signal_plot = pd.read_csv(DATA_FILE_NAME, index_col=0, parse_dates=True,header=0)
        plt.plot( df_signal_plot['close'][-TAIL_NUMBER:], color='black', label='EUR_USD')
        plt.title('Stream data EURUSD price', color='darkblue')
        plt.xlabel("datetime")
        plt.ylabel("EUR / USD")
        plt.draw()
        plt.pause(0.1)
        plt.clf()
        time.sleep(1)

    plt.show(block=True)
