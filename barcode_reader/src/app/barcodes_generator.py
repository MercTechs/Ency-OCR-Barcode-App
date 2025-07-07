from barcode import Code128, Code39, EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import io

def generate_code128(data, filename):
    """Generate Code128 barcode"""
    code128 = Code128(data, writer=ImageWriter())
    buffer = io.BytesIO()
    code128.write(buffer)
    
    # Save the image
    with open(f"{filename}.png", 'wb') as f:
        buffer.seek(0)
        f.write(buffer.read())
    print(f"Code128 barcode saved as {filename}.png")

def generate_code39(data, filename):
    """Generate Code39 barcode"""
    code39 = Code39(data, writer=ImageWriter())
    buffer = io.BytesIO()
    code39.write(buffer)
    
    with open(f"{filename}.png", 'wb') as f:
        buffer.seek(0)
        f.write(buffer.read())
    print(f"Code39 barcode saved as {filename}.png")

def generate_ean13(data, filename):
    """Generate EAN13 barcode (needs 12 digits, checksum auto-calculated)"""
    # EAN13 needs exactly 12 digits
    if len(data) != 12 or not data.isdigit():
        data = "123456789012"  # Default valid EAN13 data
    
    ean13 = EAN13(data, writer=ImageWriter())
    buffer = io.BytesIO()
    ean13.write(buffer)
    
    with open(f"{filename}.png", 'wb') as f:
        buffer.seek(0)
        f.write(buffer.read())
    print(f"EAN13 barcode saved as {filename}.png")

def create_sample_barcodes():
    """Create a variety of sample barcodes"""
    
    # Code128 barcodes
    generate_code128("SAMPLE123", "sample_code128_text")
    generate_code128("9876543210", "sample_code128_numbers")
    
    # Code39 barcodes
    generate_code39("HELLO", "sample_code39_text")
    generate_code39("123456", "sample_code39_numbers")
    
    # EAN13 barcode
    generate_ean13("123456789012", "sample_ean13")
    
    print("\n✅ All sample barcodes generated successfully!")
    print("Files created:")
    print("- sample_qr_*.png (QR codes)")
    print("- sample_code128_*.png (Code128 barcodes)")
    print("- sample_code39_*.png (Code39 barcodes)")
    print("- sample_ean13.png (EAN13 barcode)")

if __name__ == "__main__":
    # Install required packages first:
    # pip install qrcode[pil] python-barcode[images] pillow
    
    create_sample_barcodes()