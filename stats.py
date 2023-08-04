import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("results_stats.csv")

# Calculate average response time
avg_response_time = data["Average Response Time"].mean()

# Calculate maximum response time
max_response_time = data["Max Response Time"].max()

# Calculate number of requests
num_requests = data.shape[0]

# Calculate number of failures
num_failures = data["Failure Count"].sum()
# Plot response time distribution
plt.hist(data["Average Response Time"], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Response Time (ms)')
plt.ylabel('Frequency')
plt.title('Response Time Distribution')
plt.show()
