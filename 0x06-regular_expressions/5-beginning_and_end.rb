#!/usr/bin/env ruby

# Regular expression to match the pattern (case-insensitive)
regex = /^h.n$/i

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end
