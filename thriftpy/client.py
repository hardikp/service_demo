import thriftpy
from thriftpy.rpc import make_client

time_thrift = thriftpy.load('time_service.thrift', module_name='time_thrift')
client = make_client(time_thrift.TimeService, '127.0.0.1', 6000)
print(client.get_time())
