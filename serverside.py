from des import DesKey
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #created the socket
port = 12345
s.bind(('', port)) #binded socket to address
s.listen(10)

with open("key", "r") as f:
    des_key = f.read()

# keystr = "iamakeys" #key string must be multiple of 8
key = DesKey(des_key.encode('utf-8')) #create key
print("server is running...")
conn, addr = s.accept() #accept connection request
print("accept new connection from %s"%(str(addr)))
conn.send(str("connection has been established!").encode())
while True:
    rcv = conn.recv(1024)
    print("*"*18)
    print("recieved ciphertext is: %s"%rcv.decode('utf-8', 'ignore'))
    pt = key.decrypt(rcv, padding=True).decode() #decrypt the key
    print("recieved plaintext is: %s"%pt)
    print("*"*18)
    if pt == "bye": #if recieved msg is bye then break and close the connection
        break
    msg = input("type your message: ")
    ct = key.encrypt(msg.encode('utf-8'), padding=True)
    print("*"*18)
    print("key is ", des_key)
    print("sent plaintext is: %s"%msg)
    print("sent ciphertext is: %s"%ct.decode('utf-8', 'ignore'))
    print("*"*18)
    conn.send(ct) #send ciphertext
conn.close()