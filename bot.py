import requests
import misc
from yobit import get_btc
from time import sleep
from creator import get_creator
from roll import get_roll
from ask_fm import get_ask
from discord import get_discord
from group import get_group
from group_steam import get_groupsteam
from instagram import get_instagram
from steam import get_steam
from sub import get_sub
from trade import get_trade
from twitch import get_twitch
from vk import get_vk
from youtube import get_youtube
from uslovie import get_botsay

#import json

token = misc.token
#https://api.telegram.org/bot529526555:AAGZMZDY988e67XquePj3eJxjblBcf_6ru0/sendmessage?chat_id=439398622&text=hi
URL = "https://api.telegram.org/bot" + token + "/"


global last_update_id
last_update_id = 0


def get_updates():
    url = URL + "getupdates"
    r = requests.get(url)
    return r.json()



def get_message():
	
    data = get_updates()
    
    last_object = data["result"][-1]
    current_update_id = last_object["update_id"]
	
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object["message"]["chat"]["id"]
        message_text = last_object["message"]["text"]

        message = {"chat_id": chat_id,
                   "text": message_text}
        
        return message
    return None


def send_message(chat_id, text="Wait...."):
	url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
	requests.get(url)



def main():
    #d = get_updates()
    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer["chat_id"]
            text = answer["text"]
        
            if text == "/btc":
                send_message(chat_id, get_btc())

            elif text == "/btc@JeffFosterUKBot":
                send_message(chat_id, get_btc())
            
            elif text == "/creator":
                send_message(chat_id, get_creator())
            
            elif text == "/creator@JeffFosterUKBot":
                send_message(chat_id, get_creator())

            elif text == "/roll":
                send_message(chat_id, get_roll())

            elif text == "/roll@JeffFosterUKBot":
                send_message(chat_id, get_roll())
        
            elif text == "/ask":
                send_message(chat_id, get_ask())

            elif text == "/ask@JeffFosterUKBot":
                send_message(chat_id, get_ask())

            elif text == "/discord":
                send_message(chat_id, get_discord())

            elif text == "/discord@JeffFosterUKBot":
                send_message(chat_id, get_discord())

            elif text == "/group":
                send_message(chat_id, get_group())

            elif text == "/group@JeffFosterUKBot":
                send_message(chat_id, get_group())

            elif text == "/group_steam":
                send_message(chat_id, get_groupsteam())

            elif text == "/group_steam@JeffFosterUKBot":
                send_message(chat_id, get_groupsteam())

            elif text == "/instagram":
                send_message(chat_id, get_instagram())

            elif text == "/instagram@JeffFosterUKBot":
                send_message(chat_id, get_instagram())

            elif text == "/steam":
                send_message(chat_id, get_steam())

            elif text == "/steam@JeffFosterUKBot":
                send_message(chat_id, get_steam())

            elif text == "/sub":
                send_message(chat_id, get_sub())

            elif text == "/sub@JeffFosterUKBot":
                send_message(chat_id, get_sub())

            elif text == "/trade":
                send_message(chat_id, get_trade())

            elif text == "/trade@JeffFosterUKBot":
                send_message(chat_id, get_trade())

            elif text == "/twitch":
                send_message(chat_id, get_twitch())

            elif text == "/twitch@JeffFosterUKBot":
                send_message(chat_id, get_twitch())

            elif text == "/vk":
                send_message(chat_id, get_vk())

            elif text == "/vk@JeffFosterUKBot":
                send_message(chat_id, get_vk())

            elif text == "/youtube":
                send_message(chat_id, get_youtube())

            elif text == "/youtube@JeffFosterUKBot":
                send_message(chat_id, get_youtube())

            elif "Бот," in text:
                send_message(chat_id, get_botsay())


        else:
            continue


        sleep(2)
        




if __name__ == "__main__":
    main()  