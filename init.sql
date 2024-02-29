CREATE USER 'Breizhibus'@'%' IDENTIFIED BY 'Breizhibus';
GRANT ALL PRIVILEGES ON Breizhibus.* TO 'Breizhibus'@'%';
FLUSH PRIVILEGES;