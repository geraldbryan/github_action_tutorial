import pandas as pd
from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Extract date, day, and time
date_today = current_datetime.strftime('%Y-%m-%d')
day_today = current_datetime.strftime('%A')
time_today = current_datetime.strftime('%H:%M:%S')

# Create DataFrame
df = pd.DataFrame({
    'date today': [date_today],
    'day today': [day_today],
    'time today': [time_today]
})

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Write JSON data to a file
with open('today_data.json', 'w') as file:
    file.write(json_data)

print("JSON file saved successfully.")
