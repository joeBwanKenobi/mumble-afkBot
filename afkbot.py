import pymumble_py3 as pymumble

afkbot = pymumble.Mumble("multiverse.jo3.io", "afkBot", password='beersh!tz')
afkbot.set_application_string('afkbot')
afkbot.start()
afkbot.is_ready()
afkbot.set_bandwidth(72000)

userList = afkbot.users

print(userList)
for session in userList:
    print(userList[session])