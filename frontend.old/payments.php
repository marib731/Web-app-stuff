<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Payments</title>
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
            if ($conn->connect_error) {
                die("Failed to connect to server: " . $conn->connect_error);
            } 
        
            //variable that is changed according to dropdown
            $sql = "SELECT customerNumber, checkNumber, paymentDate, amount FROM payments GROUP BY paymentDate ORDER BY paymentDate DESC LIMIT 20";
        ?>
            <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" name="form" id="form">
                       <p>Display: </p> <select name="sizeselect" class="sizeselect" id="sizeselect">
                            <option id="20" value="20">20</option>
                            <option id="40" value="40">40</option>
                            <option id="60" value="60">60</option>
                            <default value="20"></default>
                        </select>
                        <input type="submit" name="submit"/>
                    </form>
        

    
        <?php    
        
        
    if(isset($_POST['sizeselect'])){
            $value = $_POST['sizeselect'];
                if ($value == '20'){
                    $sql = "SELECT customerNumber, checkNumber, paymentDate, amount FROM payments GROUP BY paymentDate ORDER BY paymentDate DESC LIMIT 20";
                }
                else if ($value == '40'){
                   $sql = "SELECT customerNumber, checkNumber, paymentDate, amount FROM payments GROUP BY paymentDate ORDER BY paymentDate DESC LIMIT 40"; 
                }
                else if ($value == '60'){
                    $sql = "SELECT customerNumber, checkNumber, paymentDate, amount FROM payments GROUP BY paymentDate ORDER BY paymentDate DESC LIMIT 60";

                }
            }
            //initial table
            $result = $conn->query($sql);
        if($result == false){
            die ("Error returning data from the query");
        }
            $row_cnt = mysqli_num_rows($result);
            if ($row_cnt > 0) {
                echo "<div class=\"table\" id=\"table\" style=\"overflow-x:auto\"><table width=\"80%\"><tr><th>Customer Number</th><th>Cheque Number</th><th>Payment Due</th><th>Amount</th><th>More Info</th></tr>";
                while($row = $result->fetch_assoc()) {
                    $ID=$row["customerNumber"];
                    $sqlexpanded = "SELECT customers.customerNumber, customers.phone, customers.salesRepEmployeeNumber, customers.creditLimit, COUNT(payments.amount) as NoofTransactions, SUM(payments.amount) as Total FROM payments, customers WHERE payments.customerNumber=customers.customerNumber and payments.customerNumber=$ID;";
                    echo "<tr class=\"tr\" id=\"tr\"><td>" . $row["customerNumber"] . "</td><td>" . $row["checkNumber"] . "</td><td>" . $row["paymentDate"] . "</td><td>" . $row["amount"] . "</td><td><button id=\"" . $row["customerNumber"] ."\" class=\"collapsible\">More Info</button><div class=\"MoreInfo\">";
                    //inner table
                    $resultexpanded = $conn->query($sqlexpanded);
                    if($resultexpanded == false){
                        die ("Error returning data from the query");
                    }
                    $row_cnt2 = mysqli_num_rows($resultexpanded);
                    if ($row_cnt2 > 0) {
                        echo "<table><tr><th>Phone Number</th><th>SalesRep Number</th><th>Credit Limit</th><th>Total Transactions</th><th>Total Due</th></tr>";
                        echo "<div class=\"expandedtable\" id=\"expandedtable\">";
                        while($rows = $resultexpanded->fetch_assoc()) {
                            echo "<tr><td>" . $rows["phone"] . "</td><td>" . $rows["salesRepEmployeeNumber"] . "</td><td>" . $rows["creditLimit"] . "</td><td>" . $rows["NoofTransactions"] . "</td><td>" . $rows["Total"] . "</td></tr>"; 
                        }
                        echo "</table></div>";
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
        <?php
            $conn->close();     
            include 'footer.php';
        ?>
        <script>
            window.onload =x();
            elem = document.getElementById("form")
                elem.onclick = function(){
                    document.forms[0].submit();
                }
            function x(){ 
                var a = false;
                document.getElementsByClassName("MoreInfo").onclick=toggle_visibility(a);
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
    //i genuinely cant remember where the below is from.....but it's from somewhere. Im also pretty sure only the collapsible bit is being used        
            function getRowID($ID){
                $ID = parseInt(getElementByID($row["customerNumber"]).value);}
            
            
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
    </body>
</html>