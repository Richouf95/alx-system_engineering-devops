# User limit

exec {'increase-hard':
  command => 'sed -i "/holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'increase-soft':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

