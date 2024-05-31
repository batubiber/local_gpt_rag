with open("C:/Users/PC_5185/Desktop/private-gpt/private_gpt/ui/baykar.ico", "rb") as ico_file:
    ico_data = ico_file.read()

import base64
encoded_ico_data = base64.b64encode(ico_data)


with open("C:/Users/PC_5185/Desktop/private-gpt/private_gpt/ui/embed.txt", "wb") as a:
    a.write(encoded_ico_data)
