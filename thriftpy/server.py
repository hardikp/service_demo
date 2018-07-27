import time

import thriftpy
from thriftpy.rpc import make_server


class Dispatcher(object):
    def get_time(self):
        return time.ctime()


time_thrift = thriftpy.load('time_service.thrift', module_name='time_thrift')
server = make_server(time_thrift.TimeService, Dispatcher(), '127.0.0.1', 6000)
server.serve()
