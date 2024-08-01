import qrcode

def generate_qr_code(url, output_filename="qr_code.png"):
    """Generates a QR code pointing to the specified URL.

    Args:
        url (str): The URL to be linked to the QR code.
        output_filename (str, optional): The filename for the generated QR code image.
            Defaults to "qr_code.png".
    """
    qr = qrcode.QRCode(
        version=1,  # Adjust for desired QR code size and data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Adjust for desired pixel size of each QR code box
        border=4,  # Adjust for desired white border around the QR code
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(output_filename)
    print(f"QR code generated and saved as: {output_filename}")

# Example usage
redirect_html_url = "https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model13"  # Replace with your actual hosted HTML file URL
generate_qr_code(redirect_html_url)
