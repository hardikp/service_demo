# service_demo
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/hardikp/service_demo/blob/master/LICENSE)

Python3 server and client examples for [gRPC](https://grpc.io/), [Thrift](https://thrift.apache.org/docs/) and [RPyC](https://rpyc.readthedocs.io/en/latest/).

## Service Example

* `TimeService` implents `get_time` RPC call.
* `get_time` returns the current server time in string format.

## Implementations

* grpc
* thrift
* thriftpy
* rpyc
* (Upcoming) grpc streaming
* (Upcoming) thrift streaming
* (Upcoming) rpyc streaming

## How to use

1. Create an virtualenv and install requirements.
    ```bash
    cd grpc
    pip3 install -r requirements.txt
    ```

1. Run Server in one terminal window:
    ```bash
    python3 server.py
    ```

1. Run Client in another terminal:
    ```bash
    python3 client.py
