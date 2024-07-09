#!/bin/bash

# Define variables
private_key="~/.ssh/school"
user="ubuntu"
server="54.157.157.39"

# SSH command with single-character flags
ssh -i "$private_key" "$user@$server"
