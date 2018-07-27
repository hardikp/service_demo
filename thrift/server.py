#!/usr/bin/env python
import sys
import time

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
sys.path.append('gen-py')
from time_service import TimeService


class TimeHandler:
    def __init__(self):
        self.log = {}

    def get_time(self):
        return time.ctime()


if __name__ == '__main__':
    handler = TimeHandler()
    processor = TimeService.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
