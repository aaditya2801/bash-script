docker exec -it webserver yum install httpd git -y
docker exec -it webserver git clone https://github.com/aaditya2801/menu.git
docker exec -it webserver mv menu/index.html /var/www/html/
docker exec -it webserver /usr/sbin/httpd ; httpd

