import yfinance as yf
import ta # https://github.com/bukosabino/ta et https://technical-analysis-library-in-python.readthedocs.io/en/latest/
import matplotlib.pyplot as plt

# Import the data
f = yf.download("GOOG")
#print(f)

# Compute the RSI
f["rsi"] = ta.momentum.RSIIndicator(f["Adj Close"], window=14).rsi()
#print(f)

# Plot the RSI with the overbuy and oversell threshold

# Adapt the size of the graph
plt.figure(figsize=(15,8))

# View the RSI
plt.plot(f["rsi"].loc["2010"])
#plt.show()

# View horizontal line for the Overbuy threshold (RSI=70)
plt.axhline(70, color="#57CE95")

# View horizontal line for the Oversell threshold (RSI=30)
plt.axhline(30, color="#CE5757")

# Put a title
plt.title("RSI with thresholds")

# Put a legend
plt.legend(["RSI", "Overbuy threshold", "Oversell threshold"])

# Show the graph
plt.show()