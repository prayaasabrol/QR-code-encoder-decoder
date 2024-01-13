import qrcode
import cv2

# Function to encode data into a QR code
def encode_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR code saved as {filename}")

# Function to decode a QR code from an image
def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, points, straight_qrcode = detector.detectAndDecode(img)

    if data:
        print(f"Decoded data from QR code: {data}")
    else:
        print("No QR code detected or decoded")

# Prompt the user to input the website URL
website_url = input("Enter the website URL: ")

# Encode the website URL into a QR code
qr_code_filename = input("Enter the name of the file: ")
encode_qr_code(website_url, qr_code_filename)

# Decode a QR code from an image
decode_qr_code(qr_code_filename)
