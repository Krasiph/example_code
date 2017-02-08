#!/usr/bin/ruby
puts ""

print "Hello Ruby!"
print " It's time for Pen Testing!\n"

print Float(4)
print Float(5.7)

#interpolation
#num = 5
#puts "Hello Ruby!"
#puts "This is the number #{num}."

#classes and the bang!
#autobot = "Optimus Prime"
#puts "#{autobot}", "#{autobot.upcase}", "#{autobot.downcase!}", "#{autobot}"

#case statement
=begin
a = rand
print "Our random number is #{a} which is"
case a
when 0..100
	print " between 0 and 100.\n"
when 101..200
	print " between 101 and 200.\n"
else
	print " somewhere else.\n"
end
=end

#functions
=begin
def foo(x, y)
	return x - y
end

def bar(x, y)
	x - y
end

puts "Results of function foo() => #{foo(10, 5)}"
puts "Results of function bar() => #{bar(10, 5)}"
=end

print "\n"
