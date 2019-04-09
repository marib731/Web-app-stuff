<!DOCTYPE html>
<html>
<head>
	<!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="main.css">
    <link rel="stylesheet" href="GoogleMapsAPI.css">
</head>
    
<body>
    <!--nav bar-->
    <header class="header" id="header">
        <!--nav bar image-->
        <img src="images/Banniere.png" alt="Banner" width="100%" height="10%">
            <!--Nav Bar List-->
            <div class="nav" id="nav">
                <ul>
                    <li class="Home"><a href="index.html">Home</a></li>
                    <li class="Stations"><a href="stations.html">Stations</a>
                    <li class="RoutePlanner"><a href="#">Route Planner</a></li>
                    <li class="GettingStarted"><a href="#">Getting Started</a></li>
                    <li class="Contact"><a href="#">Contact</a></li>
                    <li class="MyAccount"><a href="#">My Account</a></li>
                    <input type="text" placeholder="Search.." name="search">
                </ul>
            </div>
	</header>
    <!--nav bar end-->

    <div class="whitebkgnd" id="whitebkgnd">   
        <div class="flexbox" id="flexbox">
            <!--Connect to database-->
            <?php
                //connect to RDS database on EC2
                $servername = "dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com";
                $username = "EnxiJessieMarian";
                $password = "SoftwareEngineering2019";
                $dbname = "dublinbikesdata";
                $port = "3306";
                mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);   
                $conn = new mysqli($servername, $username, $password, $dbname, $port);
                mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);   
                //$conn = mysqli_connect($_SERVER['Endpoint'], $_SERVER['EnxiJessieMarian'], $_SERVER['SoftwareEngineering2019'], $_SERVER['dublinbikesdata'], $_SERVER['3306']);

                // Check connection
                if ($conn->connect_error) {
                    echo "Failed to connect to server: " . $conn->connect_error;
                } 

                // get data from RDS instance and store in variable result 
                $sql = "SELECT * FROM DublinBikesData";
                $result = $conn->query($sql);
                if($result == false){
                    echo "Error returning data from the query";
                }

                //loop through result and display lat_long for each station
                if ($result->num_rows > 0) {
                    while($row = $result->fetch_assoc()) {
                        echo "$row[position_lat]";
                        echo "$row[position_lng]"; 
                    }
                }
            ?>
    

            <!--map-->
                <div class="map" id="map">
                    <input id="mapTraffic" type="button" value="Turn on Traffic" />
                    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

                    <script src="GoogleMapsAPI.js"></script>
                    <script async defer
                            src="https://maps.googleapis.com/maps/api/js?key=AIzaSyChFqt0viVKUQkLpX0Fmnfj4W9yTj-7sew&callback=initMap">
                    </script>
                </div>
    
            <!--side bar-->
                <div id="sidebar" class="sidebar">
                    <h2>Alerts</h2>
                    <div class="alert-container">
                        <p>display alerts here</p>
                    </div>
                </div>
    
        </div>
    </div>
</body>
</html>

