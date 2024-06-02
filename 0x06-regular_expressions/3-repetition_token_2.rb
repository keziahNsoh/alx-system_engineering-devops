#!/usr/bin/env ruby

# Regular expression to match the pattern
regex = /hb(t{2,})n/

# Accept the argument from command line
input = ARGV[0]

# Match the input against the regular expression
match = input.match(regex)

# Output the result
if match
  puts match[0]
else
  puts "No match found"
end
