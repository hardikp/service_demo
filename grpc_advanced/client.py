from datetime import date

import grpc
import pandas as pd

import market_data_pb2
import market_data_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = market_data_pb2_grpc.MarketDataStub(channel)

    stocks = ['TSLA', 'F', 'AAPL', 'MSFT', 'FB']
    start_date = date(2018, 1, 1).strftime('%Y-%m-%d')
    end_date = date(2018, 9, 1).strftime('%Y-%m-%d')

    request = market_data_pb2.OHLCRequest(ticker=stocks, start_date=start_date, end_date=end_date)

    response = stub.GetOHLC(request)

    open_df = pd.DataFrame(index=response.dates)
    high_df = pd.DataFrame(index=response.dates)
    low_df = pd.DataFrame(index=response.dates)
    close_df = pd.DataFrame(index=response.dates)

    for stock in response.open:
        open_df[stock] = response.open[stock].price
        high_df[stock] = response.high[stock].price
        low_df[stock] = response.low[stock].price
        close_df[stock] = response.close[stock].price

    print('Last day Open: ')
    print(open_df.tail(1))
    print('Last day Close: ')
    print(close_df.tail(1))


if __name__ == '__main__':
    run()
