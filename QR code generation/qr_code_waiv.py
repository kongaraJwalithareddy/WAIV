import qrcode
# Program: To generate a QR code, it doesn't get expired and no need to pay for the QR code. Can customize the QR size and apprearance a little bit.

# Data to encode (this can be any string, such as a URL, text, contact information, etc.)
data = "https://www.csulb.edu/career-development-center/workability-iv-program"

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Controls how many pixels each “box” of the QR code is
    border=2,  # Controls how many boxes thick the border should be
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)  # Fit the data in the QR Code

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")
