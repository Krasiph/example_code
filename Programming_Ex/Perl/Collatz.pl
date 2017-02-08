#!/usr/bin/perl

sub on_even
{
	return $_[0] / 2;
}

sub on_odd
{
	return $_[0] * 3 + 1;
}

for($i=0; $i<scalar(@ARGV); $i++)
{
	$num = scalar($ARGV[$i]);
	if($num == 0 || $num < 0 || int($num) != $num)
	{
		print $ARGV[$i] . " is not a valid number.\n";
	}
	else
	{
		print $num . "\n";
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
			print "\t" . $num . "\n";
		}
		print "\n";
	}
}
