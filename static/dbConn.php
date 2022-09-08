<?php 

$con = mysqli_connect("localhost","root","","student_db");

if(mysqli_connect_errno()){
    echo "Connenction Fail".mysqli_connect_errno();
}