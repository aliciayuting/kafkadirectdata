import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


def plot_throughput_data():
    df = pd.read_csv('throughput_processed_data.csv')
    df.sort_values(['mr'], inplace=True)
    colors = ['r', 'g', 'b']
    record_sizes = [1024, 16384, 262144]
    rfs = [3]  # , 3]
    line_styles = ['-', '-.']
    plt.xscale('log', base=2)
    for i in range(len(record_sizes)):
        for j in range(len(rfs)):
            rs = record_sizes[i]
            rf = rfs[j]
            cur_df = df[(df['rs'] == rs) & (df['rf'] == rf)]
            cur_label = f"record_size={rs},replication={rf}"
            plt.errorbar(cur_df['throughput(MiB/s)'], cur_df['ete_latency50'],
                         yerr=cur_df['ete_std'], color=colors[i],  label=cur_label)
    plt.xlabel('throughput(MiB/s)')
    plt.ylabel('end-to-end latency(us)')
    plt.legend()
    plt.show()


plot_throughput_data()
