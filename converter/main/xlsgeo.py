# XLS GeoConverter
import csv
import csv
from shapely.geometry import Polygon,Point,LineString, mapping
from fiona import collection
import os
		
		
def get_file_schema(csv_file):
	schema = []
	with open(csv_file, 'rU') as geoFile:
		reader = csv.reader(geoFile)
		for row in reader:
			schema = row
			break
	return schema

def _convert_poly_to_point(geo):
	poly_dic = []
	if geo!="" or geo!='n/a' or geo!= 'null' or geo != 'none' or geo != None:
		poly_array =  geo.split(';')
		for i in poly_array:
			row = i.split(' ')
			if (len(row)>1):
				try:
					point = (float(row[1]),float(row[0]))
					poly_dic.append(point)
				except:
					continue
	return poly_dic

def _create_shp_path(directory):
	shape_dir = os.path.join(directory,"shape")
	if(os.path.exists(shape_dir)!= True):
		os.mkdir(shape_dir)
	return shape_dir

def build_point_shape(file_path,shapefile,schema,geometry_field):
	try:
		with collection(
	    	shapefile , "w", "ESRI Shapefile", schema) as output:
			    with open(file_path, 'rU') as f:
			        reader = csv.DictReader(f)
			        for row in reader:
			        	shape_props = build_schema_key_par(schema['properties'],row)
			        	try:
			        		lat = float(row[geometry_field[0]])
			        		lng = float(row[geometry_field[1]])
			        		point = Point(lng,lat)
				        	output.write({
				        		'properties': shape_props,
				        		'geometry': mapping(point)
				        	})
				        except:
				        	continue
	except:
		return False
	return True

def build_schema_key_par(schema,row):
	schema_key_pair = {}
	for s in schema:
		schema_key_pair[s] = row[s]
	return schema_key_pair

def build_polygon_shape(file_path,shapefile,schema,geometry_field):
	try:
		with collection(
	    	shapefile , "w", "ESRI Shapefile", schema) as output:
			    with open(file_path, 'rU') as f:
			        reader = csv.DictReader(f)
			        for row in reader:
			        	shape_props = build_schema_key_par(schema['properties'],row)
			        	x = _convert_poly_to_point(row[geometry_field])
			        	if x:
				        	poly = Polygon(x)
				        	output.write({
				        		'properties': shape_props,
				        		'geometry': mapping(poly)
				        	});
	except:
		return False

	return True

def build_polyline_shape(file_path,shapefile,schema,geometry_field):
	try:
		with collection(
	    	shapefile , "w", "ESRI Shapefile", schema) as output:
			    with open(file_path, 'rU') as f:
			        reader = csv.DictReader(f)
			        for row in reader:
			        	shape_props = build_schema_key_par(schema['properties'],row)
			        	x = _convert_poly_to_point(row[geometry_field])
			        	if x:
				        	poly = LineString(x)
				        	output.write({
				        		'properties': shape_props,
				        		'geometry': mapping(poly)
				        	});
	except:
		return False

	return True

def create_spatial_file(file_path,geometry_type,geometry_field):
	directory = os.path.dirname(file_path)
	file_name = os.path.basename(file_path).split('.')[0]
	shape_path = _create_shp_path(directory)
	shapefile = os.path.join(shape_path,file_name)+".shp"
	print 'Directory: ',directory
	print 'File Name: ',file_name
	print 'Shape_Path: ',shape_path
	print 'Shape_File:', shapefile

	colms =  get_file_schema(file_path)
	props = {}
	##### Settings for Point #######
	if geometry_type == 'point':
		for row in colms:
			props[row]='str'
		schema = { 'geometry': 'Point', 'properties': props }
		build = build_point_shape(file_path,shapefile,schema,geometry_field)

	##### Settings for  #######
	if geometry_type == 'polygon':
		for row in colms:
			if row != geometry_field:
				props[row]='str'
		schema = { 'geometry': 'Polygon', 'properties': props }
		build = build_polygon_shape(file_path,shapefile,schema,geometry_field)

	if geometry_type == 'polyline':
		for row in colms:
			if row != geometry_field:
				props[row]='str'
		schema = { 'geometry': 'LineString', 'properties': props }
		build = build_polyline_shape(file_path,shapefile,schema,geometry_field)


	if build==False:
		error = True
		print "error"
	else:
		print "success"

	return shapefile

# def _Test_Point():
# 	file_path = '/vagrant/Data/Point_Test_Data.csv'
# 	geometry_type ='point'
# 	geometry_field = ['location:Latitude','location:Longitude']
# 	shapeFile = create_spatial_file(file_path,geometry_type,geometry_field)
# 	return "sds"
# def _Test_Poylgon():
# 	file_path = '/vagrant/Data/Polygon_Test_Data.csv'
# 	geometry_type ='polygon'
# 	geometry_field = 'location/trace'
# 	shapeFile = create_spatial_file(file_path,geometry_type,geometry_field)
# 	return "sd"
# def _Test_Polyline():
# 	file_path = '/vagrant/Data/Polygon_Test_Data.csv'
# 	geometry_type ='polyline'
# 	geometry_field = 'location/trace'
# 	shapeFile = create_spatial_file(file_path,geometry_type,geometry_field)
# 	return "sds"

# def main():
# 	_Test_Polyline()
# 	# file_path = '/vagrant/tmp/tmp3BihVD/land_tenure_survey_2015_02_28_07_36_00.csv'
# 	# geometry_type ='polygon'
# 	# geometry_field = 'location/trace'
# 	# x = create_spatial_file(file_path,geometry_type,geometry_field)
# if __name__ == '__main__':
# 	main()











