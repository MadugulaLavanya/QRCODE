import pyqrcode
from pyqrcode import QRCode
s="www.google.com"
url=pyqrcode.create(s)
url.svg("MyQRcode.svg",scale=10)