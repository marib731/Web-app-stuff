/*************************getting alerts from backend flask****************************/
//Take road closures and traffic issues from aaRoadwatch twitter
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

/*Take dublin bikes station closures news and put titles in alert box
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



/****************call weather api *************************/
fetch('/api/weather')
  .then(function(resp) {
    //check the response was ok
    if (resp.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' + resp.status);
        return;
    }
    
    resp.json().then((dataW) => {
        for (var data in dataW) {
            document.getElementById('mapW').innerHTML += '<li>' + dataW[data] + '</li>';
        }
    }).catch((err) => {
        console.log('Fetch Error :-S', err)
    })
})


// Turn on/off Weather icon
$('#mapW').click(function(){
    fetch('/api/weather')
      .then(function(resp) {
        //check the response was ok
        if (resp.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + resp.status);
            return;
        }
        resp.json().then((dataW) => {
            for(var data in dataW) {
                console.log(dataW[data]);
                if (data == 'temperature'){
                    document.getElementById('weather').innerHTML +=  '<li> Temperature : ' + dataW[data] + '</li>';
                }
                else if(data == 'cloud-cover'){
                    document.getElementById('weather').innerHTML +=  '<li> Cloud Cover : ' + dataW[data] + '%</li>';    
                }
                else if(data == 'humidity'){
                    document.getElementById('weather').innerHTML +=  '<li> Humidity : ' + dataW[data] + '%</li>';    
                }
                else if(data == 'wind-direction'){
                    windDir = degToCard(dataW[data]);
                    document.getElementById('weather').innerHTML +=  '<li> Wind Direction : ' + windDir + '</li>';    
                }
                else if (data == 'wind-speed'){
                    document.getElementById('weather').innerHTML +=  '<li> Wind Speed : ' + dataW[data] + 'km per hour</li>';    
                }
            }
        }).catch((err) => {
            console.log('Fetch Error :-S', err)
        })
    })
    } 
    
    
    else{
        //settings when weather is off
        $(this).val('Turn on Weather');
        //option to clear weather 
        }

    })


//function to change circle degrees to direction for wind direction
var degToCard = function(deg){
  if (deg>11.25 && deg<33.75){
    return "NNE";
  }else if (deg>33.75 && deg<56.25){
    return "ENE";
  }else if (deg>56.25 && deg<78.75){
    return "E";
  }else if (deg>78.75 && deg<101.25){
    return "ESE";
  }else if (deg>101.25 && deg<123.75){
    return "ESE";
  }else if (deg>123.75 && deg<146.25){
    return "SE";
  }else if (deg>146.25 && deg<168.75){
    return "SSE";
  }else if (deg>168.75 && deg<191.25){
    return "S";
  }else if (deg>191.25 && deg<213.75){
    return "SSW";
  }else if (deg>213.75 && deg<236.25){
    return "SW";
  }else if (deg>236.25 && deg<258.75){
    return "WSW";
  }else if (deg>258.75 && deg<281.25){
    return "W";
  }else if (deg>281.25 && deg<303.75){
    return "WNW";
  }else if (deg>303.75 && deg<326.25){
    return "NW";
  }else if (deg>326.25 && deg<348.75){
    return "NNW";
  }else{
    return "N"; 
  }
}


//enxi's fancy weather box


        const app = document.getElementById('root');

        $.ajax({
            url: 'http://api.openweathermap.org/data/2.5/weather?appid=ae679d7b6212a1a3daf681d0d843aa83&q=Dublin&units=metric',
            type: "GET",
            dataType: "jsonp",
            jsonpCallback: "jsonp",
            success: function (data) {

                let widget = "<h3 style='padding-top:5px;'><strong>Current weather</strong>  </h3>" +
                    "<img src = 'http://openweathermap.org/img/w/" + data.weather[0].icon + ".png' > " + data.weather[0].description +


                    "<h3 style='text-align: center;border-bottom:thick double black; padding-bottom: 10%'>" + data.main.temp + "&deg;C</h3>" + "</hr>" +

                    "<h3 style='padding-top:5px; font-size: 110%'>Humidity levels at: " + data.main.humidity + " %</h3>" +

                    "<h3 style='padding-top:5px; font-size: 110%'>Winds at: " + data.wind.speed + " m/s</h3>"
                document.getElementById("weather_box").innerHTML = widget;

            }
        })

    function display() {
            var date = $("#date").val();
            var time = $("#time").val();

            if (date != '' && time != '') {
                $.ajax({
                    url: 'http://api.openweathermap.org/data/2.5/forecast?appid=ae679d7b6212a1a3daf681d0d843aa83&q=Dublin&units=metric',
                    type: "GET",
                    dataType: "jsonp",
                    jsonpCallback: "jsonp",
                    success: function (data) {
                        var a = 0;
                        for (var i = 0; i < data.list.length; i++) {
                            if (data.list[i].dt_txt == date + ' ' + time) {

                                let fore = "<img src = 'http://openweathermap.org/img/w/" + data.list[i].weather[0].icon + ".png' > " + data.list[i].weather[0].description +

                                    "<h3 style='text-align: center;border-bottom:thick double black; padding-bottom: 10%'>" + data.list[i].main.temp + "&deg;C</h3>" + "</hr>" +
                                    "<h3 style='padding-top:5px; font-size: 110%'>Humidity levels at: " + data.list[i].main.humidity + " %</h3>" +
                                    "<h3 style='padding-top:5px; font-size: 110%'>Winds at: " + data.list[i].wind.speed + " m/s</h3>"
                                document.getElementById("show_forecast").innerHTML = fore;
                                var a = 1;
                            }

                        }
                        if (a == 0) {
                            alert("Error");
                        }

                    }
                });
            }
        }
        /*Enxi weather box end*/