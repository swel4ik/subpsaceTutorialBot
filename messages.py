import requests
import json
from datetime import datetime, timezone


class BotMessages:

    def __init__(self):
        """Constructor"""
        req = requests.get('https://api.github.com/repos/subspace/subspace/releases')
        data = json.loads(req.text)
        self.current_release = data[0]['tag_name']
        self.current_date = datetime.now(timezone.utc).date()
        self.docker_messages = {

            'Step_0_0':

                """
*First, make sure that your system corresponds to requirements:*
- CPU: 2 Core+ (Rec. 4GB+)
- RAM: 4GB+(Rec. 8GB)
- Storage: 150GB+ (Rec. 170GB SSD)

*Wallets*
Before running anything you need to have a wallet where you'll receive testnet coins. 
There are currently two wallets we suggest using, *SubWallet* being the preferred route.
- [SubWallet](https://subwallet.app/)
- [PolkadotJS](https://polkadot.js.org/extension/)
Install one of the two wallets above into your browser and create a new account there or you can use your address from previous stress-test. The address of your account will be necessary at the last step.
""",

            'Step_0_1':

                """
*For PolkadotJS wallet*
To get the wallet address, go to https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Feu-2.gemini-2a.subspace.network%2Fws#/accounts and click on the icon
""",

            'Step_1':

                """
*Update and install useful tools, copy and past this command into your terminal:*
```
sudo apt update && sudo apt install mc wget htop jq git curl -y
```
*Install Docker, copy and past this command into your terminal:*
```
curl -s https://raw.githubusercontent.com/razumv/helpers/main/tools/install_docker.sh | bash
```
 """,

            'Step_2':

                """
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
""",

            'Step_3_0':

                """
*Fill the necessary info: replace examples in quotes on your own and past into terminal*
`REWARD_WALLET_ADDRESS="YOUR_WALLET_ADDRESS"` - your own wallet address from Step 0
`NODE_NAME="YOUR_NODE_NAME"` - desired name that will be shown in telemetry (doesn't impact anything else)
`FARMER_PLOT_SIZE="100G"` - you can set lesser value, but maximum for this stress-test is 100G
`SUBSPACE_RELEASE="LATEST_RELEASE_NAME"` - the latest release;
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
""",
            'Step_3_1': f'''The latest release for `{self.current_date}` (UTC): 
`{self.current_release}`''',

            'Step_4':

                """
Here is the final step!
*Create `subspace` dir and pull the config:*
        ```
cd ~ && mkdir subspace && cd subspace
wget https://raw.githubusercontent.com/swel4ik/subspace_docker_config/main/docker-compose.yml
        ```
*Run your nodes!*
`docker-compose up -d`
""",
            'logs':

                """
*To check the node logs run the command:*
`docker-compose -f $HOME/subspace/docker-compose.yml logs -f --tail=100 node`

*To check the farmer logs run the command:*
`docker-compose -f $HOME/subspace/docker-compose.yml logs -f --tail=100 farmer`

*To restart a subspace node:*
`docker-compose -f $HOME/subspace/docker-compose.yml restart node`

*To restart a subspace farmer:*
`docker-compose -f $HOME/subspace/docker-compose.yml restart farmer`

*To stop node and farmer:*
`docker-compose -f $HOME/subspace/docker-compose.yml down -v`
""",

            'Docker_update':

                f"""
*First stop your nodes:*
`docker-compose -f $HOME/subspace/docker-compose.yml down -v`
*Change subspace release:*
`echo "export SUBSPACE_RELEASE="{self.current_release}"" >> $HOME/.bash_profile`
*Update profile:*
`source $HOME/.bash_profile`
*Run your nodes:*
`cd $HOME/subspace && docker-compose up -d`
"""
        }
