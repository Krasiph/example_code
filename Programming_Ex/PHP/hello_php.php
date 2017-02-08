<?php
	//Declare and assign a variable. <br> is the newline for HTML
	$string = "Hello World!<br/>";

	//Print the string to the webpage
	echo $string;

	//Or use print. You can also use dot to concat strings
	print $string."I'm Matt!<br/>";

	//Or use printf
	printf('%s',$string);

	//We can set a variable to null
	$string = null;
	echo $string;

	//We can also destroy a variable using unset()
	unset($string);
	echo $string;

	//Since concat is a single operator it can be used similar to the familiar +=/-=
	$string = "PHP is pretty cool.";
	$string .= " I might start using it more often.";
	echo $string;

	//Think using </br> is annoying and prefer \n? Me too! Use nl2br($string) to sanitize your input!
	echo "<br/>--Newline to Break Test--<br/>";
	$string = "Hello world!\nI hate the break tag... and HTML in general.\nThey're just aweful.\n";
	echo nl2br($string);

	//Floats
	$i = floatval("8.9");
	if(is_float($i))
	{
		echo "Float!";
	}
	else
	{
		echo "Not a float";
	}
?>
