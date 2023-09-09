import json
import requests
import telebot
from datetime import datetime
from telebot import types
from decouple import config  # Importe a função config do módulo decouple

# Carregar configurações do JSON
with open('./settings.json', encoding='utf-8') as settings_file:
    settings = json.load(settings_file)

# Lê o token do Telegram do arquivo .env usando a função config
token_telegram = config('TELEGRAM_BOT_TOKEN')

# Verifica se o token do Telegram foi definido no arquivo .env
if not token_telegram:
    raise Exception("Token do Telegram não encontrado. Verifique o arquivo .env.")

# Inicializar o bot
bot = telebot.TeleBot(token_telegram, parse_mode=None)

# ... restante do seu código ...

# Ações de callback
TEST_IPTV_ACTION = 'teste_iptv1'
SOBRE_ACTION = 'sobre'
TEST_NET_ACTION = 'testnet'

# Dicionário para armazenar os últimos horários de solicitação de teste dos usuários
last_test_requests = {"iptv": {}, "net": {}}

# Tratador do comando /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    photo = settings["logobot"]
    caption = f"BEM-VINDO(A) 𝗕𝗢𝗧 𝗧𝗘𝗦𝗧𝗘 𝗜𝗣𝗧𝗩 𝗘 𝗜𝗡𝗧𝗘𝗥𝗡𝗘𝗧\n\n"
    keyboard = [
        [types.InlineKeyboardButton("📺 TESTE TV", callback_data=TEST_IPTV_ACTION)],
        [types.InlineKeyboardButton("📱 TESTE SSH", callback_data=TEST_NET_ACTION)],
        [types.InlineKeyboardButton("📺 SOBRE O BOT", callback_data=SOBRE_ACTION)],
    ]
    reply_markup = types.InlineKeyboardMarkup(keyboard)
    bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=reply_markup)

# Tratador de consulta de callback
@bot.callback_query_handler(func=lambda query: True)
def callback_query(query):
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    action = query.data

    # Verifica se o usuário solicitou um teste no último mês para cada tipo de teste
    now = datetime.now()
    iptv_last_request = last_test_requests["iptv"].get(user_id)
    net_last_request = last_test_requests["net"].get(user_id)

    if iptv_last_request and (now - iptv_last_request).days < 30 and action == TEST_IPTV_ACTION:
        bot.send_message(chat_id=chat_id, text="𝗣𝗔𝗣𝗔 𝗧𝗘𝗦𝗧𝗘 𝗡𝗔 𝗔𝗥𝗘𝗔!!!!! 𝗩𝗢𝗖𝗘̂ 𝗝𝗔 𝗣𝗘𝗚𝗢𝗨 𝗧𝗘𝗦𝗧𝗘 𝗥𝗔𝗣𝗢𝗦𝗔 𝗩𝗢𝗟𝗧𝗔 𝗠𝗘𝗦 𝗤𝗨𝗘 𝗩𝗘𝗠 𝗘́ 𝟭 𝗣𝗢𝗥 𝗠𝗘𝗦")
        return
    elif net_last_request and (now - net_last_request).days < 30 and action == TEST_NET_ACTION:
        bot.send_message(chat_id=chat_id, text="𝗣𝗔𝗣𝗔 𝗧𝗘𝗦𝗧𝗘 𝗡𝗔 𝗔𝗥𝗘𝗔!!!!! 𝗩𝗢𝗖𝗘̂ 𝗝𝗔 𝗣𝗘𝗚𝗢𝗨 𝗧𝗘𝗦𝗧𝗘 𝗥𝗔𝗣𝗢𝗦𝗔 𝗩𝗢𝗟𝗧𝗔 𝗠𝗘𝗦 𝗤𝗨𝗘 𝗩𝗘𝗠 𝗘́ 𝟭 𝗣𝗢𝗥 𝗠𝗘𝗦")
        return

    if action == TEST_IPTV_ACTION:
        api_url = f"http://api.revenda3ssh.tk:8080/api?type=iptv1&token={settings['tokentv']}&query=teste&loginUrltv={settings['loginUrltv']}&usernametv={settings['usernametv']}&passwordtv={settings['passwordtv']}"
        bot.send_message(chat_id=chat_id, text="𝗔𝗴𝘂𝗮𝗿𝗱𝗲, 𝘁𝗲𝘀𝘁𝗲 𝘀𝗲𝗻𝗱𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗮𝗱𝗼...")
        
        response = requests.get(api_url)
        data = response.json()
        
        if "resultado" in data:
            resultado = data["resultado"].replace('*', '')
            bot.send_message(chat_id=chat_id, text=f"Resultados da consulta:\n{resultado}")
            last_test_requests["iptv"][user_id] = now  # Armazena o horário da solicitação do teste
        else:
            bot.send_message(chat_id=chat_id, text="Não foram encontrados resultados.")

    elif action == SOBRE_ACTION:
        sobre_message = f"CHAME MEU DONO {settings['NickDono']}"
        bot.send_message(chat_id=chat_id, text=sobre_message)

    elif action == TEST_NET_ACTION:
        api_url = f"http://api.revenda3ssh.tk:8080/api?type=ssh&token={settings['tokentv']}&query=teste&server_ofc={settings['server_ofc']}&senha_ofc={settings['senha_ofc']}"
        bot.send_message(chat_id=chat_id, text="𝗔𝗴𝘂𝗮𝗿𝗱𝗲, 𝘁𝗲𝘀𝘁𝗲 𝘀𝗲𝗻𝗱𝗼 𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗮𝗱𝗼...")

        response = requests.get(api_url)
        data = response.json()
        
        if "resultado" in data:
            resultado = data["resultado"].replace('*', '')
            bot.send_message(chat_id=chat_id, text=f"Resultados da consulta:\n{resultado}\nBaixe o app {settings['apklink']}")
            last_test_requests["net"][user_id] = now  # Armazena o horário da solicitação do teste
        else:
            bot.send_message(chat_id=chat_id, text="Não foram encontrados resultados.")

print('BOT SYKYNED TESTE ONLINE @batmonn ✅!!!')

# Iniciar a captura de comandos
bot.polling(none_stop=True)
