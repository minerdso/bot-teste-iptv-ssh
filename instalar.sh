#!/bin/bash

# Função para exibir o título em letras grandes
function exibir_titulo {
    clear
    echo " _______  _______  _______  _______  ______  _____    ______  _______  _______ "
    echo "|   |   ||_     _||    |  ||    ___||   __ \|     \  |   __ \|       ||_     _|"
    echo "|       | _|   |_ |       ||    ___||      <|  --  | |   __ <|   -   |  |   |  "
    echo "|__|_|__||_______||__|____||_______||___|__||_____/  |______/|_______|  |___|  "
    echo ""
}

# Exibe o título
exibir_titulo

# Função para verificar se um pacote está instalado
verificar_pacote() {
    pacote=$1
    if ! dpkg -l | grep -q $pacote; then
        return 1  # Pacote não está instalado
    else
        return 0  # Pacote está instalado
    fi
}

# Verificar se as dependências estão instaladas
if verificar_pacote "python3" && verificar_pacote "python3-pip"; then
    echo "As dependências já estão instaladas."
else
    echo "Instalando as dependências..."
    # Atualizar o sistema
    sudo apt-get update

    # Instalar o Python (substitua o comando abaixo pelo comando correto para sua distribuição)
    sudo apt-get install -y python3

    # Instalar o gerenciador de pacotes Python pip
    sudo apt-get install -y python3-pip
fi

# Instalar as dependências do bot usando o pip
pip3 install telebot requests python-decouple

# Clone o repositório do bot
git clone https://github.com/minerdso/bot-teste-iptv-ssh.git

# Acesse a pasta do bot
cd bot-teste-iptv-ssh

# Instala as dependências Python
pip3 install pyTelegramBotAPI requests requests python-decouple

# Executa o script de configuração interativamente
python config.py

# Iniciar o bot
python botteste.py

# Menu de opções
echo "Selecione uma opção:"
echo "1. Instalar"
echo "0. Sair"

# Solicita a escolha do usuário
read -p "Digite o número da opção desejada: " opcao

# Realiza a ação com base na escolha do usuário
case $opcao in
    1)
    echo "Iniciando a instalação..."
    # Coloque aqui os comandos para a instalação do bot, se necessário.
    ;;
    0)
    echo "Saindo..."
    ;;
    *)
    echo "Opção inválida."
    ;;
esac
