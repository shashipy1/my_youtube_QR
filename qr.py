import pyqrcode
# import png

yt = "https://youtube.com/channel/UCwJCfjG4t4EZtIu1EZEnSbQ"

q = pyqrcode.create(yt)
q.png('qr.png')



# import pyqrcode
# # import image
# qr = pyqrcode.QRCode(
#     version=15,
#     box_size=10,
#     border=5
#     )
# data = "https://youtu.be/X0BdSYf-4U0"
# qr.add_data(data)
# qr.make(fit=True)
# img = pyqrcode.make_image(fill="black", back_color="white")
# img.save("qr.png")







# logic
# web = "utl/data"
# q = pyqrcode.create(yt)
# q.png('rq.png')