import qrcode

date = {
    "name": "John Bills",
    "age": 30,
    "address": "123 Main St, Springfield, USA",
    "phone": "+1234567890",
    "email": "johnjohn@gmail.com"
}
qr = qrcode.make(f"{date['name']}, {date['age']}, {date['address']}, {date['phone']}, {date['email']}")
qr.save("data.jpg")