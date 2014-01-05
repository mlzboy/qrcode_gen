#!/usr/bin/env python
#encoding=utf-8
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image()
print type(img)
#help(img)
f = open("./zz.png","wb")
img.save(f)
f.close()

