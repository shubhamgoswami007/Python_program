from ftplib import FTP

host = "192.168.1.2"
user = "demo"
password = "123"


with FTP(host, user, password) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    file = open('RAJKOT.txt', 'wb')
    ftp.retrbinary("RETR " + "RAJKOT.txt", file.write,1024)

    file = open('MUMBAI.txt', 'wb')
    ftp.retrbinary("RETR " + "MUMBAI.txt", file.write, 1024)

    file = open('JAMNAGAR.txt', 'wb')
    ftp.retrbinary("RETR " + "JAMNAGAR.txt", file.write, 1024)

    file = open('AHMEDABAD.txt', 'wb')
    ftp.retrbinary("RETR " + "AHMEDABAD.txt", file.write, 1024)

    ftp.close()