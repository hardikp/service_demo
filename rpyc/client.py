import rpyc

conn = rpyc.connect('localhost', 18871)
print('Time is {}'.format(conn.root.get_time()))
