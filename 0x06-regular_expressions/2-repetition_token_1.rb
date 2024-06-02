#!/usr/bin/env ruby

# Regular expression to match the pattern
regex = /hb(t{2,})n/

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end
