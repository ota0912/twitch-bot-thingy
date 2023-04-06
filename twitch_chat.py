import socket
import os
from dotenv import load_dotenv
load_dotenv()

sock = socket.socket()

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'
token = os.getenv('TWITCH_TOKEN')
channel = '#loltyler1'

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

while(True):
    resp = sock.recv(512).decode('utf-8')
    l = resp.split('\n')
    for i in l:
        temp = i.split(':')
        try:
            uname = temp[1].split('!')[0]
            msg = temp[-1]
        except:
            continue
        print(uname,"=======>",msg)
    # time.sleep(5)