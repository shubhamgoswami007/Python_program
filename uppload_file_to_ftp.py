from ftplib import FTP

host = "192.168.1.2"
user = "demo"
password = "123"

save_path = 'C:/Users/shubh/Desktop/moument_data/RAJKOT.txt'
with FTP(host, user, password) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    file = open(r'C:/Users/shubh/Desktop/moument_data/RAJKOT.txt', 'rb')
    ftp.storbinary(r'STOR RAJKOT.txt', file)  # send the file
    file2 = open(r'C:/Users/shubh/Desktop/moument_data/mumbai.txt', 'rb')
    ftp.storbinary(r'STOR MUMBAI.txt', file2)
    file3 = open(r'C:/Users/shubh/Desktop/moument_data/jamnagar.txt', 'rb')
    ftp.storbinary(r'STOR JAMNAGAR.txt', file3)
    file4 = open(r'C:/Users/shubh/Desktop/moument_data/ahmedabad.txt', 'rb')
    ftp.storbinary(r'STOR AHMEDABAD.txt', file4)

    ftp.close()