import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_line_chart(data_frame):
    """
    Plots a line chart showing the number of cyber events over time by protocol.
    
    Args:
        data_frame (DataFrame): A pandas DataFrame with Timestamp and Protocol columns.
    
    Returns:
        None
    """
    # Ensure the Timestamp column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(data_frame['Timestamp']):
        data_frame['Timestamp'] = pd.to_datetime(data_frame['Timestamp'])
    
    # Group data by date and protocol, then count occurrences
    line_data = data_frame.groupby([data_frame['Timestamp'].dt.date, 'Protocol']).size().unstack().fillna(0)
    
    # Plotting
    plt.figure(figsize=(15, 5))
    for protocol in line_data.columns:
        plt.plot(line_data.index, line_data[protocol], label=protocol)
    
    plt.title('Cyber Events Over Time by Protocol')
    plt.xlabel('Date')
    plt.ylabel('Number of Events')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(data_frame):
    """
    Plots a bar chart showing the distribution of cyber events by protocol.
    
    Args:
        data_frame (DataFrame): A pandas DataFrame with a Protocol column.
    
    Returns:
        None
    """
    bar_data = data_frame['Protocol'].value_counts()
    plt.figure(figsize=(10, 5))
    plt.bar(bar_data.index, bar_data.values, color='orange')
    plt.title('Distribution of Cyber Events by Protocol')
    plt.xlabel('Protocol')
    plt.ylabel('Number of Events')
    plt.xticks(rotation=45)
    plt.show()

def plot_pie_chart_enhanced(data_frame):
    """
    Plots an enhanced pie chart showing the proportion of different traffic types in cyber events.
    The enhancements include better color choices and exploded slices for emphasis.
    
    Args:
        data_frame (DataFrame): A pandas DataFrame with a Traffic Type column.
    
    Returns:
        None
    """
    pie_data = data_frame['Traffic Type'].value_counts()
    colors = plt.cm.Paired(np.arange(len(pie_data))/len(pie_data))  # Color map to generate distinct colors
    explode = [0.1 if i == pie_data.idxmax() else 0 for i in pie_data.index]  # Explode the largest slice

    plt.figure(figsize=(8, 8))
    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
    plt.title('Proportion of Traffic Types', pad=20)
    plt.show()

# Load your data
data = pd.read_csv('cybersecurity_attacks.csv')

# Now we will call these functions with the data
plot_line_chart(data)
plot_bar_chart(data)
plot_pie_chart_enhanced(data)
