import pandas as pd
import re

# Load the CSV file (adjust the relative path if needed)
file_path = 'Copy of National RV graphic mailer - Sheet1 (1).csv'
df = pd.read_csv(file_path)

# Function to process campground names
def process_campground_name(name):
    if pd.isna(name):
        return name
    name = str(name).title()
    name = name.replace('Rv', 'RV').replace('Llc', 'LLC')
    return name

# Process campground names
df['Campground Name'] = df['Campground Name'].apply(process_campground_name)

# Process email addresses
df['Email Address'] = df['Email Address'].replace('No email found', '').str.lower()

# Create Full Name column
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

# Debugging: Check addresses before extraction
print("Addresses before extraction:")
print(df['Address'].head(10))

# Preprocess addresses to replace line breaks with commas
df['Address'] = df['Address'].str.replace(r'\r\n', ', ', regex=True)

# Debugging: Check addresses after preprocessing
print("Addresses after preprocessing:")
print(df['Address'].head(10))

# Split address into components with updated regex pattern
# Extract second address line if present
def split_address(address):
    if pd.isna(address):
        return pd.Series([None, None, None, None, None])
    parts = address.split(', ')
    if len(parts) == 3:
        return pd.Series([parts[0].title(), '', parts[1], parts[2][:2], parts[2][3:]])
    elif len(parts) == 4:
        return pd.Series([parts[0].title(), parts[1].title(), parts[2], parts[3][:2], parts[3][3:]])
    return pd.Series([None, None, None, None, None])

address_split = df['Address'].apply(split_address)
address_split.columns = ['Street_Address', 'Second_Address_Line', 'City', 'State', 'Zip']

# Ensure title case and trim whitespace
address_split['Street_Address'] = address_split['Street_Address'].str.strip().str.title()
address_split['Second_Address_Line'] = address_split['Second_Address_Line'].str.strip().str.title()
address_split['City'] = address_split['City'].str.strip().str.title()
address_split['State'] = address_split['State'].str.strip()
address_split['Zip'] = address_split['Zip'].str.strip()

# Debugging: Check address split results
print("Address split results:")
print(address_split.head(10))

# Join the split address components back to the original DataFrame
df = df.join(address_split)

# Rename the address columns to have spaces
df.rename(columns={
    'Street_Address': 'Street Address',
    'Second_Address_Line': 'Second Address Line',
    'City': 'City',
    'State': 'State',
    'Zip': 'Zip'
}, inplace=True)

# Drop unnecessary columns if they exist
columns_to_drop = ['First Name', 'Last Name', 'Address', 'url']
existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]
df.drop(columns=existing_columns_to_drop, inplace=True)

# Save the processed DataFrame to a new CSV file
output_file_path = 'Processed_Campgrounds.csv'
df.to_csv(output_file_path, index=False)

print(f"Processed data saved to {output_file_path}")
