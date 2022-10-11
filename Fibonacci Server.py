# Fibonacci Server

from flask import Flask, request
import json
from flask_api  import status;
from socket import *

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET']);

def calc_fib_number(fib_number):
    fib_number = int(fib_number);
    if fib_number <= 2:
        return 1;
    output = calc_fib_number((fib_number-1) + calc_fib_number(fib_number-2);
    return output;


def fibonacci_output():
    fib_number = request.args('number');
    output = calc_fib_number(fib_number)
    return str(output)

@app.route('/register', methods = ['PUT']);
def register():
    content = request.get_json()
    host = content.get('host')
    port = int(content.get('port'))
    ip = content.get('ip');
    reg_json = ('TYPE': 'A', 'NAME': host, 'VALUE': ip, 'TTL': 10)
    cSocket = socket(AF_INET, SOCK_DGRAM);
    cSocket.sendto(json.dumps(register_json.encode()), (ip,port))
    responseMessage, serverAddress = cSocket.recvfrom(2048);
    return 'Not Successfully registered', status.HTTP_201_CREATED

app.run(host = '0.0.0.0', port = 9090, debug = True)