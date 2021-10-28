<?php
	session_start();
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
		?>
		
		<?php
			//validate host connection
			if(!mysql_connect($_dbHost, $_dbUser, $_dbPass)) {
				echo $_connFailed;
			}
			//validate database 
			if(!mysql_select_db($_dbName)) {
				echo $_dbConnFailed;
			} 
		?>
		
		<?php
			
			if(isset($_POST["login"])) {
				$username = trim($_POST["username"]);
				$password = trim($_POST["password"]);
				
				$loginQry = "SELECT * FROM tbl_user WHERE username='$username' AND password='$password'";
				$result = mysql_query($loginQry) or die ("Database query failed: $loginQry" . mysql_error());
				$userRaw = mysql_fetch_array($result);
			
				if($userRaw) {
					$_SESSION['id'] = $userRaw['id'];
					$_SESSION['username']= $userRaw['username'];
					$userid = $userRaw['id'];
						
						echo "<script>windows: location='index.php?userlog=$username'</script>";
				} else {
					$msgOut = "Sorry you can't login. Your username and password is incorrect.";
				}
			}
	?>
		<div>
			<?php echo $msgOut?>
		</div>
		<div>
		
		<fieldset>
		<legend>User Authentication</legend>
		<form action="login.php" method="post">
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
			<input type="submit" name="login" value="Login"><input type="reset" value="Clear">
		</form> 
		<br />
		<a href="register.php">Not yet registered?</a>	
		</fieldset>
		</div>
	</body>
	</html>