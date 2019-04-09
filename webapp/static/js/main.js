/*************************getting alerts from backend flask****************************/

fetch('/api/aa')
  .then(function(responseaa) {
    //check the response was ok
    if (responseaa.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' + responseaa.status);
        return;
    }
    
    responseaa.json().then((dataaa) => {
        for (var aaitem in dataaa) {
            document.getElementById('aaslerts').innerHTML += '<li>' + dataaa[aaitem] + '</li>';
        }
    }).catch((err) => {
        console.log('Fetch Error :-S', err)
    })
})

//Take dublin bikes station closures news and put titles in alert box
fetch('/api/db')
  .then(function(responsedb) {
    //check the response was ok
    if (responsedb.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' + responsedb.status);
        return;
    }
    
    responsedb.json().then((datadb) => {
        for (var dbitem in datadb) {
            document.getElementById('alerts').innerHTML += '<li>' + dbitem + '</li>';
            document.getElementById('alerts').innerHTML += '<p>' + datadb[dbitem] + '</p>';
            
        }
    }).catch((err) => {
        console.log('Fetch Error :-S', err)
    })
})

/****************************************************************************************/



/****************call basic google map *************************/


// Traffic layer
 var trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(map);
    
    
    // My Version Weather
    var imageMapType = new google.maps.ImageMapType({
      
      getTileUrl: function(tile,zoom) {
         /* Include date at the end as a cachebuster */
         return "https://mesonet.agron.iastate.edu/cache/tile.py/1.0.0/nexrad-n0q-900913/"
         + zoom + "/" + tile.x + "/" + tile.y +".png?"+ (new Date()).getTime(); 
      },
      opacity: 0.5
    });
    
    map.overlayMapTypes.push(imageMapType);
    
//getting latlong for stations from backend for marker drawing loop
fetch('/api/stations')
  .then(function(response) {
    //check the response was ok
    if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' + response.status);
        return;
    }
    
    response.json().then((data) => {
        for (var item in data) {
                StationLat = data[item[0]];
                StationLng = data[item[1]];
                // Create markers
               //checkbox filters here - eventlistener 
                marker = new google.maps.Marker({
                  position: {lat: StationLat, lng: StationLng},
                  map: map
                });
        }
    }).catch((err) => {
        console.log('Fetch Error :-S', err)
    })
})
