# grpc demo

* `TimeService` implements `get_time` RPC call.
* `get_time` returns the current server time in string format.

## How to Run

1. Create an virtualenv and install requirements.
    ```bash
    cd grpc
    pip3 install -r requirements.txt
    ```

1. (Optional) Generate the compiled files.
    ```bash
    python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. time.proto
    ```

1. Run Server in one terminal window:
    ```bash
    python3 server.py
    ```

1. Run Client in another terminal:
    ```bash
    python3 server.py
    ```