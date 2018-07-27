import time

from rpyc import Service
from rpyc.utils.server import ThreadedServer


class TimeService(Service):
    def exposed_get_time(self):
        return time.ctime()


if __name__ == '__main__':
    s = ThreadedServer(TimeService, port=18871)
    s.start()
