import time
from concurrent import futures
from datetime import datetime

import grpc
import pandas_datareader.data as web

import market_data_pb2
import market_data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MarketDataService(market_data_pb2_grpc.MarketDataServicer):
    """
    MarketDataService
    - GetOHLC - returns the open, high, low, close prices for the given securities.
    """

    def GetOHLC(self, request, context):
        """
        Returns [open, high, low, close] prices for the given list of securities.
        Prices are specified between given start and end dates.
        """
        # Extract arguments
        start_date = datetime.strptime(request.start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(request.end_date, '%Y-%m-%d').date()
        tickers = request.ticker

        # Reply parameters
        open_dict = {}
        high_dict = {}
        low_dict = {}
        close_dict = {}
        dates = None

        # Fetch OHLC data using pandas-datareader
        for ticker in tickers:
            df = web.DataReader(ticker, 'iex', start_date, end_date)

            if dates is None:
                dates = list(df.index)

            open_dict[ticker] = market_data_pb2.OHLCReply.OHLCRet(price=list(df['open']))
            high_dict[ticker] = market_data_pb2.OHLCReply.OHLCRet(price=list(df['high']))
            low_dict[ticker] = market_data_pb2.OHLCReply.OHLCRet(price=list(df['low']))
            close_dict[ticker] = market_data_pb2.OHLCReply.OHLCRet(price=list(df['close']))

        # Construct the OHLC Reply
        reply = market_data_pb2.OHLCReply(dates=dates, open=open_dict, high=high_dict, low=low_dict, close=close_dict)
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_data_pb2_grpc.add_MarketDataServicer_to_server(MarketDataService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
