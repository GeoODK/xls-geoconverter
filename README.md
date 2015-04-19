# XLS GeoConverter

This is a Django web interface for converting data collected with GeoODK Collect/ODK Collect to a geographical format. In the XLSForm there are three main geographical formats 

To learn about XLSForms visit [http://xlsform.org/](http://xlsform.org/)

## Spatial Data Type:
* geopoint (point)
* geoshape (polygon)
* geotrace (polyline)

This tool is for assisting with the “.csv” export formats of ODK Aggregate, Formhub and Ona.io. Once the data has been collected you can use this tool to convert your data into a ESRI shapefile.


## Try it out:
[http://geoodk.com/geoconverter](http://geoodk.com/geoconverter)


## Question

[Geoodk Community](https://groups.google.com/forum/#!forum/geoodk-community)

[Geoodk Developers](https://groups.google.com/forum/#!forum/geoodk-developers)

For question 
## Install 
If you are using Vagrant  for testing, pull the repo and run

	vagrant up
    
    
In the Vagrant file you will notice that it runs the install.sh

	config.vm.provision :shell, path: "install.sh"
 
Run Django setup

	python manage.py syncdb --noinput
	
	python manage.py migrate
	
	python manage.py runserver
    
If you are installing directly on your a server check out the install.sh.
The install.sh script includes:

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

## Notes

The Django app use shapely and Fiona, to learn more about these see:
	
    Shapely:
	https://pypi.python.org/pypi/Shapely
    
    Fiona:
    https://github.com/Toblerity/Fiona
    
 View them used together [http://www.macwright.org/2012/10/31/gis-with-python-shapely-fiona.html](http://www.macwright.org/2012/10/31/gis-with-python-shapely-fiona.html)
