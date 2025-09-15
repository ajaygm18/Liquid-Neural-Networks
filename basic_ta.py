"""
Basic Technical Analysis functions to replace pandas-ta
"""
import pandas as pd
import numpy as np

def macd(data, close='Close', fast=12, slow=26, signal=9):
    """Calculate MACD"""
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    
    exp1 = close_series.ewm(span=fast).mean()
    exp2 = close_series.ewm(span=slow).mean()
    macd_line = exp1 - exp2
    signal_line = macd_line.ewm(span=signal).mean()
    histogram = macd_line - signal_line
    
    return pd.DataFrame({
        f'MACD_{fast}_{slow}_{signal}': macd_line,
        f'MACDs_{fast}_{slow}_{signal}': signal_line,
        f'MACDh_{fast}_{slow}_{signal}': histogram
    })

def rsi(data, close='Close', length=14):
    """Calculate RSI"""
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    
    delta = close_series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=length).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def bbands(data, close='Close', length=20, std=2):
    """Calculate Bollinger Bands"""
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    
    middle = close_series.rolling(window=length).mean()
    std_dev = close_series.rolling(window=length).std()
    
    upper = middle + (std_dev * std)
    lower = middle - (std_dev * std)
    
    bandwidth = (upper - lower) / middle
    percent_b = (close_series - lower) / (upper - lower)
    
    return pd.DataFrame({
        f'BBL_{length}_{std}': lower,
        f'BBM_{length}_{std}': middle,
        f'BBU_{length}_{std}': upper,
        f'BBB_{length}_{std}': bandwidth,
        f'BBP_{length}_{std}': percent_b
    })

def atr(data, high='High', low='Low', close='Close', length=14):
    """Calculate Average True Range"""
    high_series = data[high] if isinstance(data, pd.DataFrame) else data
    low_series = data[low] if isinstance(data, pd.DataFrame) else data
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    
    tr1 = high_series - low_series
    tr2 = abs(high_series - close_series.shift())
    tr3 = abs(low_series - close_series.shift())
    
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = true_range.rolling(window=length).mean()
    
    return atr

def obv(data, close='Close', volume='Volume'):
    """Calculate On Balance Volume"""
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    volume_series = data[volume] if isinstance(data, pd.DataFrame) else data
    
    obv = (np.sign(close_series.diff()) * volume_series).fillna(0).cumsum()
    return obv

def stoch(data, high='High', low='Low', close='Close', fastk=14, d=3):
    """Calculate Stochastic Oscillator"""
    high_series = data[high] if isinstance(data, pd.DataFrame) else data
    low_series = data[low] if isinstance(data, pd.DataFrame) else data
    close_series = data[close] if isinstance(data, pd.DataFrame) else data
    
    lowest_low = low_series.rolling(window=fastk).min()
    highest_high = high_series.rolling(window=fastk).max()
    
    k_percent = 100 * ((close_series - lowest_low) / (highest_high - lowest_low))
    d_percent = k_percent.rolling(window=d).mean()
    
    return pd.DataFrame({
        f'STOCHk_{fastk}_{d}_{d}': k_percent,
        f'STOCHd_{fastk}_{d}_{d}': d_percent
    })

# Add functions to pandas DataFrame
def add_ta_functions(df):
    """Add TA functions to DataFrame"""
    df.ta = TAAccessor(df)
    return df

class TAAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
    
    def macd(self, close='Close', fast=12, slow=26, signal=9, append=False):
        result = macd(self._obj, close, fast, slow, signal)
        if append:
            for col in result.columns:
                self._obj[col] = result[col]
        return result
    
    def rsi(self, close='Close', length=14, append=False):
        result = rsi(self._obj, close, length)
        if append:
            self._obj[f'{length}-Day RSI'] = result
        return result
    
    def bbands(self, close='Close', length=20, std=2, append=False):
        result = bbands(self._obj, close, length, std)
        if append:
            for col in result.columns:
                self._obj[col] = result[col]
        return result
    
    def atr(self, high='High', low='Low', close='Close', length=14, append=False):
        result = atr(self._obj, high, low, close, length)
        if append:
            self._obj[f'{length}-Day ATR'] = result
        return result
    
    def obv(self, close='Close', volume='Volume', append=False):
        result = obv(self._obj, close, volume)
        if append:
            self._obj['OBV'] = result
        return result
    
    def stoch(self, high='High', low='Low', close='Close', fastk=14, d=3, k=None, append=False):
        if k is not None:
            fastk = k
        result = stoch(self._obj, high, low, close, fastk, d)
        if append:
            for col in result.columns:
                self._obj[col] = result[col]
        return result

# Register the accessor
pd.api.extensions.register_dataframe_accessor("ta")(TAAccessor)