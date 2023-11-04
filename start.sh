if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/RJMALLU/RT /RT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RT
fi
cd /RT
pip3 install -U -r requirements.txt
echo "Starting RT...."
python3 bot.py
