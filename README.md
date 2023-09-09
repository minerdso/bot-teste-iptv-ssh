# Bot de Teste IPTV e NET

Este bot permite que os usuários gerem testes para serviços IPTV e NET e recebam os resultados em seus chats no Telegram. Ele é desenvolvido em Python e utiliza a biblioteca `pyTelegramBotAPI` para interagir com o Telegram.

## Funcionalidades

- Teste de IPTV: Os usuários podem solicitar um teste de IPTV para verificar a disponibilidade dos canais e a qualidade da transmissão.
- Teste de NET: Os usuários podem solicitar um teste de NET para verificar a conectividade e a velocidade da internet.
- Geração de Testes: O bot se comunica com uma API externa para gerar testes e retorna os resultados para o usuário.
- Configurações Personalizadas: Os administradores do bot podem configurar informações como tokens, URLs e credenciais para os testes.

## Pré-requisitos
Certifique-se de ter os seguintes pré-requisitos instalados:

Python 3
pip (gerenciador de pacotes Python)
Git (opcional, apenas se você desejar clonar o repositório do bot)
Painéis Compatíveis com a API (Opainel e Koffice)
Certifique-se de ter acesso e informações de configuração para os painéis Opainel e Koffice, pois você precisará delas para configurar o bot corretamente.

Isso ajudará os usuários a entenderem quais sistemas são compatíveis com a API e quais informações podem ser necessárias durante a configuração do bot. Certifique-se de fornecer detalhes suficientes sobre como obter e configurar essas informações, se possível.

## Instalação

1. Clone este repositório (opcional):

```bash
git clone https://github.com/minerdso/bot-teste-iptv-ssh.git
cd bot-teste-iptv-ssh
```

2. Instale as dependências Python:

```bash
pip3 install pyTelegramBotAPI requests python-decouple
```

3. Execute o script de configuração interativamente para configurar seu bot:

```bash
python config.py
```

4. Inicie o bot:

```bash
python botteste.py
```

## Uso

- Inicie uma conversa com o bot no Telegram.
- Use o comando `/start` para acessar o menu principal.
- Selecione "📺 TESTE TV" para solicitar um teste de IPTV.
- Selecione "📱 TESTE SSH" para solicitar um teste de NET.
- Siga as instruções do bot para fornecer informações adicionais, como URLs e credenciais, se solicitado.
- Aguarde o resultado do teste que será enviado pelo bot.

## Configuração Personalizada

Os administradores do bot podem personalizar as configurações editando o arquivo `settings.json` no diretório do bot. Este arquivo contém informações como tokens, URLs e credenciais para os testes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de recebimento (pull requests) para melhorias ou correções.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---

Espero que este README.md seja útil para você. Você pode personalizá-lo de acordo com suas necessidades e adicionar informações adicionais sobre o bot e suas funcionalidades. Se precisar de mais ajuda ou tiver alguma dúvida, sinta-se à vontade para perguntar.
