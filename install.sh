##vagrant init hashicorp/precise32
sudo apt-get update
sudo apt-get install -y python-software-properties
sudo add-apt-repository -y ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get install -y python-dev

sudo apt-get install -y libgdal1-dev
sudo apt-get install -y libgdal-dev
sudo apt-get install -y g++
sudo apt-get install -y python-gdal
sudo apt-get install -y python-pip

sudo apt-get update

sudo pip install shapely
sudo pip install six
sudo pip install cligj
sudo pip install argparse
sudo pip install ordereddict
sudo pip install fiona
sudo pip install Django==1.8
