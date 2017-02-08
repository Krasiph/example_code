#!/usr/bin/ruby

i = 100
c = 0
until i < 0 or c == 20
	print "#{i}\n"
	i /= 2
	c += 1
end
