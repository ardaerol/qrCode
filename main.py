import pyqrcode

url = input("qrCodunu oluşturmak istediğiniz urlyi giriniz.=")

qr = pyqrcode.create(url)
qr.svg('gitHub.svg', scale=5)