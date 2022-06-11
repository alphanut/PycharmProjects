import yfinance as yf

ticker_list = ["EURUSD=X"] # on trouve le ticker sur la page de yahoo e.g. pour EURUSD: https://fr.finance.yahoo.com/quote/EURUSD%3DX?p=EURUSD%3DX
# avec date de début et fin
print(yf.download(ticker_list, start="2000-01-01", end="2010-01-01"))
# choix du timeframe
print(yf.download(ticker_list, interval="1mo"))
