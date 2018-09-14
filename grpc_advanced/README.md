# grpc demo

* `MarketDataService` implements `GetOHLC` RPC call.
* `GetOHLC` takes in the list of stocks as well as the start and the end dates.
* `GetOHLC` returns the open, high, low, close prices for the given list of stocks.

## How to Run

1. Create an virtualenv and install requirements.
    ```bash
    cd grpc
    pip3 install -r requirements.txt
    ```

1. (Optional) Generate the compiled files.
    ```bash
    python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. market_data.proto
    ```

1. Run Server in one terminal window:
    ```bash
    python3 server.py
    ```

1. Run Client in another terminal:
    ```bash
    python3 server.py
    ```