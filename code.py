!pip install pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

TO READ THE CSV FILE

df_original = pd.read_csv('/content/TATAPOWER.NS_stock_data.csv')
df_original.drop_duplicates(inplace=True)
df_original['close']

#TO TRANSFORM THE DATA INTO DECENDING


import pandas as pd

# Assuming df_original is your DataFrame containing Excel sheet data

# Reverse the list of column names to sort by position in descending order
columns_descending = df_original.iloc[::-1]

df=columns_descending
columns_to_drop = ['Unnamed: 6', 'Unnamed: 7']  # Replace 'COLUMN1', 'COLUMN2', 'COLUMN3' with actual column names

# Check if columns exist before dropping
columns_to_drop = [col for col in columns_to_drop if col in df.columns]
# Drop columns using the drop() method
df.drop(columns=columns_to_drop, inplace=True)
df.head()

#TO CALCULATE THE SIMPLE MOVING AVERAGE

unnamed_column = df.iloc[:, 0]
y=unnamed_column
x=df_original['close']
def calculate_sma(data, window):
    return x.rolling(window=window).mean()

# Calculate SMA for a specified window (e.g., 4 days)
window_size = 7

df['SMA_VALUES'] = calculate_sma(df, window=window_size)

df.head()




#TO CALCULATE THE RELATVE STRENGTH INDEX

def calculate_rsi(data, window):
    # Calculate price changes
    delta = data.diff()

    # Separate gains and losses
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    # Avoid division by zero
    loss[loss == 0] = pd.NA

    # Calculate RS (Relative Strength)
    rs = gain / loss

    # Calculate RSI (Relative Strength Index)
    rsi = 100 - (100 / (1 + rs))

    return rsi

# Assuming 'df' is your DataFrame containing stock price data
window_size = 14  # Typical window size for RSI calculation
df['RSI_VALUES'] = calculate_rsi(x, window=window_size)



#TO CALCULATE THE MACD VALUE

import pandas as pd
import matplotlib.pyplot as plt

def calculate_macd(data, short_window, long_window, signal_window):
    # Calculate short-term EMA
    short_ema = data.ewm(span=short_window, min_periods=1, adjust=False).mean()

    # Calculate long-term EMA
    long_ema = data.ewm(span=long_window, min_periods=1, adjust=False).mean()

    # Calculate MACD line
    df['MACD_LINE'] = short_ema - long_ema
    MACD_LINE = df['MACD_LINE']

    # Calculate Signal line
    df['SIGNAL_LINE'] = MACD_LINE.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    SIGNAL_LINE = df['SIGNAL_LINE']

    # Calculate MACD Histogram
    df['MACD_HISTOGRAM'] = MACD_LINE - SIGNAL_LINE
    MACD_HISTOGRAM = df['MACD_HISTOGRAM']

    return MACD_LINE, SIGNAL_LINE,MACD_HISTOGRAM

# Assuming 'df' is your DataFrame containing stock price data
short_window = 12
long_window = 26
signal_window = 9
MACD_LINE, SIGNAL_LINE,MACD_HISTOGRAM = calculate_macd(x, short_window, long_window, signal_window)

df.head()


# prompt: Using dataframe df: calculate the difference

# Calculate the difference between the 'high' and 'low' columns
df['difference'] = df['high'] - df['low']

# Display the first few rows to show the new 'difference' column
print(df.head())
