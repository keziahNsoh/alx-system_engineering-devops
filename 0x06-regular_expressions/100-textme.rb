#!/usr/bin/env ruby

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/

file_path = ARGV[0]

log_file = File.read(file_path)

log_file.scan(regex) do |sender, receiver, flags|
  puts "#{sender},#{receiver},#{flags}"
end
