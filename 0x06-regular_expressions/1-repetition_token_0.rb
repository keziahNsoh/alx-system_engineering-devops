#!/usr/bin/env ruby
# Define the regular expression
pattern = /School/

# Accept one argument from the command line
input = ARGV[0]

# Check if the input matches the pattern
if input.match?(pattern)
  puts "The input '#{input}' matches the pattern."
else
  puts "The input '#{input}' does not match the pattern."
end
