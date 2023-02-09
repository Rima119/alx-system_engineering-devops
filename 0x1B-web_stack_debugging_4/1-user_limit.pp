# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message

exec {'fixed-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['fixed-2'],
}

exec {'fixed-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
