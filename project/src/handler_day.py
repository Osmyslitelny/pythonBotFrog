import logging
import datetime
from datetime import datetime
import random
import glob

logger = logging.getLogger(__name__)


def day(bot, update):
    message = update.message
    person_name = message.from_user.first_name
    responce_text = "Bad news for you, " + person_name

    day = datetime.today().weekday()
    day_path = "project\\resource\\days\\"

    get_file = lambda file_name: glob.glob(day_path + file_name + '.jpg')
    get_files = lambda files_path: glob.glob(day_path + files_path)

    imags_list = get_files(str(day) + "\\*")
    common_image_list = get_files("common_day" + "\\*")
    imags_list.extend(common_image_list)

    photo = random.choice(imags_list)
    if day is 0:
        ""
    elif day is 1:
        ""
    elif day is 2:
        photo = get_file(str(day) + '\\wednesday')
        response_text = 'Yep, it is!'
    elif day is 3:
        ""
    elif day is 4:
        if message.from_user.username == 'FedchenkoR':
            photo = get_file(str(day) + '\\fridayForRoman')
            response_text = "It isn't wednesday, but don't be upset , " + person_name + ", it is friday!"
    elif day is 5:
        ""
    elif day is 6:
        ""
    bot.send_photo(message.chat.id, open(photo, 'rb'), responce_text)
