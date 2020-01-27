

Vagrant.configure("2") do |config|


  config.vm.define "ansible-server" do |ansible|
    ansible.vm.box = "centos/7"
    ansible.vm.hostname = "ansible-server"
    ansible.vm.network "private_network", ip: "173.42.42.100"
    ansible.vm.provider "virtualbox" do |v|
      v.name = "ansible-server"
      v.memory = 1024
      v.cpus = 1
      v.customize ["modifyvm", :id, "--audio", "none"]
    end
  end

  NodeCount = 2

  # Kubernetes Worker Nodes
  (1..NodeCount).each do |i|
    config.vm.define "ansible-client#{i}" do |workernode|
      workernode.vm.box = "centos/7"
      workernode.vm.hostname = "ansible-client#{i}.com"
      workernode.vm.network "private_network", ip: "173.42.42.10#{i}"
      workernode.vm.provider "virtualbox" do |v|
        v.name = "ansible-client#{i}"
        v.memory = 1024
        v.cpus = 1
        # Prevent VirtualBox from interfering with host audio stack
        v.customize ["modifyvm", :id, "--audio", "none"]
      end
    end
  end

end
