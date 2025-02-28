# Stock Data Analysis Project

This project focuses on analyzing stock data using various technical indicators such as Simple Moving Average (SMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD). The data is processed and visualized to provide insights into stock price movements.

## Project Structure

- **Data Loading**: The project starts by loading stock data from a CSV file.
- **Data Cleaning**: Duplicates are removed, and unnecessary columns are dropped.
- **Data Transformation**: The data is sorted in descending order.
- **Technical Indicators Calculation**:
  - **Simple Moving Average (SMA)**: Calculated over a specified window.
  - **Relative Strength Index (RSI)**: Computed to measure the magnitude of recent price changes.
  - **Moving Average Convergence Divergence (MACD)**: Calculated to identify changes in the strength, direction, momentum, and duration of a trend in a stock's price.
- **Difference Calculation**: The difference between the 'high' and 'low' prices is calculated to understand daily price volatility.

## Requirements

To run this project, you need the following Python libraries:

- pandas
- scikit-learn
- matplotlib

You can install these libraries using pip:

```bash
pip install pandas scikit-learn matplotlib
```

## Usage

1. **Load the Data**: The stock data is loaded from a CSV file.
   ```python
   df_original = pd.read_csv('/content/TATAPOWER.NS_stock_data.csv')
   ```

2. **Clean the Data**: Remove duplicates and unnecessary columns.
   ```python
   df_original.drop_duplicates(inplace=True)
   columns_to_drop = ['Unnamed: 6', 'Unnamed: 7']
   df.drop(columns=columns_to_drop, inplace=True)
   ```

3. **Transform the Data**: Sort the data in descending order.
   ```python
   columns_descending = df_original.iloc[::-1]
   df = columns_descending
   ```

4. **Calculate SMA**: Compute the Simple Moving Average.
   ```python
   def calculate_sma(data, window):
       return data.rolling(window=window).mean()
   df['SMA_VALUES'] = calculate_sma(df['close'], window=7)
   ```

5. **Calculate RSI**: Compute the Relative Strength Index.
   ```python
   def calculate_rsi(data, window):
       delta = data.diff()
       gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
       loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
       rs = gain / loss
       rsi = 100 - (100 / (1 + rs))
       return rsi
   df['RSI_VALUES'] = calculate_rsi(df['close'], window=14)
   ```

6. **Calculate MACD**: Compute the Moving Average Convergence Divergence.
   ```python
   def calculate_macd(data, short_window, long_window, signal_window):
       short_ema = data.ewm(span=short_window, min_periods=1, adjust=False).mean()
       long_ema = data.ewm(span=long_window, min_periods=1, adjust=False).mean()
       df['MACD_LINE'] = short_ema - long_ema
       df['SIGNAL_LINE'] = df['MACD_LINE'].ewm(span=signal_window, min_periods=1, adjust=False).mean()
       df['MACD_HISTOGRAM'] = df['MACD_LINE'] - df['SIGNAL_LINE']
       return df['MACD_LINE'], df['SIGNAL_LINE'], df['MACD_HISTOGRAM']
   MACD_LINE, SIGNAL_LINE, MACD_HISTOGRAM = calculate_macd(df['close'], 12, 26, 9)
   ```

7. **Calculate Difference**: Compute the difference between 'high' and 'low' prices.
   ```python
   df['difference'] = df['high'] - df['low']
   ```

## Results

The final DataFrame contains the original data along with the calculated SMA, RSI, MACD, and difference values. These can be used for further analysis or visualization.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


## Acknowledgments

- Thanks to the pandas and scikit-learn communities for their excellent documentation and support.
- Special thanks to the contributors of the matplotlib library for making data visualization easier.
