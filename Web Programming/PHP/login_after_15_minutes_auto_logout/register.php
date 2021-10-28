<html>
	<head>
		<title>User registration</title>
	</head>
	<body>
		<?php
			//declaring variables
			$_dbHost = "localhost";
			$_dbUser = "root";
			$_dbPass = "";
			$_dbName = "tutorials";
			$_connFailed = "Database connection failed.";
			$_dbConnFailed = "Database selection failed.";
			$_register = isset($_POST["register"]);
			$_username = trim($_POST["username"]);
			$_password = trim($_POST["password"]);
			$_uIP = trim($_POST["uIP"]);
			$_userExists = "<font color='red'><b>The user: " .$_username. ", is already exists. Please used other user.</b></font>";
			$_userSuccessCreated = "<font color='green'>Your user <b>".$_username."</b> has been successfully created.</font>";
			$_userFailedCreated = "User couldn't not created. Please check.";
			$_fieldEmpty = "Failed required, Please check.";
			
			//validate host connection
			if(!mysql_connect($_dbHost, $_dbUser, $_dbPass)) {
				echo $_connFailed;
			}
			//
			if(!mysql_select_db($_dbName)) {
				echo $_dbConnFailed;
			} 
		
			if($_register) {	//check if variable is true then POST request
				if ($_username == "" || $_password == "") {	//check if field is empty
					$message = $_fieldEmpty;
				} else {
				//check if user is already exists in database
				$query = mysql_query("Select * From tbl_user Where username = '$_username'") or die ("Database query failed." . mysql_error());
				if(mysql_num_rows($query)) {
					echo $_userExists;
				} else {
					//insert user if not exists
						if(mysql_query("Insert Into tbl_user (username, password) Values ('".$_username."', '".$_password."')")) {
							echo "<script>windows: location='login.php?Success registration you can now login.'</script>";
						} else {
				//failed to create user
						$message = $_userFailedCreated;
						}
					}
				}
			}
		?>	
		<div>
			<?php echo $message?>
		</div>
		<div>
		
		<fieldset>
		<legend>User Registration</legend>
		<form action="register.php" method="post">
			Username:
			<br />
			<input type="text" name="username" placeholder="Username!">
			<br />
			<br />
			Password:
			<br />
			<input type="password" name="password" placeholder="Password!">
			<br />
			<br />
			<input type="submit" name="register" value="Register"><input type="reset" value="Clear">
		</form> 
		<a href="login.php">Do you want to login?</a>	
		</fieldset>
		</div>
	</body>
</html>	