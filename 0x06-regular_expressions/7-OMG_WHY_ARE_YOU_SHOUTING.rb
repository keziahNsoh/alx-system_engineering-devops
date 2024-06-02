#!/usr/bin/env ruby

# Regular expression to match capital letters
regex = /[A-Z]/

input = ARGV[0]

matches = input.scan(regex)

if matches.any?
  puts matches.join('')
else
  puts ""
end
