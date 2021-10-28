<?php
	session_start();
?>
<?php	
	unset($_SESSION['id']);
	unset($_SESSION['username']);
	echo "<script>window: location='login.php'</script>";
?>