import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Load the data
df = pd.read_csv('results.csv', delimiter=';')

def plot_data(ax, data):
    data = data.sort_values('Input')
    ax.set_xlabel('Input Size')

    # Generate a color map based on the number of unique algorithms
    colors = plt.colormaps["Dark2"]

    # Create the second y-axis and remove its tick labels
    ax2 = ax.twinx()
    ax2.set_ylabel('Solution')

    algo_handles = []

    for idx, algo in enumerate(data['Algorithm'].unique()):
        algo_data = data[data['Algorithm'] == algo]

        ax.plot(algo_data['Input'], algo_data['Time'], color=colors(idx))
        ax2.plot(algo_data['Input'], algo_data['Solution'], linestyle='-.', color=colors(idx))
        algo_handles.append(Line2D([0], [0], color=colors(idx), label=f'{algo}'))

    ax.set_ylabel('Time')
    ax.set_title(f'Benchmark')

    handles_style = [
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='Time'),
        Line2D([0], [0], color='black', linestyle='-.', linewidth=2, label='Solution')
    ]

    combined_handles = handles_style + algo_handles

    ax.legend(handles=combined_handles, loc='upper left')
    ax.grid(True)

fig, ax = plt.subplots(figsize=(12, 12))
plot_data(ax, df)
fig.tight_layout()
plt.savefig('assets/plot.svg')
plt.show()
