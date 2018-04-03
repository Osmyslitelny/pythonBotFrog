import logging
import random

import vk

logger = logging.getLogger(__name__)


def tea(bot, update):

    session = vk.Session(access_token='========')
    vk_api = vk.API(session)
    wall_posts = vk_api.wall.get(owner_id=-41691627, filter="owner", count=100, v=5.76)
    id = wall_posts["items"][random.randint(0, 100)]["id"]
    photo_url = wall_posts["items"][random.randint(0,100)]["attachments"][0]["photo"]["photo_1280"]

    bot.send_photo(update.message.chat.id, photo_url)
