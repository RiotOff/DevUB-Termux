# Общедоступные модули, которые могут использовать другие пользователи


from pyrogram import Client, filters

cinfo = "Здесь ваше название команды"
ccomand = "Здесь ваше описание команды"
with open("userbot.info", "r") as file:
    lines = file.readlines()

with open("bldb.info", "r") as file:
    for line in file:
        user_id = int(line.strip())
        blacklist.append(user_id)


# Замените "example" на название вашего модуля
def command_example(app):
    @app.on_message(filters.command("hi", prefixes="."))
    def example_module(client, message):
        user_id = str(message.from_user.id)
        if user_id in open("bldb.info").read():
            message.reply("`Вам запрещено использовать эту команду.`")
        else:
            message.reply_text("`Привет!`")


# Замените "example" на название вашего модуля
print("Модуль example загружен!")

# После того как сделали модуль, добавьте это в файл "modules.info":
# module_example
# (Замените "example" на название вашего модуля)
