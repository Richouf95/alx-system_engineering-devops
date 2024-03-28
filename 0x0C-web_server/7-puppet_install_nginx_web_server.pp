# exécutez une commande sur un serveur
exec { 'update':
  command => '/usr/bin/apt-get update'
}

# installez nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

# créez un fichier HTML simple
file { '/var/www/html/index.html':
  content => 'Hello World!'
}

# Ajoutez une redirection dans la configuration nginx
exec { 'redirection':
  command  => 'sed -i "24i\     rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# Démarrez le service nginx
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}

