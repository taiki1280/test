from line_notify_bot import LINENotifyBot

bot = LINENotifyBot(access_token="naK0YLzsQHyzaVjNzFdVmS9CnuA4hoxvW6THqCHlTIh")

bot.send(
    message="Write Your Message",
    image="test.png",  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
    )