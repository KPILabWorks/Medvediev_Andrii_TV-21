import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# Files
files = {
    "East": "./Data_VB_A1710/East_data.xlsx",
    "South": "./Data_VB_A1710/South_data.xlsx",
    "West": "./Data_VB_A1710/West_data.xlsx"
}

# Function to process data
def process_data(filename, orientation_label):
    df = pd.read_excel(filename)

    # Convert Timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='mixed', dayfirst=False, errors='coerce')
    df = df.dropna(subset=['Timestamp'])  # Remove invalid dates
    df['Hour'] = df['Timestamp'].dt.hour

    # Filter for daylight hours (7:00 AM – 7:00 PM)
    df_daylight = df[(df['Hour'] >= 7) & (df['Hour'] <= 19)]

    # Drop rows with missing values for key columns
    df_daylight = df_daylight.dropna(subset=['BA', 'WPI_1 (A)', 'WPI_2 (A)', 'WPI_3 (A)'])

    # Calculate the average illuminance in the room
    df_daylight['Avg_Illuminance'] = df_daylight[['WPI_1 (A)', 'WPI_2 (A)', 'WPI_3 (A)']].mean(axis=1)

    # Group by each full degree of the blind slat angle
    df_daylight['BA_bin'] = df_daylight['BA'].astype(int)
    grouped = df_daylight.groupby('BA_bin')['Avg_Illuminance'].mean().reset_index()

    return grouped, orientation_label

# Plotting the graph
plt.figure(figsize=(12, 6))

for orientation, file in files.items():
    grouped_data, label = process_data(file, orientation)
    plt.plot(grouped_data['BA_bin'], grouped_data['Avg_Illuminance'], label=label)

# Graph settings
plt.xlabel('Blind Slat Angle (degrees)')
plt.ylabel('Average Illuminance (lux)')
plt.title('Illuminance vs. Blind Slat Angle')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
