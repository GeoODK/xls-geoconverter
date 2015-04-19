$( document ).ready(function() {
	// $('#createshape').click(function(){
	// 	validate_form();
	// })

	$("#geometry_type").change(function(evt){

		clearFields();
		$('#geometry_type_box').removeClass('has-error');
		var field = $("#geometry_type").val();
		var geo_box = $("#geometry_field_box");
		if(field =="point"){
			$('#geo_point').css('display','block')
			$('#geo_shape').css('display','none');
		}else if(field =="polyline" ||field =="polygon"){
			$('#geo_point').css('display','none')
			$('#geo_shape').css('display','block');
		}else{
			$('#geo_point').css('display','none');
			$('#geo_shape').css('display','none');
		}
	});
});

function clearFields(){
	document.getElementById("lat_field").options[0].selected="selected";
	document.getElementById("lng_field").options[0].selected="selected";
	document.getElementById("geometry_field").options[0].selected="selected";
	$('#lat_field_box').removeClass('has-error');
	$('#lng_field_box').removeClass('has-error');
	$('#geo_shape').removeClass('has-error');
	$('#errorList').html("");
}

function validate_form(){

	fields= $('#createshapeform').serializeArray();
	geometry_type = fields[1]['value'];
	var errors = false;
	if(geometry_type =="none"){
		$('#geometry_type_box').addClass('has-error');
		errors = true;
	}else{
		if (geometry_type =='point'){
			// Get Values
			lat_field = $('#lat_field').val();
			lng_field = $('#lng_field').val();
			//Clear any error classes
			$('#lat_field_box').removeClass('has-error');
			$('#lng_field_box').removeClass('has-error');
			
			if (lat_field =="none" || lng_field =="none"){
				errors = true;
				$('#lat_field_box').addClass('has-error');
				$('#lng_field_box').addClass('has-error');
			}
		}else{
			//Its an polyline or a polygon
			$('#geo_shape').removeClass('has-error');
			var geometry_field = $('#geometry_field').val();
			if (geometry_field =="none"){
				// The value is none
				errors = true;
				$('#geo_shape').addClass('has-error');
			}
		}
	}
	if(errors ==true){
		$('#errorList').html("<li>Error has Occured</li>");
		return false;
	}else{
		return true;
	}
}