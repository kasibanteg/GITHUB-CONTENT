<?php
	
	include ("connection.php");
	include ("ExportToExcel.php");

	if(isset($_POST["submit"]))
	{
		ExportExcel("csv");
 	}

?>

<html>
<head>
	<style type="text/css">
	body
	{
		margin: 0;
		padding: 0;
		background-color:#D6F5F5;
		text-align:center;
	}
	.top-bar
		{
			width: 100%;
			height: auto;
			text-align: center;
			background-color:#FFF;
			border-bottom: 1px solid #000;
			margin-bottom: 20px;
		}
	.inside-top-bar
		{
			margin-top: 5px;
			margin-bottom: 5px;
		}
	.link
		{
			font-size: 18px;
			text-decoration: none;
			background-color: #000;
			color: #FFF;
			padding: 5px;
		}
	.link:hover
		{
			background-color: #9688B2;
		}
	</style>
	
</head>

<body>
	<div class="top-bar">
		<div class="inside-top-bar">
			<a href="http://www.eggslab.net"><img src="http://www.eggslab.net/wp-content/uploads/2015/03/eggslablogo.png" width="500px"></a>
			<br><br>
			<a href="http://www.eggslab.net/export-mysql-table-data-into-excel-sheet" class="link">&larr; Back to Article</a> | <a href="http://demos.eggslab.net/" class="link">More Demos &rarr;</a>
		</div>
	</div>
    	

    		<form name="export" method="post">
    			<input type="submit" value="Click Me!" name="submit">
    		</form>
    

    <hr style="margin-top:300px;" />	
    
    <div align="center" style="font-size:18px;"><a href="http://www.eggslab.net">&copy; Eggs Lab</a></div>
 
</body>
</html>