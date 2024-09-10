import qrcode
import pandas as pd

def create_contact_qr_code(name, direct_number, office_number, email):
    # Construct vCard data
    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{name};;;;\nTEL;TYPE=CELL:{direct_number}\nTEL;TYPE=WORK:{office_number}\nEMAIL;TYPE=INTERNET:{email}\nEND:VCARD"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    return qr_image

if __name__ == "__main__":
    csv_file = "contacts.csv"  # Specify the path to your CSV file here

    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        name = row['Name']
        direct_number = row['Direct']
        office_number = row['Office']
        email = row['Email']

        qr_code = create_contact_qr_code(name, direct_number, office_number, email)
        qr_code.save(f"{name}_contact_qr_code.png")
        print(f"QR code for {name} saved as '{name}_contact_qr_code.png'")
