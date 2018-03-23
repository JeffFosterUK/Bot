import requests
import random




def get_botsay():

    mon = random.randint(1, 2)

    if mon == 1:
    	return "Да"
    elif mon == 2:
    	return "Нет"
