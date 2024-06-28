from PIL import Image,ImageFont,ImageDraw
import textwrap


def main(input_image, text,text_font=30):

    def calculate_best_wrap_width(text,image_width, text_width):
        min_wrap_width = 10
        reserved_width = image_width // 1.17
        max_chars_per_line = reserved_width // (text_width / len(text))
        return max(min_wrap_width, max_chars_per_line)
    

    img = Image.open(input_image)
    img_width,img_height = img.size

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Russo_One\RussoOne-Regular.ttf',size=text_font)

    left,right = draw.textbbox((0,0),text=text,font=font)[::2]
    text_width = right-left
    
    if text_width > img_width:
        text= textwrap.fill(text,break_long_words=False,break_on_hyphens=True,width=calculate_best_wrap_width(text,img_width,text_width))
    
    if text_width <= img_width //1.5:   # textposition when the 'text' is too small
        text_position = (img_width // 5, img_height // 3 )  # img_height //3  means text will start from upper center of image if you want to start from top you can change it to 0
    
    else:  # textposition when the 'text' is long
        text_position = (10, img_height // 3)

    draw.multiline_text(text_position,spacing=0,align='center',text=text,font=font,fill='yellow')
    img.save('changed.jpg')


if __name__ == '__main__':
    input_image =  'input.jpg'
    text ='''In the realm of technology, the rapid evolution of artificial intelligence (AI) continues to redefine the landscape of innovation. From intelligent virtual assistants to advanced natural language processing, AI is permeating various aspects of our daily lives.'''
    text_font =25
    main(input_image,text,text_font)








