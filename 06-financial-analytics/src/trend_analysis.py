"""
Trend Analysis Module

This module provides functions for analyzing trends in financial data:
- Trend detection and classification
- Growth rate calculations
- Seasonality analysis
- Correlation analysis
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Tuple, Dict, List


def calculate_growth_rate(current: float, previous: float) -> float:
    """
    Calculate period-over-period growth rate.
    
    Growth Rate = (Current - Previous) / Previous * 100
    
    Args:
        current: Current period value
        previous: Previous period value
        
    Returns:
        Growth rate percentage
    """
    if previous == 0:
        return np.nan
    return ((current - previous) / abs(previous)) * 100


def calculate_cagr(begin_value: float, end_value: float, 
                   num_periods: int) -> float:
    """
    Calculate Compound Annual Growth Rate (CAGR).
    
    CAGR = (End Value / Begin Value) ^ (1 / n) - 1
    
    Args:
        begin_value: Initial value
        end_value: Final value
        num_periods: Number of periods
        
    Returns:
        CAGR percentage
    """
    if begin_value <= 0 or num_periods == 0:
        return np.nan
    return (np.power(end_value / begin_value, 1 / num_periods) - 1) * 100


def detect_trend(data: pd.Series, window: int = 3) -> str:
    """
    Detect trend direction (Uptrend, Downtrend, Sideways).
    
    Args:
        data: Time series data
        window: Window size for trend detection
        
    Returns:
        Trend classification: 'Uptrend', 'Downtrend', or 'Sideways'
    """
    if len(data) < window:
        return 'Insufficient Data'
        
    recent = data.tail(window)
    slope, _, _, _, _ = stats.linregress(range(len(recent)), recent.values)
    
    if slope > 0.01:
        return 'Uptrend'
    elif slope < -0.01:
        return 'Downtrend'
    else:
        return 'Sideways'


def calculate_moving_average(data: pd.Series, window: int) -> pd.Series:
    """
    Calculate Simple Moving Average.
    
    Args:
        data: Time series data
        window: Window size for moving average
        
    Returns:
        Series with moving averages
    """
    return data.rolling(window=window).mean()


def calculate_exponential_moving_average(data: pd.Series, 
                                         span: int) -> pd.Series:
    """
    Calculate Exponential Moving Average.
    
    Args:
        data: Time series data
        span: Span for exponential averaging
        
    Returns:
        Series with exponential moving averages
    """
    return data.ewm(span=span, adjust=False).mean()


def detect_seasonality(data: pd.Series, period: int = 12) -> Dict:
    """
    Detect seasonal patterns in data.
    
    Args:
        data: Time series data
        period: Seasonal period (e.g., 12 for monthly data with annual seasonality)
        
    Returns:
        Dictionary with seasonality metrics
    """
    if len(data) < period * 2:
        return {'seasonal': False, 'strength': 0}
        
    # Simple seasonality detection using autocorrelation
    seasonal_data = [data.iloc[i::period].values for i in range(period)]
    seasonal_vars = [np.var(s) if len(s) > 0 else 0 for s in seasonal_data]
    
    total_var = np.var(data)
    seasonal_strength = np.mean(seasonal_vars) / total_var if total_var > 0 else 0
    
    return {
        'seasonal': seasonal_strength > 0.3,
        'strength': seasonal_strength,
        'period': period
    }


def calculate_correlation(series1: pd.Series, series2: pd.Series) -> float:
    """
    Calculate Pearson correlation between two series.
    
    Args:
        series1: First time series
        series2: Second time series
        
    Returns:
        Correlation coefficient (-1 to 1)
    """
    if len(series1) != len(series2):
        raise ValueError("Series must have same length")
    
    # Remove NaN values
    mask = ~(series1.isna() | series2.isna())
    return series1[mask].corr(series2[mask])


def analyze_volatility(data: pd.Series, window: int = 20) -> pd.Series:
    """
    Calculate rolling volatility (standard deviation).
    
    Args:
        data: Time series data
        window: Window size for volatility calculation
        
    Returns:
        Series with volatility values
    """
    return data.pct_change().rolling(window=window).std() * np.sqrt(252)  # Annualized


def identify_anomalies(data: pd.Series, threshold: float = 2.0) -> pd.Series:
    """
    Identify anomalies using Z-score method.
    
    Args:
        data: Time series data
        threshold: Z-score threshold for anomaly (default: 2.0 = 95% confidence)
        
    Returns:
        Boolean series indicating anomalies
    """
    z_scores = np.abs(stats.zscore(data.dropna()))
    return pd.Series(z_scores > threshold, index=data.index[~data.isna()])


def calculate_trend_metrics(data: pd.Series, 
                           lookback_periods: int = None) -> Dict:
    """
    Calculate comprehensive trend metrics.
    
    Args:
        data: Time series data
        lookback_periods: Number of periods to analyze (default: all)
        
    Returns:
        Dictionary with trend metrics
    """
    if lookback_periods is not None:
        data = data.tail(lookback_periods)
    
    # Calculate trend
    trend = detect_trend(data)
    
    # Calculate growth rates
    if len(data) >= 2:
        recent_growth = calculate_growth_rate(data.iloc[-1], data.iloc[-2])
        period_growth = calculate_growth_rate(data.iloc[-1], data.iloc[0])
    else:
        recent_growth = np.nan
        period_growth = np.nan
    
    # Calculate volatility
    volatility = data.pct_change().std() * 100
    
    return {
        'trend': trend,
        'recent_growth': recent_growth,
        'period_growth': period_growth,
        'volatility': volatility,
        'mean': data.mean(),
        'std_dev': data.std(),
        'min': data.min(),
        'max': data.max()
    }
