<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <style> 
        .table{
            padding: 10%;
            padding-top: 3%;
        }
    </style>
</head>
<body>
   
<?php include 'header.php';

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "classicmodels";
 mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);   
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Failed to connect to server: " . $conn->connect_error);
} 

$sql = "SELECT productLine, textDescription FROM productlines";
$result = $conn->query($sql);
if($result == false){
    die ("Error returning data from the query");
}

if ($result->num_rows > 0) {
    // output data of each row
    echo "<div class=\"table\" id=\"table\" style=\"overflow-x:auto\"><table><tr><th>Product</th><th>Description</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr class=\"tr\" id=\"tr\"><td>" . $row["productLine"] . "</td><td>" . $row["textDescription"] . "</td></tr>"; 
    }
    echo "</table></div>";
} else {
    echo "0 results";
}
$conn->close();     
include 'footer.php';?>
</body>
</html>