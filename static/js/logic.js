// Creating map object
var myMap = L.map("map", {
  center: [ 36.778259, -119.417931],
  zoom: 5
});

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Query url
var url = "http://127.0.0.1:5000/data"


// Grab the data with d3
d3.json(url, function(response) {
  // console.log(response);
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();
  // Loop through data
  for (var i = 0; i < response.length; i++) {
    // Set the data location  to a variable
    var location = response[i].coordinates;

    // Check for location property
    if (location) {
      //Stripping location out of a list 
      var newLocation = JSON.parse(location.split("'").join(''));
      // console.log(newLocation);

      // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer(L.marker([newLocation[0], newLocation[1]])
      .bindPopup(response[i].name));
    }
  }
  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});
