
var map, thePos, marker, infoWindow;
var i = 0;
var radarInterval;
var trafficLayer;
var timestamps = ['900913-m50m', '900913-m45m', '900913-m40m', '900913-m35m', '900913-m30m', '900913-m25m', '900913-m20m', '900913-m15m', '900913-m10m', '900913-m05m', '900913'];

function initMap() {
  
    // Set Variables
    trafficLayer = new google.maps.TrafficLayer();
    infoWindow = new google.maps.InfoWindow();
  
    // Center for map
    thePos = {lat: 53.3498, lng: -6.2603};
    
    // Create map
    map = new google.maps.Map($('#map')[0], {
      zoom: 12,
      center: thePos
    });
    
    // Create markers
   //checkbox filters here - eventlistener 
    marker = new google.maps.Marker({
      position: thePos,
      map: map
    });
    
    
}

// Handle errors for locating user
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
    'Error: The Geolocation service failed.' :
    'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}


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


