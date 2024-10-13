from pyrogram import Client, filters

cinfo = "Здесь ваше название команды"
ccomand = "Здесь ваше описание команды"
with open("userbot.info", "r") as file:
    lines = file.readlines()


# Замените "example" на название вашего модуля
def command_example(app):
    @app.on_message(filters.command("hi", prefixes="."))
    def example_module(client, message):
        message.edit("Привет!")


# Замените "example" на название вашего модуля
print("Модуль example загружен!")

# После того как сделали модуль, добавьте это в файл "modules.info":
# module_example
# (Замените "example" на название вашего модуля)
