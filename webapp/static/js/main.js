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



