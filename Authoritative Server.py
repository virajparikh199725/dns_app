# Authoritative Server

from socket import *
import json

server_p = 53533

serverS = socket(AF_INET, SOCK_DGRAM)
serverS.bind('', server_p);
IPMAP = {};

def request(qMessage):
    message = json.load(qMessage.decode());
    Ip = 'VALUE' in message;

    if not Ip:
        host = message['NAME'];
        req_type = message['TYPE'];

        return query(host, req_type);

    else:
        req_type = message['TYPE'];
        host = message['NAME'];
        Ip = message['VALUE'];
        t_t_l = message['TTL'];
        return registering(host, Ip, req_typ, t_t_l);


def registering(host, Ip, req_type, t_t_l):
    id = req_type + ' ' + host;
    dns_content = {'TYPE': req_type, 'VALUE': Ip, 'NAME': host, 'TTL': t_t_l};
    IPMAP[id] = dns_content;

    return json.dumps('').encode();

def query(host, req_type):
    dns_content = IPMAP[req_type + ' ' + host];
    ip = dns_content['VALUE'];
    return str(ip).encode();

while 1:
    qMessage, address = serverS.recvfrom(2048);
    message_response = request(qMessage);
    serverS.sendto(message_response, address);