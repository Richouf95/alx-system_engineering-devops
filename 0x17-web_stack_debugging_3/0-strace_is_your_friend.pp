# find the apache bug and fix it
exec { 'php bug find and fix solution':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
