#!/usr/bin/env python3
# coding: utf-8
# Copyright 2016 Abram Hindle, https://github.com/tywtyw2002, and https://github.com/treedust
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib.parse

def help():
    print("httpclient.py [GET/POST] [URL]\n")

class HTTPResponse(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):

    def connect(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        return None

    def get_code(self, data):
        
        try:
            protocal_ver = 'HTTP/1.1 '
            start = data.find(protocal_ver) + len(protocal_ver)
            end = start + 3

            return int(data[start:end+1])

        except:
            return -1

    def get_headers(self,data):
        # testing
        data = "Location: http://www.google.com/ \nContent-Type: text/html; charset=UTF-8\nDate: Thu, 09 Feb 2023 07:36:51 GMT\nExpires: Sat, 11 Mar 2023 07:36:51 GMT\nCache-Control: public, max-age=2592000\nServer: gws\nContent-Length: 219\nX-XSS-Protection: 0\nX-Frame-Options: SAMEORIGIN"

        method_GET = 'GET'
        method_POST = 'POST'

        if data.find(method_GET) != -1:
            # format: method path host args port
            header = f'GET {path} {host} {args} {port}}'

        if data.find(method_POST) != -1:
            print(f'POST index = {data.find(method_POST)}')

        # alist = data.split('\n')

        # c_type = alist.index('Content-Type')
        # c_len = alist.index('Content-Length')

        # if 'Content-Type' in alist:

        # print()
        # print(alist)
        # print(c_type)
        # print(c_len)

        return data

    def get_body(self, data):
        return None
    
    def sendall(self, data):
        self.socket.sendall(data.encode('utf-8'))
        
    def close(self):
        self.socket.close()

    # read everything from the socket
    def recvall(self, sock):
        buffer = bytearray()
        done = False
        while not done:
            part = sock.recv(1024)
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return buffer.decode('utf-8')

    def parse_url(self, url):
        
        host = urllib.parse.urlparse(url).hostname

        path, port = self.check_path_port(urllib.parse.urlparse(url).path, urllib.parse.urlparse(url).port)

        return path, host, port

    def check_path_port(self, path, port):

        if path == '':
            path = '/'

        if port == None:
            port = 8080

        return path, port

    def GET(self, url, args=None):
        
        path, port, host = self.parse_url(url)
        
        
        response = message() 
        
        return HTTPResponse(self.get_code(response), self.get_body(response))

    def POST(self, url, args=None):
        code = 500
        body = ""
        return HTTPResponse(code, body)

    def command(self, url, command="GET", args=None):
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print(client.command( sys.argv[2], sys.argv[1] ))
    else:
        print(client.command( sys.argv[1] ))
