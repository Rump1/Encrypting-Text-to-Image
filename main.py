from PIL import Image

def encryption(img, text_input): # Шифрование
    for i in range(0,len(text_input) * 8, 3):
        one_pixel = img.getpixel((i%img.width//3, i//img.width)) # Получение пикселя для обработки
        red = one_pixel[0] & 0xFE # Зануляем последние биты
        green = one_pixel[1] & 0xFE
        blue = one_pixel[2] & 0xFE
        red += ord(text_input[i//8]) >> (7 - i%8) & 1 # Обработка красного цвета, изменение последнего бита
        if i+1 < len(text_input) * 8:
            green += ord(text_input[(i+1)//8]) >> (7 - (i+1)%8) & 1 # Обработка зеленого цвета
        if i + 2 < len(text_input) * 8:
            blue += ord(text_input[(i+2)//8]) >> (7 - (i+2)%8) & 1 # Обработка синего цвета
        img.putpixel((i % img.width // 3, i // img.width),(red,green,blue)) # Изменение пикселя в картинке
    img.save("encrypted_image.png")

def decryption(img):
    result = ""
    letter = 0
    i = 0
    while result == "" or result[-1] != '\0':
        one_pixel = img.getpixel((i % img.width // 3, i // img.width))
        for x in range(3):
            letter = letter << 1
            letter += (one_pixel[x] & 1)
            i += 1
            if i % 8 == 0:
                result += chr(letter)
                letter = 0
    return result[:-1]

text_input = input("Введите текст для шифрования ")
text_input += '\0' # Добавление нулевого символа для определения конца дешифровки
img = Image.open("Image.png") # Открытие картинки для работы
encryption(img, text_input)
enc_img = Image.open("encrypted_image.png")
print(decryption(enc_img))