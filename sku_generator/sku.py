import pandas as pd
import hashlib


# Load the CSV into a DataFrame
def load_inventory(file_path):
    return pd.read_csv(file_path)


# Function to generate a SKU
def generate_sku(row, used_skus):
    # Concatenate relevant fields
    base_sku = f"{row['Handle']}-{row['Title']}-{row['Option1 Value']}-{row['Option2 Value']}-{row['Option3 Value']}"

    # Generate initial hash
    sku = hashlib.md5(base_sku.encode()).hexdigest()[:10].upper()

    # Ensure SKU is unique
    original_sku = sku
    counter = 1
    while sku in used_skus:
        sku = f"{original_sku}-{counter}"
        counter += 1

    used_skus.add(sku)
    return sku


# Add SKUs to the DataFrame
def add_skus(df):
    used_skus = set()
    df['SKU'] = df.apply(lambda row: generate_sku(row, used_skus), axis=1)
    return df


# Save the DataFrame back to a CSV
def save_inventory(df, output_path):
    df.to_csv(output_path, index=False)


# Main function to process the inventory
def process_inventory(input_file, output_file):
    df = load_inventory(input_file)
    df = add_skus(df)
    save_inventory(df, output_file)


# Example usage
input_file = 'shopify_inventory.csv'  # Replace with your input file path
output_file = 'shopify_inventory_with_skus.csv'  # Replace with your output file path

process_inventory(input_file, output_file)
