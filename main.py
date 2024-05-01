from PIL import Image, ImageDraw, ImageFont
def zadacha1():
    jpg = Image.open('otk.jpg')
    newjpg = jpg.crop((380,380,1630,1630))
    newjpg.show()
    newjpg.save('otk2.jpg')

def zadacha2():
    otk = {'1 мая' : 'may1.jpg', '1 апреля' : 'apr1.jpg', 'новый год' : 'jan1.jpg', '8 марта' : 'mar8.jpg', '23 февраля' : 'feb23.jpg'}
    day = input('Введите день праздника:')
    if day in otk:
        jpg = Image.open(otk[day])
        jpg.show()

def zadacha3():
    name = input('Введите имя:')
    name= name + ' ,поздравляю!'
    jpg = Image.open('otk.jpg')
    newjpg = jpg.crop((300, 300, 1800, 1800))
    newtext = ImageDraw.Draw(newjpg)
    newfont = ImageFont.truetype('arial.ttf',32)
    newtext.text((50,50), name, font=newfont, fill=(255,255,255))
    newjpg.save('otk3.jpg')
    newjpg.show()
