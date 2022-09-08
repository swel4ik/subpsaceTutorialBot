import telebot
from telebot import types

bot = telebot.TeleBot("5384669677:AAHepwAcMJWbcoesDOtC3jiqzty3ztsbGR8")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    install_key = types.InlineKeyboardButton(text='📡Set up your nodes📡', callback_data='set_up')
    requirements_key = types.InlineKeyboardButton(text='🛠Machine requirements🛠', callback_data='req')
    faq_key = types.InlineKeyboardButton(text='❓FAQ❓', callback_data='faq')
    keyboard.add(install_key)
    keyboard.add(requirements_key)
    keyboard.add(faq_key)
    bot_mes = 'What do you interested in?'
    bot.send_message(message.from_user.id, text=bot_mes, reply_markup=keyboard)


    # key_docker = types.InlineKeyboardButton(text='Docker', callback_data='docker')  # кнопка «Да»
    # keyboard.add(key_docker)  # добавляем кнопку в клавиатуру
    # key_linux = types.InlineKeyboardButton(text='Linux', callback_data='linux')
    # keyboard.add(key_linux)
    # bot_mes = 'Choose installation type:'
    # bot.send_message(message.from_user.id, text=bot_mes, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message != '/start' or message != '/help':
        bot.reply_to(message, "Write /start for bot activation")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'set_up':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_docker = types.InlineKeyboardButton(text='Docker', callback_data='docker')  # кнопка «Да»
        keyboard.add(key_docker)  # добавляем кнопку в клавиатуру
        key_linux = types.InlineKeyboardButton(text='Linux (CLI)', callback_data='linux')
        keyboard.add(key_linux)
        key_windows = types.InlineKeyboardButton(text='Windows (PowerShell)', callback_data='windows')
        keyboard.add(key_windows)
        bot_mes = 'Choose the installation type:'
        bot.send_message(call.message.chat.id, text=bot_mes, reply_markup=keyboard)

    if call.data == 'req':
        bot_mes = "CPU: 2 Core+\nRAM: 4GB+(Rec. 8GB)\nStorage: 150 GB"
        bot.send_message(call.message.chat.id, bot_mes)

    elif call.data == "docker":
        keyboard = types.InlineKeyboardMarkup()
        docker_1 = types.InlineKeyboardButton(text='Step 0: Requirements | Wallet', callback_data='0')  # кнопка «Да»
        keyboard.add(docker_1)
        docker_2 = types.InlineKeyboardButton(text='Step 1: Installing necessary server tools', callback_data='1')
        keyboard.add(docker_2)
        docker_3 = types.InlineKeyboardButton(text='Step 2: Check | Open necessary TCP ports', callback_data='2')
        keyboard.add(docker_3)
        docker_4 = types.InlineKeyboardButton(text='Step 3: Configure your config', callback_data='3')
        keyboard.add(docker_4)
        docker_5 = types.InlineKeyboardButton(text='Step 4: Set up and run your nodes', callback_data='4')
        keyboard.add(docker_5)
        bot_mes = 'Choose the installation step:'
        bot.send_message(call.message.chat.id, text=bot_mes, reply_markup=keyboard)

    elif call.data == '0':
        markdown = """
        *First, make sure that your system corresponds to requirements:*
        - CPU: 2 Core+
        - RAM: 4GB+(Rec. 8GB)
        - Storage: 150 GB
        
        *Wallets*
        Before running anything you need to have a wallet where you'll receive testnet coins. 
        There are currently two wallets we suggest using, *SubWallet* being the preferred route.
        - [SubWallet](https://subwallet.app/)
        - [PolkadotJS](https://polkadot.js.org/extension/)
        Install one of the two wallets above into your browser and create a new account there or you can use your address from previous stress-test. The address of your account will be necessary at the last step.
        """

        markdown_2 = """
        *For PolkadotJS wallet*
        To get the wallet address, go to https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Feu-2.gemini-2a.subspace.network%2Fws#/accounts and click on the icon
        """
        img = open('polka.png', 'rb')

        bot.send_message(call.message.chat.id, markdown, parse_mode="Markdown")
        bot.send_message(call.message.chat.id, markdown_2, parse_mode="Markdown")
        bot.send_photo(call.message.chat.id, img)

    elif call.data == '1':
        markdown = """
        *Update and install useful tools, copy and past this command into your terminal:*
        ```
        sudo apt update && sudo apt install mc wget htop jq git curl -y
        ```
*Install Docker, copy and past this command into your terminal:*
        ```
        curl -s https://raw.githubusercontent.com/razumv/helpers/main/tools/install_docker.sh | bash
        ```
        """
        bot.send_message(call.message.chat.id, markdown, parse_mode="Markdown")

    elif call.data == '2':
        markdown = """
        Currently, TCP port `30333` and `40333` needs to be exposed for node to work properly.
If you have a server with no firewall, there is nothing to be done, but otherwise make sure to open TCP ports `30333` and `40333` for incoming connections.
        
Check these ports on your machine with following commands:
        ```
        sudo iptables -L | grep 30333
        sudo iptables -L | grep 40333
        ```
If there is nothing showed in terminal open the port if not open:
```
sudo iptables -A INPUT -p tcp --dport 30333 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 40333 -j ACCEPT
```
Rerun the check commands to be ensure that you've opened the ports
        """
        bot.send_message(call.message.chat.id, markdown, parse_mode="Markdown")

    elif call.data == '3':
        markdown = """
            *Fill the necessary info: replace examples in quotes on your own and past into terminal*
`REWARD_WALLET_ADDRESS="YOUR_WALLET_ADDRESS"` - your own wallet address from Step 0
`NODE_NAME="YOUR_NODE_NAME"` - desired name that will be shown in telemetry (doesn't impact anything else)
`FARMER_PLOT_SIZE="100G"` - you can set lesser value, but maximum for this stress-test is 100G
`SUBSPACE_RELEASE="LATEST_RELEASE_NAME"` - the latest release; in the following format example: `snapshot-2022-apr-29`
*Save the variables, reload the `.bash_profile` and check:*
```
echo "export REWARD_WALLET_ADDRESS="${REWARD_WALLET_ADDRESS}"" >> $HOME/.bash_profile
echo "export NODE_NAME="${NODE_NAME}"" >> $HOME/.bash_profile
echo "export FARMER_PLOT_SIZE="${FARMER_PLOT_SIZE}"" >> $HOME/.bash_profile
echo "export SUBSPACE_RELEASE="${SUBSPACE_RELEASE}"" >> $HOME/.bash_profile

source $HOME/.bash_profile

echo -e "REWARD_WALLET_ADDRESS > ${REWARD_WALLET_ADDRESS}"
echo -e "NODE_NAME > ${NODE_NAME}"
echo -e "FARMER_PLOT_SIZE > ${FARMER_PLOT_SIZE}"
echo -e "SUBSPACE_RELEASE > ${SUBSPACE_RELEASE}"
```
            
❗️❗️❗️You can check the latest release with this link: https://github.com/subspace/subspace/releases
            """
# TODO success screen
        release_mes = 'Example of latest release (you should copy the name in red square): ⤵'
        release_img = open('Screenshot_12.png', 'rb')


        bot.send_message(call.message.chat.id, markdown, parse_mode="Markdown")
        bot.send_message(call.message.chat.id, release_mes)

        bot.send_photo(call.message.chat.id, release_img)

    elif call.data == '4':
        markdown = """
        Here is the final step!
*Create `subspace` dir and pull the config:*
        ```
        cd ~
        mkdir subspace && cd subspace
        wget https://raw.githubusercontent.com/swel4ik/subspace_docker_config/main/docker-compose.yml
        ```
*Run your nodes!*
`docker-compose up -d`
        """
        bot.send_message(call.message.chat.id, markdown, parse_mode="Markdown")

    elif call.data == "linux":
        bot.send_message(call.message.chat.id, "Ok, let's try!")


bot.infinity_polling()
