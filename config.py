import json
import os
from decouple import config  # Importe a função config do módulo decouple

# Função para solicitar um valor ao usuário e validar a entrada
def solicitar_valor(mensagem, tipo=str, validacao=None):
    while True:
        valor = input(mensagem)
        if validacao is None or validacao(valor):
            try:
                # Tenta converter o valor para o tipo especificado
                valor = tipo(valor)
                return valor
            except ValueError:
                print("Entrada inválida. Certifique-se de fornecer um valor válido do tipo correto.")
        else:
            print("Entrada inválida.")

# Verifica se o arquivo settings.json já existe
if not os.path.exists('settings.json'):
    dados = {}
else:
    with open('settings.json', 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)

# Coleta e armazena cada campo de configuração que não existe nos dados
if 'NickDono' not in dados:
    dados['NickDono'] = solicitar_valor("Digite o Seu login telegram exemplo: @batmonn: ", str)

if 'logobot' not in dados:
    dados['logobot'] = solicitar_valor("Digite o caminho da imagem do logo do bot: ", str)

if 'tokentv' not in dados:
    dados['tokentv'] = solicitar_valor("Digite o token da API dos testes use esse aqui: tioefoda ", str)

if 'loginUrltv' not in dados:
    dados['loginUrltv'] = solicitar_valor("Digite o url do painel completa comece com http:// (com / no final): ", str)

if 'usernametv' not in dados:
    dados['usernametv'] = solicitar_valor("Digite o username do painel IPTV: ", str)

if 'passwordtv' not in dados:
    dados['passwordtv'] = solicitar_valor("Digite a senha do painel IPTV: ", str)

if 'server_ofc' not in dados:
    dados['server_ofc'] = solicitar_valor("Digite o IP do servidor SSH: ", str)

if 'senha_ofc' not in dados:
    dados['senha_ofc'] = solicitar_valor("Digite a senha do root do servidor SSH: ", str)

if 'apklink' not in dados:
    dados['apklink'] = solicitar_valor("Digite o link do aplicativo de internet: ", str)

# Salva os dados no arquivo settings.json
with open('settings.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)

# Lê o token do Telegram do arquivo .env usando a função config
token_telegram = config('TELEGRAM_BOT_TOKEN')

# Verifica se o token do Telegram foi definido
if token_telegram:
    # Executa o botteste.py passando o token como variável de ambiente
    os.environ['TELEGRAM_BOT_TOKEN'] = token_telegram
    os.system("python botteste.py")
else:
    print("Token do Telegram não encontrado. Verifique o arquivo .env.")
