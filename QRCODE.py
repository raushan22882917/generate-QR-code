import qrcode
qr = qrcode.QRCode()
qr.add_data("sitare university")
qr.make()
img = qr.make_image()
img.save("rk.png")