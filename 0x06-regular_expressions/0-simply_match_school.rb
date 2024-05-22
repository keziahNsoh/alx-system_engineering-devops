#!/usr/bin/env ruby

# Accept one argument from the command line
input_string = ARGV[0]

# Define the regular expression to match "School"
regex = /School/

# Use the regular expression to find matches in the input string
match_result = input_string.match(regex)

# Print the matched result
puts match_result ? match_result[0] : ''
