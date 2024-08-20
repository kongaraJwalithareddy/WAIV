import pandas as pd
import json

# Load the input Excel file
input_file = 'Book2.xlsx'
df = pd.read_excel(input_file)

# Create a new DataFrame with the required columns
formatted_df = pd.DataFrame()

# Parse 'Custom Fields' JSON and extract 'Student ID Number' and 'Meeting Location'
def extract_custom_fields(custom_fields, key):
    try:
        return json.loads(custom_fields).get(key, None)
    except (TypeError, json.JSONDecodeError):
        return None

formatted_df['Student ID'] = df['Custom Fields'].apply(lambda x: extract_custom_fields(x, 'Student ID Number'))
formatted_df['Meeting Format'] = df['Custom Fields'].apply(lambda x: extract_custom_fields(x, 'Meeting Location'))

# Convert 'Date Time' to 'Counseling Date' and 'Counseling Time'
if 'Date Time' in df.columns:
    counseling_datetime = pd.to_datetime(df['Date Time'], errors='coerce')
    formatted_df['Counseling Date'] = counseling_datetime.dt.strftime('%m/%d/%Y')
    formatted_df['Counseling Time'] = counseling_datetime.dt.strftime('%I:%M %p') + ' PT'
else:
    formatted_df['Counseling Date'] = pd.Series([None] * len(df))
    formatted_df['Counseling Time'] = pd.Series([None] * len(df))

# Add the constant columns
formatted_df['Counseling Type'] = 'Career Exploration and Planning'
formatted_df['Counselor'] = 'WorkAbility IV'

# Map the 'Duration (mins.)' column to 'Appointment Length'
formatted_df['Appointment Length'] = df.get('Duration (mins.)', pd.Series([None] * len(df)))

# Save the formatted data to a new Excel file
output_file = 'formatted_Book2.xlsx'
formatted_df.to_excel(output_file, index=False)

print(f"Formatted data has been saved to {output_file}")
