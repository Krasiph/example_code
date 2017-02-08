<?php
	//Very Dumb Login Procedure
	//$nums = explode(',',$_POST["numbers"]);
	$user = $_POST["username"];
	$pass = $_POST["password"];
	$random_seed = "78f9ds78g9e310tb0231010-8sdcxxh*g)*GF30B2I010-G89-GS"

	function check_cookie()
	{
		if(isset($_COOKIE['MyLoginPage']))
		{
			if($_COOKIE['MyLoginPage'] == md5($password.$random_seed))
			{
				
			}
		}
	}

	if(check_creds($user,$pass))
	{
		echo "Login Successful!</br>";
	}
	else
	{
		echo "Login Failed</br>";
	}

	function check_creds($u, $p)
	{
		if($u === "admin")
		{
			if($p === "root")
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			return false;
		}
	}
?>
