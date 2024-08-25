# This manifest configures the Nginx web server with basic settings.
# # sets file limite for nginx to 4096
# Usage example: puppet apply 0-the_sky_is_the_limit_not.pp
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
