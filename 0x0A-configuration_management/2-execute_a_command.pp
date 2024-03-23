# kill the processus "killmenow"

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
