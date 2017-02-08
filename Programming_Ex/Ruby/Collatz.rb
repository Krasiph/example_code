#!/usr/bin/ruby

#Displays the Collatz Conjecture path towards 1 for
#the given integer arguments.
#Collatz Conjecture Rules:
#If the number is odd, multiply by 3 and add 1.
#If the number is even, devide by 2

def f_odd(num)
	num * 3 + 1
end

def f_even(num)
	num / 2
end

for num_s in ARGV.each
	num = num_s.to_i
	if num == 0 || num < 0 || num != num_s.to_f
		puts num_s + " is not a valid number."
	else
		puts "#{num}"
		while num != 1
			if num % 2 == 0
				num = f_even(num)
			else
				num = f_odd(num)
			end
			puts "\t#{num}"
		end
	end
end
