import csv
import os

def create_vcf(full_name, email, office, direct, output_dir):
    vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=WORK,VOICE:{office}
TEL;TYPE=CELL,VOICE:{direct}
END:VCARD
"""
    # Replace any invalid filename characters in the full name
    safe_full_name = "".join([c if c.isalnum() or c in (' ', '.', '_') else '_' for c in full_name])
    vcf_filename = os.path.join(output_dir, f"{safe_full_name}.vcf")

    with open(vcf_filename, 'w', encoding='utf-8') as vcf_file:
        vcf_file.write(vcf_content)

def csv_to_vcf(csv_filename, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            full_name = row['Full Name']
            email = row['Email']
            office = row['Office']
            direct = row['Direct']
            create_vcf(full_name, email, office, direct, output_dir)

if __name__ == "__main__":
    csv_filename = "contacts.csv" 
    output_dir = "vcf_contacts"  # Directory where VCF files will be saved
    csv_to_vcf(csv_filename, output_dir)
