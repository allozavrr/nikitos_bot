import telebot
import logging
import time
import re
import requests
from random import randint
# from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot('bot_token')
CHANNEL_NAME = '@Lys_Mykyta_bot'

def Lys_Mykyta_bot():
    f = open('words.txt', 'r', encoding='UTF-8')
    all_words = f.read().split('\n')
    f.close()

    f = open('wishes.txt', 'r', encoding='UTF-8')
    all_wishes = f.read().split('\n')
    f.close()
    j = 0
    print('Всім доброго дня, шановні дяді й тьоті Хʼюстону!')
    while j < 2:
        a = randint(0,1)
        print(a)
        if a == 1:
            gender ='дядь'
        else: 
            gender = 'тьоть'
        i =0 
        wish = [1, 2, 3]
        word = [1, 2, 3]
        while i<=2: 
            wish[i] = all_wishes[randint(1, len(all_wishes)-1)]
            word[i] = all_words[randint(1, len(all_words)-1)] 
            i += 1
        message = (f'{word[0]}\n{word[1]}\n{word[2]}\n\n     - {wish[0].title()} {wish[1].title()} {wish[2].title()}, {randint(0, 2)} г. {gender}')
        j += 1
        search = word[randint(0,2)] 
        print(f'japan crazy {search}')
        picture(message, search)
        time.sleep(randint(28800, 57600))


def picture(message, search):
    # generate word to image

    im = requests.get(request_photo('japan crazy'))  
    out = open("img.jpg", "wb")
    out.write(im.content)
    out.close()
    image = Image.open('img.jpg')

    # generate shrift
    font = ImageFont.truetype('font.name', size= int(image.width/15))
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (int(image.width/50), int(image.height/4)),
        message,
        # send shrift to picture
        font=font,
        fill='#d60000') 

    bot.send_photo(CHANNEL_NAME, photo = request_photo(f'japan crazy {search}'), caption = message)

def request_photo(message):
    req = requests.get("https://www.google.com/search?q="+message)
    ph_links = list(filter(lambda x: '.jpg' in x, re.findall('''(?<=["'])[^"']+''', req.text)))
    ph_list = []
    for i in range(len(ph_links)):
        if (ph_links[i][0] == "h"):
            ph_list.append(ph_links[i])
    del ph_links
    return ph_list[randint(0, len(ph_list))]



Lys_Mykyta_bot()

if __name__ == '__main__':
   bot.polling(none_stop=True, interval=0)
