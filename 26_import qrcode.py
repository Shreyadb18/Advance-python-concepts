import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('I am learning python from Engineering in kannada')
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="black")

img.save("/Users/shreyasmac/eik_qr.png")