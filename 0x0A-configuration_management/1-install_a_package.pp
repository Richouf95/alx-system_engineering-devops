# Install a package
# Using Puppet, install flask from pip3

# define package ressource
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
