import pymumble_py3 as pymumble
from time import sleep

afkbot = pymumble.Mumble("multiverse.jo3.io", "afkBot", password='beersh!tz')
afkbot.set_application_string('afkbot')
afkbot.start()
afkbot.is_ready()
afkbot.set_bandwidth(72000)

userList = afkbot.users


isRunning = True;

while isRunning:
    for session in userList:
        print(userList)
        for u in userList:
            print(userList[u]['name']+ ' sound: ' + str(userList[u].sound.is_sound()))
            userList[u].mute()

    sleep(10)
#         # print(userList[session].get_property('name'))
#         # userList[session].send_message('HEY! You will be muted now, this is a test.')
#         print(userList[session].mute())
#         print(userList[session].idlesecs)
