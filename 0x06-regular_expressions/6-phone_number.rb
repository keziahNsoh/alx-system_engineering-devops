#!/usr/bin/env ruby

# Regular expression to match a 10-digit phone number
regex = /^\d{10}$/

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end
