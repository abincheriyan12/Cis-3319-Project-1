#Abin Cheriyan
#Cis 3319 - Project 1
from des import DesKey
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #created the socket
port = 12345
s.bind(('', port)) #binded socket to address
s.listen(10)

with open("key", "r") as f:
    des_key = f.read()

key = DesKey(des_key.encode('utf-8')) #create key
print(" Server is running............ yayy")
conn, addr = s.accept() #accept connection request
print(" Accepted new connection from %s " % (str(addr)))
conn.send(str(" Connection has been established! ").encode())
while True:
    rcv = conn.recv(1024)
    print("*" * 20)
    print(" Recieved ciphertext is: %s" % rcv.decode('utf-8', 'ignore'))
    pt = key.decrypt(rcv, padding = True).decode() #decrypt the key
    print(" Recieved plaintext is: %s " % pt)
    print("*" *20)
    if pt == "bye": #Bye breaks and closes the connection
        break
    msg = input("type your message: ")
    ct = key.encrypt(msg.encode('utf-8'), padding=True)
    print("*" *20)
    print(" Key is ", des_key)
    print(" Plaintext is: %s " % msg)
    print(" Ciphertext is: %s " % ct.decode('utf-8', 'ignore'))
    print("*" * 20)
    conn.send(ct) #sending the ciphertext
conn.close()