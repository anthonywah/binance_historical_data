from binance_helper import BinanceAPIHelper
from argparse import ArgumentParser
import sys


TARGET_SAVE_DIR = './dir_to_save_data'


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('-c', '--coin',       help='target_coin', action='store', desk='coin',       default='BTCUSDT')
    p.add_argument('-s', '--start_date', help='YYYY-MM-DD',  action='store', desk='start_date', default='2020-01-01')
    p.add_argument('-e', '--end_date',   help='YYYY-MM-DD',  action='store', desk='end_date',   default='2020-12-31')
    p.add_argument('-i', '--interval',   help='1m',          action='store', desk='interval',   default='1m')
    args = p.parse_args(sys.argv[1:])

    helper = BinanceAPIHelper()
    helper.get_historical_ohlc(symbol=args.coin,  
                               start_date=args.start_date, 
                               end_date=args.end_date, 
                               interval=args.interval, 
                               save_dir=TARGET_SAVE_DIR)
