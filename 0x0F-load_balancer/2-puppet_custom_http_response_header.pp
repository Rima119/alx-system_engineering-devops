# Add a custom HTTP header with Puppet

exec { 'update':
  command  => 'sudo apt update',
}

package {'nginx':
  ensure => installed,
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
}

-> file_line('line'):
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line   => '	server_name _;
    add_header X-Served-By $hostname;',
  match   => 'server_name _;',
  require => Exec['restart nginx']
}
