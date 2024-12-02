"""	
•	argparse is used to handle command-line arguments:
•	model_number: The number for the model, appended to the URL.
•	output_filename: The name of the generated QR code image file.
•	The URL is dynamically constructed using the provided model number.
•	The QR code is saved with the specified filename.
Usage:
python Qr-code-v2.py XX name.png
    """
import qrcode
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code for a specific model.")
    parser.add_argument("model_number", type=int, help="The model number to include in the URL.")
    parser.add_argument("output_filename", type=str, help="The output filename for the QR code image.")

    args = parser.parse_args()

    # Ensure the output filename ends with .png
    if not args.output_filename.endswith(".png"):
        args.output_filename += ".png"

    # Replace with your base URL
    base_url = "https://jmb-scripts.github.io/AR-Structural-Biology/index.html"
    full_url = f"{base_url}?model=model{args.model_number}"

    generate_qr_code(full_url, args.output_filename)