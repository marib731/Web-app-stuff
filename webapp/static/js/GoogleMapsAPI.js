
var map, thePos, marker, infoWindow;
var i = 0;
var radarInterval;
var trafficLayer;
var timestamps = ['900913-m50m', '900913-m45m', '900913-m40m', '900913-m35m', '900913-m30m', '900913-m25m', '900913-m20m', '900913-m15m', '900913-m10m', '900913-m05m', '900913'];

function initMap() {
  console.log('initing map...')
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

// Turn on/off Weather Radar
$('#mapRadar').click(function(){
  
  if($(this).val() === 'Turn on Weather Radar'){
    i = 0;
    $(this).val('Turn off Weather Radar');
    radarInterval = setInterval(startAnimation, 500);
  }else{
    $(this).val('Turn on Weather Radar');
    clearInterval(radarInterval);
    map.overlayMapTypes.clear();
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

// Animate the Weather Radar
function startAnimation(){
    map.overlayMapTypes.clear();
    map.overlayMapTypes.push(null);
    tileNEX = new google.maps.ImageMapType({
      getTileUrl: function(tile, zoom) {
          return "https://mesonet.agron.iastate.edu/cache/tile.py/1.0.0/nexrad-n0q-" + timestamps[i] + "/" + zoom + "/" + tile.x + "/" + tile.y +".png"; 
      },
      tileSize: new google.maps.Size(256, 256),
      opacity:0.60,
      name : 'NEXRAD',
      isPng: true
    });
    map.overlayMapTypes.setAt("0", tileNEX);
  
    i++;
    if (i > 10 ){
      i = 0;
    }
}








