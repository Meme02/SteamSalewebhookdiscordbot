from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from bs4 import BeautifulSoup
import time

#Packages used in this file were not made by the creator of this file

webhook = DiscordWebhook(url='WEBHOOK URL GOES HERE')

#List of games for the bot to check with a True or False statment. True standing for on sale, and False for not on sale. Everything is set to False for now.
urls = (['https://store.steampowered.com/app/1172620/Sea_of_Thieves/', False], ['https://store.steampowered.com/app/1144200/Ready_or_Not/', False], ['https://store.steampowered.com/app/235460/METAL_GEAR_RISING_REVENGEANCE/', False])


#Functions
def check(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    if soup.find('div', {'class': 'discount_block game_purchase_discount'}) != None:
        return True
    else:
        return False

def get_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    unprocessed = soup.find('div', {'class': 'responsive_page_header_img'})
    image = unprocessed.find('img').attrs['src']
    print(image)
    return image



#Main
while True:
    print("Started")
    for url in urls:
        if url[1] == False:
            if check(url[0]) == True:
                print("Game is on sale!")
                embed = DiscordEmbed(title='This game is on sale!', description=url[0], color='1C4C9A')
                embed.set_image(url=get_image(url[0]))
                webhook.add_embed(embed)
                response = webhook.execute()

    time.sleep(3600*2)    
#At the time of making this I am very much tired.            
    