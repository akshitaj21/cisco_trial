# Simple Python script to batch generate QR codes
import qrcode

token = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
url = f"https://myclub.vercel.app/verify/{token}"
img = qrcode.make(url)
img.save("member_john_doe.png")