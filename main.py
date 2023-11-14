import qrcode

def generates_qr_code(link: str, file_name: str) -> None:
    """Generates an png qr_code file
    
    Parameters
    ----------
    link : str
        Link returned by the qr code
    file_names : str
        Name of final file with extension. ex: .png, .jpg
    """

    # Creates QRCode object
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)

    # Add link to qr code
    qr.add_data(link)
    qr.make(fit=True)

    # Creates a image
    img = qr.make_image(fill_color="black", back_color="white")


    img.save(file_name)

if __name__ == "__main__":
    # Get the link
    link = input("Type link to the QR code: ")
    
    # Defines file name
    file_name = input("Type file name  (with extension): ")

    # Generates the qr code
    generates_qr_code(link, file_name)

    print("QR Code generated successfully;")
