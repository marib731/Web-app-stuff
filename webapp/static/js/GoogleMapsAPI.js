var i = 0;
var timestamps = ['900913-m50m', '900913-m45m', '900913-m40m', '900913-m35m', '900913-m30m', '900913-m25m', '900913-m20m', '900913-m15m', '900913-m10m', '900913-m05m', '900913'];


/*********************************create map on index.html*******************************************/
var map, thePos, marker, infoWindow;
var trafficLayer;
function initMap() {
    // Set Variables from google api for bike lanes, traffic, and pop up when marker clicked
    trafficLayer = new google.maps.TrafficLayer();
    infowindow = new google.maps.InfoWindow();
    bikeLayer = new google.maps.BicyclingLayer();
    // Center for map
    thePos = {lat: 53.3498, lng: -6.2603};
    // Create map
    map = new google.maps.Map($('#map')[0], {
      zoom: 13,
      center: thePos
    });
    // Create markers
    fetch('/api/JCD')
      .then(function(response) {
        //check the response was ok
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + response.status);
            return;
        }
        //response ok, get lat and long for each station
        response.json().then((data) => {
            for (var item in data) {
                    var StationLat = data[item]['latitude'];
                    var StationLng = data[item]['longitude'];
                    var stationStatus = data[item]['status'];
                    var stationBikes = data[item]['bikes'];
                    var stationStands = data[item]['stands'];
                    var stationName = data[item]['name'];
                    
                
                    //contents of info window / pop up for each marker    
                    var contentString = '<h3>' + stationName + '</h3><ul><li>Status: ' + stationStatus + '</li><li>Available Bikes: ' + stationBikes + '</li><li>Available Stands: ' + stationStands + '</li></ul>';
                
                    //choose which image for the marker
                    var image; 
                    if (stationBikes < 1){
                        var image = {url:'/static/image/bike-out.png', scaledSize: new google.maps.Size(35, 35)};
                    }
                    else if(stationBikes <= 5){
                        var image = {url:'/static/image/bike-low.png', scaledSize: new google.maps.Size(35, 35)};
                    }
                    else{
                        var image = {url:'/static/image/bike-full.png', scaledSize: new google.maps.Size(35, 35)};
                    }
                    //create the marker
                    marker = new google.maps.Marker({
                        position: {lat: StationLat, lng: StationLng},
                        map: map,
                        icon: image
                    });
                marker.content = '<h3>' + stationName + '</h3><ul><li>Status: ' + stationStatus + '</li><li>Available Bikes: ' + stationBikes + '</li><li>Available Stands: ' + stationStands + '</li></ul>';


                    //on click, open info window / pop up for marker                                  
                    google.maps.event.addListener(marker, 'click', function() {
                    infowindow.setContent(this.content);
                    infowindow.open(map,marker);

 });
      }
        
        //if error along way, catch and show in console
        }).catch((err) => {
            console.log('Fetch Error :-S', err)
        })
    })
}

/*********************************end of made map*******************************************/



/*********************************buttons for map*******************************************/
// Turn on/off Bicycle Lanes
$('#mapBike').click(function(){
  
  if($(this).val() === 'Turn on Bike Lanes'){
    $(this).val('Turn off Bike Lanes');
    bikeLayer.setMap(map)
  } else{
    $(this).val('Turn on Bike Lanes');
    bikeLayer.setMap(null);
  }
  
})


// Turn on/off Traffic
$('#mapTraffic').click(function(){
  
  if($(this).val() === 'Turn on Traffic'){
    $(this).val('Turn off Traffic');
    trafficLayer.setMap(map)
  } else{
    $(this).val('Turn on Traffic');
    trafficLayer.setMap(null);
  }
  
})




