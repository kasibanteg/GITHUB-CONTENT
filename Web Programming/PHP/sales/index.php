<?php
ini_set("display_errors",1);
require_once 'excel_reader2.php';
require_once 'db.php';

$data = new Spreadsheet_Excel_Reader("example.xls");

echo "Total Sheets in this xls file: ".count($data->sheets)."<br /><br />";

$html="<table border='1'>";
for($i=0;$i<count($data->sheets);$i++) // Loop to get all sheets in a file.
{	
	if(count($data->sheets[$i][cells])>0) // checking sheet not empty
	{
		echo "Sheet $i:<br /><br />Total rows in sheet $i  ".count($data->sheets[$i][cells])."<br />";
		for($j=1;$j<=count($data->sheets[$i][cells]);$j++) // loop used to get each row of the sheet
		{ 
			$html.="<tr>";
			for($k=1;$k<=count($data->sheets[$i][cells][$j]);$k++) // This loop is created to get data in a table format.
			{
				$html.="<td>";
				$html.=$data->sheets[$i][cells][$j][$k];
				$html.="</td>";
			}
			$data->sheets[$i][cells][$j][1];
			$eid = $eid = mysqli_real_escape_string($connection,$data->sheets[$i][cells][$j][1]);
			$name = mysqli_real_escape_string($connection,$data->sheets[$i][cells][$j][2]);
			$email = mysqli_real_escape_string($connection,$data->sheets[$i][cells][$j][3]);
			$dob = mysqli_real_escape_string($connection,$data->sheets[$i][cells][$j][4]);
			$query = "insert into excel(eid,name,email,dob) values('".$eid."','".$name."','".$email."','".$dob."')";
			
			 
			
			mysqli_query($connection,$query);
			
			
			$html.="</tr>";
		}
	}
	
}






$html.="</table>";
echo $html;
echo "<br />Data Inserted in dababase";

{
//clean_up query
mysql_connect('localhost', 'root', '');
mysql_select_db('sales');

$delete_query = "delete from excel where dob=''";
mysql_query($delete_query);

}

?>