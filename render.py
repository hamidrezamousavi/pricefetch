from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
from data import currency
from tgju import get_data

data = get_data()

def prepare_text(text):
    reshaped_text = arabic_reshaper.reshape(text)    
    bidi_text = get_display(reshaped_text)
    return bidi_text

def prepare_image(data):

    img = Image.open('background.jpg')
   
    #reg = (50,20,100,40)
    #cut = img.crop(reg)
    #img.paste(pimg,(50,20))
    #img = img.transpose(Image.ROTATE_90)
    #out = img.point(lambda i: i * 3)
    #print(img.getbands())
    #im = Image.new("RGB", (200, 200), "white")
    # d.line(((0, 100), (200, 100)), "gray")
   # d.line(((100, 0), (100, 200)), "gray")
    font = ImageFont.truetype("BNAZANIN_0.ttf", 48)
    
    
    
    d = ImageDraw.Draw(img)
   
    d.text((100, 100), bidi_text, fill="green", anchor="ms", font=font)

    img.show()