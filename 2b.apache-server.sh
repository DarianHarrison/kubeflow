sudo yum -y update
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
sudo systemctl status httpd

firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload
iptables-save | grep 80

mkdir -p /var/www/html/staticfiles

echo "serve static assets here" > /var/www/html/staticfiles/abc.txt

# verify ports are running
sudo lsof -i -P -n | grep ":80"

# # go to ui
# http://10.163.169.28/staticfiles/
# http://10.163.169.28/staticfiles/abc.txt