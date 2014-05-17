var POI_URL = "http://10.0.1.54:8080/ams/";
//var POI_URL = "data.json";
var TWITTER_ENDPOINT="http://10.0.1.54:8080/ams/tweets/";
function getPOIs(latitude, longitude, callback){
	var latLngDetails = latitude + ',' + longitude;
	$.ajax({
		type: "GET",
		url: POI_URL,
		dataType: "json",
		crossDomain : true,
		// jsonp:'jsonp',
		data: { ll: latLngDetails, categories:'food'  },
		success: function(data, textStatus, jqXHR) {
			callback(true, data);
		},
		error: function(err) {
			callback(false, err);
		}
	});
}

function getTweets(latitude, longitude, callback){
	var latLngDetails = latitude + ',' + longitude;
	$.ajax({
		type: "GET",
		url: TWITTER_ENDPOINT,
		dataType: "json",
		crossDomain : true,
		// jsonp:'jsonp',
		data: { ll: latLngDetails},
		success: function(data, textStatus, jqXHR) {
			callback(true, data);
		},
		error: function(err) {
			callback(false, err);
		}
	});
}