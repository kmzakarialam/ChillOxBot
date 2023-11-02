# @km-zakaria-alam-akib

if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/km-zakaria-alam-akib/ChillOxBot.git /ChillOxBot 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ChillOxBot 
fi
cd /ChillOxBot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
