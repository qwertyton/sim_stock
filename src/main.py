import requests
import yfinance as yf
from config import all_ticker_list


def main():
    port = dict()
    money = dict()
    for type_symbol in all_ticker_list:
        interval = '1mo'
        start = '2000-1-1'
        end = '2024-1-31'
        data = yf.Ticker(type_symbol)
        data_df = data.history(interval=interval, start=start, end=end)
        port[type_symbol] = 0
        for ind in data_df.index:
            port[type_symbol] = port[type_symbol] + 5000 / data_df['Close'][ind]
            if ind == data_df.index[-1]:
                money[type_symbol] = port[type_symbol] * data_df['Close'][ind]
    sort_money = sorted(money, key=money.get, reverse=True)
    for r in sort_money:
        print(r, money[r])


if __name__ == "__main__":
    main()
