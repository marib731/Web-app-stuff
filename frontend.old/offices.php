<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Office</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <script src="payments.js"></script>
    <style>
            #expandedtable{
                height: 100%;
                overflow: hidden;
                transition: all .5s linear;
            }
/*collapisble button style from w3schools - + and - were super handy for debugging*/   
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.collapsible:after {
  content: '\002B';
  color: white;
  font-weight: bold;
  float: right;
  margin-left: 5px;
}

.active:after {
  content: "\2212";
}

.content {
  padding: 0 18px;
  max-height: 0;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
    overflow: hidden;
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
                //initial table
        $sql2="SELECT officeCode, city, phone, addressLine1, addressLine2 FROM `offices`";
            $result = $conn->query($sql2);
            if($result == false){
                die ("Error returning data from the query");
            }
            $row_cnt = mysqli_num_rows($result);
            if ($row_cnt > 0) {
                echo "<div class=\"table\" id=\"table\" style=\"overflow-x:auto\"><table><tr><th>Office Number</th><th>City</th><th>Telephone</th><th>Address</th><th>Employees List</th></tr>";
                while($row = $result->fetch_assoc()) {
                    $x = $row["officeCode"];
                    $sqlexpanded = "SELECT firstName, lastName, jobTitle, employeeNumber, email, employees.officeCode FROM `employees`, `offices` WHERE employees.officeCode = offices.officeCode and employees.officeCode = $x ORDER BY jobTitle DESC";
                    echo "<tr class=\"tr\" id=\"tr\"><td>" . $row["officeCode"] . "</td><td>" . $row["city"] . "</td><td>" . $row["phone"] . "</td><td>" . $row["addressLine1"] . ", " . $row["addressLine2"] . "</td><td><button class=\"collapsible\">Employees</button><div id=\"content\" class=\"content\">";
                    //inner table
                    $resultexpanded = $conn->query($sqlexpanded);
                    if($resultexpanded == false){
                        die ("Error returning data from the query");
                    }
                    $row_cnt2 = mysqli_num_rows($resultexpanded);
                    if ($row_cnt2 > 0) {
                        echo "<table><tr><th>Name</th><th>Job Title</th><th>Employee Number</th><th>E-mail</th></tr>";
                        while($rownew = $resultexpanded->fetch_assoc()) {
                            echo "<tr><td>" . $rownew["firstName"]. " " . $rownew["lastName"] . "</td><td>" . $rownew["jobTitle"] . "</td><td>" . $rownew["employeeNumber"] . "</td><td>" . $rownew["email"] . "</td></tr>"; 
                        }
                        echo "</table>";
                    } 
                    else {
                        echo "0 results";}
                    echo "</div></td></tr>"; 
                    
                }
   
                echo "</table></div>";
            } 
            else {
                echo "0 results";
            }
    
      

?>



<script>

var coll = document.getElementsByClassName("collapsible");
var i;
//w3schools
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
            window.onload =x();
            function x(){ 
                var a = false;
                document.getElementsByClassName("expandedtable").onclick=toggle_visibility(a);
            }
            
            function toggle_visibility(a){
                if (a == false){
                    document.getElementById("expandedtable").style.height = "100%";
                    document.getElementById("expandedtable").style.display = "inline";
                    a = true;
                    }
                else{
                    document.getElementById("expandedtable").style.height = "0px";
                    document.getElementById("expandedtable").style.display = "none";
                    a = false;
                    }
                }
            
            function getRowID($x){
                $x = parseInt(getElementByID($row["officeCode"]).value);}
            
            //w3schools
            var coll = document.getElementsByClassName("collapsible");
            var i;
            for (i = 0; i < coll.length; i++) {
              coll[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var MoreInfo = this.nextElementSibling;
                if (MoreInfo.style.display === "block") {
                  MoreInfo.style.display = "none";
                } else {
                  MoreInfo.style.display = "block";
                }
              });
            }
</script>
   
<?php
$conn->close(); 
    


   
    
include 'footer.php';
?>
    
</body>
</html>