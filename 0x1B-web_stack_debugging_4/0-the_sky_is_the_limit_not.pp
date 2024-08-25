# This manifest configures the Nginx web server with basic settings.

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
      listen 80;
      server_name localhost;

      location / {
        root /var/www/html;
        index index.html index.htm;
      }
    }",
    notify  => Service['nginx'],
  }
}

include nginx

