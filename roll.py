import requests
import random



def get_roll():
    mon = random.randint(1, 10)
    return "Твое число" + " " + str(mon)