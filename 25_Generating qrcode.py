import qrcode

image = qrcode.make("Engineering in kannada")

image.save("/Users/shreyasmac/eik_qr.png")

print("QR code generation successful. The QR code has been saved as 'eik_qr.png'.")

