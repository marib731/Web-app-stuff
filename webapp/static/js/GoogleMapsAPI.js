
var map, thePos, marker, infoWindow;
var i = 0;
var radarInterval;
var trafficLayer;
var timestamps = ['900913-m50m', '900913-m45m', '900913-m40m', '900913-m35m', '900913-m30m', '900913-m25m', '900913-m20m', '900913-m15m', '900913-m10m', '900913-m05m', '900913'];

function initMap() {
    // Set Variables
    trafficLayer = new google.maps.TrafficLayer();
    infoWindow = new google.maps.InfoWindow();
    bikeLayer = new google.maps.BicyclingLayer();
  
    // Center for map
    thePos = {lat: 53.3498, lng: -6.2603};
    
    // Create map
    map = new google.maps.Map($('#map')[0], {
      zoom: 13,
      center: thePos
    });
    
    // Create markers
    fetch('/api/stations')
      .then(function(response) {
        //console.log("Getting stations")
        //check the response was ok
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + response.status);
            return;
        }
        response.json().then((data) => {
            for (var item in data) {
                    latandlong = data[item]
                    StationLat = latandlong[0];
                    StationLng = latandlong[1];
                    
                
                
                        var contentString = '<p>put html in me to show station num, name, available bikes and stands</p>';

        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });

                
                
                var image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
                marker = new google.maps.Marker({
                    position: {lat: StationLat, lng: StationLng},
                    map: map,
                    icon: image
                });
                
                marker.addListener('click', function() {
                infowindow.open(map, marker);
                });
      }
            
        }).catch((err) => {
            console.log('Fetch Error :-S', err)
        })
    })
}






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








