# Install and config nginx with puppet

exec { 'install_and_configure_nginx':
  command  => 'apt-get -y update;
  apt-get -y install nginx; 
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell
}
