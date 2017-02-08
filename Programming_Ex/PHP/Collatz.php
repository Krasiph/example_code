<?php
	//The Collatz Conjecture
	$nums = explode(',',$_POST["numbers"]);
	Collatz($nums);
	/*
	echo $_POST["numbers"]."<br/>";
	foreach($nums as $num)
	{
		echo $num;
	}
	echo "<br/>";
	*/

	function on_even($num)
	{
		return $num / 2;
	}

	function on_odd($num)
	{
		return $num * 3 + 1;
	}

	function Collatz($nums)
	{
		for($i=0; $i<count($nums); $i++)
		{
			$num = intval($nums[$i]);
			if($num == 0 || $num < 0 || $num != floatval($nums[$i]))
			{
				echo $nums[$i] . " is not a valid number.<br/>";
			}
			else
			{
				echo $num . "<br/>";
				while($num != 1)
				{
					if($num % 2 == 0)
					{
						$num = on_even($num);
					}
					else
					{
						$num = on_odd($num);
					}
					echo $num . "<br/>";
				}
			}
			echo "---------------------------<br/>";
		}
	}
?>
