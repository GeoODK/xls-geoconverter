
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
import tempfile
import os
import csv
import xlsgeo
import zipfile
# Create your views here.

SERVER_TMP_DIR = '/tmp'



class UploadFileForm(forms.Form):
	file  = forms.FileField()
	#select_field = forms.ChoiceField(label='Select Geometry Type',choices=GEO_CHOIES)

def zipdir(path, zip):
	print path
	for root, dirs, files in os.walk(path):
		for file in files:
			print os.path.relpath(file)
			zip.write(os.path.join(root, file),os.path.relpath(file))

def handle_uploaded_file(f, temp_dir):
	file_path = os.path.join(temp_dir, f.name)
	destination = open(file_path, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	return file_path


def validate_form(uploaded_form):
	return True

def index(request):

	if(request.method =='POST'):
		## IF the form submited for for the upload
		if request.POST.get('formupload'):
			form = UploadFileForm(request.POST, request.FILES) # A form bound to the POST data
			if form.is_valid():
				temp_dir = tempfile.mkdtemp(dir=SERVER_TMP_DIR)
				file_path = handle_uploaded_file(request.FILES['file'], temp_dir)
				filename, ext = os.path.splitext(request.FILES['file'].name)
				errors = validate_form(file_path)
				try:
					schema = xlsgeo.get_file_schema(file_path)
					upload = True
				except:
					schema = []
					upload = False
				
				data = {
					'title':"XLS GeoConverter",
					'form':UploadFileForm(),
					'step':"2",
					'schema':schema,
					'file_path':file_path,
					'upload':upload,
					'errors': validate_form(file_path),

				}
				return render_to_response('index.html',data)
		else:
			file_path = request.POST['file_path']
			temp_dir = os.path.dirname(file_path)
			geometry_type = request.POST['geometry_type']
			geometry_field = request.POST['geometry_field']
			lat_field = request.POST['lat_field']
			lng_field = request.POST['lng_field']

			if geometry_type =='point':
				file_geo_field = [lat_field,lng_field]
			else:
				file_geo_field = geometry_field
			
			sp_file = xlsgeo.create_spatial_file(file_path,geometry_type,file_geo_field)
			if sp_file:
				zipf = zipfile.ZipFile(temp_dir+'/shape.zip', 'w')
				zipdir(temp_dir+"/shape", zipf)
				zipf.close()

			download_path = temp_dir+"/shape.zip"
			data = {
					'title':"XLS GeoConverter",
					'form':UploadFileForm(),
					'file_path':sp_file,
					'geometry_type':geometry_type,
					'geometry_field':file_geo_field,
					'download_path':download_path,
					'errors': True,
					'upload':True,
					'download':True,

				}
			return render_to_response('index.html',data)
	else:
		form = UploadFileForm() # An unbound form


	#template = loader.get_template('polls/index.html')
	#return HttpResponse("Hello World, You are on the polls index")
	return render_to_response('index.html', {
		'title': 'XLS GeoConverter',
		'step':"1",
		'form': form,
	})




def serve_files(request, path):
	fo = open(os.path.join(SERVER_TMP_DIR,path))
	data = fo.read()
	fo.close()
	response = HttpResponse(content_type='application/zip')
	#response['Content-Disposition'] = 'attachment; filename=somefilename.xml'
	response.write(data)
	return response

