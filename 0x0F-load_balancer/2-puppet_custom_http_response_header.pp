# Add a custom HTTP header with Puppet

exec { 'update':
  command  => 'sudo apt update',
}

-> package {'nginx':
  ensure => present,
}

-> file_line{'X-Served-By':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
}
