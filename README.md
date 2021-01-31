# binance_historical_data
The repo contains a very simple function for one to call historical data from Binance API, using a third part package python-binance.

### Usage

1) Go to `binance_helper.py` and define your own `self.api_key` and `api_secret`. There can be more secured ways to do that and will be updated soon.
2) In `runner.py`, define your own directory to save the data called from binance. In my case, data will be saved in `dir_to_save_data`.
3) cd to this project directory and run `python runner.py -h` to see what options are available for customizing the data calling.

For example:

```{python}
# This will save all 1-minute ohlcv data from 2020-12-01 to 2020-12-31 of Bitcoin traded in Binance to ./dir_to_save_data
python runner.py -c "BTCUSDT" -s "2020-12-01" -e "2020-12-31" -i "1m"
```

