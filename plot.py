import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

CAPACITY = 1000

def calculate_value(row):
    if row["Algorithm"] == "backtracking":
        return 2 ** row["Input"]
    else:
        return row["Input"] * CAPACITY

# Load the data
df_1_36 = pd.read_csv('results_1_36.csv', delimiter=';')
df_1_36["Expected Asymptotic Behavior"] = df_1_36.apply(calculate_value, axis=1)
result = df_1_36.groupby("Algorithm")["Time"].agg(['max', 'min']).reset_index()
# Merge the max and min back into the original dataframe
df_1_36 = pd.merge(df_1_36, result, on="Algorithm", how="left")

# Function to apply the scaling for each row
def scale_behavior(row):
    max_time = row['max']
    min_time = row['min']
    asymptotic_behavior = row['Expected Asymptotic Behavior']
    # Apply the min-max scaling
    scaled_value = (asymptotic_behavior - df_1_36["Expected Asymptotic Behavior"].min()) / \
                   (df_1_36["Expected Asymptotic Behavior"].max() - df_1_36["Expected Asymptotic Behavior"].min()) \
                   * (max_time - min_time) + min_time
    return scaled_value

# Apply the scaling function
df_1_36["Expected Asymptotic Behavior"] = df_1_36.apply(scale_behavior, axis=1)

df = pd.read_csv('results.csv', delimiter=';')
df["Expected Asymptotic Behavior"] = df["Input"] * CAPACITY
min_time = df["Time"].min()
max_time = df["Time"].max()
df["Expected Asymptotic Behavior"] = (df["Expected Asymptotic Behavior"] - df["Expected Asymptotic Behavior"].min()) / \
                                   (df["Expected Asymptotic Behavior"].max() - df["Expected Asymptotic Behavior"].min()) \
                                   * (max_time - min_time) + min_time

def plot_data_1_36(ax, data):
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
        ax.plot(algo_data['Input'], algo_data['Expected Asymptotic Behavior'], color=colors(idx+2))
        ax2.plot(algo_data['Input'], algo_data['Solution'], linestyle='-.', color=colors(idx))
        algo_handles.append(Line2D([0], [0], color=colors(idx), label=f'{algo}'))

        if idx == 0:
            algo_handles.append(Line2D([0], [0], color=colors(idx+2), label='O(2^n)'))
        else:
            algo_handles.append(Line2D([0], [0], color=colors(idx+2), label='O(N*W)'))

    ax.set_ylabel('Time')
    ax.set_title(f'Benchmark')

    handles_style = [
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='Time'),
        Line2D([0], [0], color='black', linestyle='-.', linewidth=2, label='Solution')
    ]

    combined_handles = handles_style + algo_handles

    ax.legend(handles=combined_handles, loc='upper left')
    ax.grid(True)

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
        ax.plot(algo_data['Input'], algo_data['Expected Asymptotic Behavior'], color=colors(idx+1))
        ax2.plot(algo_data['Input'], algo_data['Solution'], linestyle='-.', color=colors(idx))
        algo_handles.append(Line2D([0], [0], color=colors(idx), label=f'{algo}'))
        algo_handles.append(Line2D([0], [0], color=colors(idx+1), label='O(N*W)'))

    ax.set_ylabel('Time')
    ax.set_title(f'Benchmark')

    handles_style = [
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='Time'),
        Line2D([0], [0], color='black', linestyle='-.', linewidth=2, label='Solution')
    ]

    combined_handles = handles_style + algo_handles

    ax.legend(handles=combined_handles, loc='upper left')
    ax.grid(True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
plot_data_1_36(ax1, df_1_36)
plot_data(ax2, df)
plt.subplots_adjust(hspace=0.5)
plt.savefig('assets/plot.svg')
plt.show()
