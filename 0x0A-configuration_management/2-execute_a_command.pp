exec { 'killmenow':
  command     => "pkill -f $(echo #{URI.encode_www_form_component('killmenow')})",
  path        => '/bin:/usr/bin',
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}

