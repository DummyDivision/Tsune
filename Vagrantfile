# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	# All Vagrant configuration is done here. The most common configuration
	# options are documented and commented below. For a complete reference,
	# please see the online documentation at vagrantup.com.

	# Every Vagrant virtual environment requires a box to build off of.
	config.vm.box = "precise32"

	# The url from where the 'config.vm.box' box will be fetched if it
	# doesn't already exist on the user's system.
	config.vm.box_url = "http://files.vagrantup.com/precise32.box"

	# Create a forwarded port mapping which allows access to a specific port
	# within the machine from a port on the host machine. In the example below,
	# accessing "localhost:8080" will access port 80 on the guest machine.
	config.vm.network :forwarded_port, guest: 8000, host: 8080    # Django DevServer
	config.vm.network :forwarded_port, guest: 5000, host: 8081    # gunicorn

	# Share an additional folder to the guest VM. The first argument is
	# the path on the host to the actual folder. The second argument is
	# the path on the guest to mount the folder. And the optional third
	# argument is a set of non-required options.
	config.vm.synced_folder "", "/vagrant"

	# Enable provisioning with chef solo, specifying a cookbooks path, roles
	# path, and data_bags path (all relative to this Vagrantfile), and adding
	# some recipes and/or roles.

	config.vm.provision :chef_solo do |chef|
		chef.json = {
		   postgresql: {
		      password: {
			 postgres: 'Pa$$w0rd'
		      },
		      pg_hba: [
			 {
			    type: 'local',
			    db: 'all',
			    user: 'all',
			    addr: nil,
			    method: 'trust'
			 },
			 {
			    type: 'host',
			    db: 'all',
			    user: 'all',
			    addr: '127.0.0.1/32',
			    method: 'trust'
			 },
			 {
			    type: 'host',
			    db: 'all',
			    user: 'all',
			    addr: '::1/128',
			    method: 'trust'
			 }
		      ]
		   }
		}
					

		chef.recipe_url = "https://dl.dropboxusercontent.com/s/fh3dxy0tbjuoulm/dependencies.tar.gz"
		chef.add_recipe("apt")
		chef.add_recipe("apache2::mod_wsgi")
		chef.add_recipe("build-essential")
		chef.add_recipe("openssl")
		chef.add_recipe("postgresql")
		chef.add_recipe("postgresql::server")
		chef.add_recipe("yum")
		chef.add_recipe("python")
	end

	# Install the stuff to which no reasonable cookbook exists yet.
	config.vm.provision :shell, :inline => "sudo apt-get -y install libpq-dev python-dev firefox xvfb graphviz"
	config.vm.provision :shell, :inline => "sudo pip install -r /vagrant/requirements/docs.txt"
	config.vm.provision :shell, :inline => "sudo pip install -r /vagrant/requirements/unittests.txt"
	config.vm.provision :shell, :inline => "sudo /opt/vagrant_ruby/bin/gem install foreman"
end
