import discord # обычная библиотека
import time # библиотека для вермени
import logging # библиотека для логов

# В кавычки вставить свой токен
TOKEN = ""
# Вставить в кавычки ID дискорд сервера где используется бот
SERVER_ID = int("")
# Включить логи "True", выключить "False"
logs = False
# Текст который отправит бот
text = """
Привет, я бот написанный @imb1rka.
Держи ссылку для проверки значка:
https://discord.com/developers/active-developer
"""
# формат времени для консоли
time = time.strftime("%Y-%m-%d %X")
# Конфиг для логов (не работает если logs=False)
if logs == True:
    logging.basicConfig(level=logging.INFO, filename="logging.log", filemode="w", encoding="UTF-8", format="%(asctime)s %(levelname)s %(message)s")
else:
    pass

print(f"\n\n{time} INFO     Код дошёл до класса (Kitagawa) [@imb1rka]")
class Kitagawa(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)

    async def on_ready(self):
        start = f"БОТ ЗАПУЩЕН ({self.user}) [@imb1rka]"
        logging.info(start)
        print(f"{time} INFO     Бот запущен ({self.user}) [@imb1rka]")

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=SERVER_ID))
        await self.tree.sync()

print(f"{time} INFO     Создание экземпляра класса (Kitagawa) [@imb1rka]")
client = Kitagawa()

@client.tree.command(name="imb1rka", description="FOR IMB1RKA UwU")
async def imb1rka(interaction: discord.Interaction) -> None:
    if logs == True:
        name = interaction.user.name
        ids = interaction.user.id
        logging.info(f"Команду /imb1rka использовал: [{name} | {ids}]")
    else:
        pass
    await interaction.response.send_message(text)

print(f"{time} INFO     Код на дошёл до (client.run) [@imb1rka]")
client.run(TOKEN)