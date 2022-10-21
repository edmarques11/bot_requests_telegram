import os
import telebot
from dotenv import load_dotenv

load_dotenv()

CHAVE_API = os.environ['CHAVE_API']

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["pizza", "hamburguer", "salada"])
def request(message):
    text = message.text.replace('/', '') + ' fica pronto em 20 min.'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["opcao1"])
def opcao1(message):
    text = 'O que você quer? (Clique em uma opção).\n\n/pizza Pizza\n/hamburguer Hamburguer\n/salada Salada'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["opcao2"])
def opcao2(message):
    bot.send_message(message.chat.id, 'Para enviar uma reclamação, mande um email para reclamacao@blablabla.com')


@bot.message_handler(commands=["opcao3"])
def opcao3(message):
    bot.send_message(message.chat.id, 'Valeu! Edmarques mandou um abraço de volta.')


def verify(message):
    return True


@bot.message_handler(func=verify)
def answer(message):
    text = "Escolha uma opção para continuar (Clique no item):\n\n/opcao1 Fazer pedido\n/opcao2 Reclamar de um pedido\n/opcao3 Mardar um abraço pro Edmarques\n\nResponder qualquer outra coisa não vai funcionar, clique em uma das opções."

    bot.reply_to(message, text)


bot.polling()
