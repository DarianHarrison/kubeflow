# WARNING, USE THS IN A NON K8S ENVIRONMENT, IT MESSES CONFIGURATION UP
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce docker-ce-cli containerd.io
yum list docker-ce --showduplicates | sort -r
sudo systemctl start docker
sudo systemctl status docker
sudo docker run hello-world