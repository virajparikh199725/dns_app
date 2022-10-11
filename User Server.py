# Deploying User Server

import flask;
from flask import *;
from socket import *;
from flask_api import status;
application = Flask(__name__);
@application.route('/fibonacci',methods = ['GET']);

def querying_as(ip, port, host):
    socket = socket(AF_INET, SOCK_DGRAM)
    json_query = {'TYPE': 'A', 'NAME': host};
    socket.sendto(json.dumps(json_query).encode(),(ip,port))
    Ip_address, Server_address = socket.recvfrom(2048)
    return Ip_address.decode()


def req_accept():
    host = request.args['hostname'];
    ip = request.args['as_ip'];
    port = request.args['as_port'];
    no = request.args['number'];
    fsPort = request.args['fs_port'];


    # if any of the above are absent, then return BAD REQUEST (400)
    if host==" " or ip==" " or port==" " or no==" " or fsPort==" ":
        return 'Wrong Format', status.HTTP_400_BAD_REQUEST;

    else:
        FsIp = querying_as(port, ip, host);
        dict_1 = ('number':no);
        act_address = 'http://' + FsIp + ':' + fsPort;
        output = requests.get(act_address + '/fibonacci' params = dict_1)
        return output.text, status.HTTP_200_OK;

application.run(host = '0.0.0.0', port = 8080)