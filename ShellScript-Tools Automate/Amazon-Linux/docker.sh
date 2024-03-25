sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo usermod -aG docker $(whoami)
newgrp docker
sudo systemctl status docker