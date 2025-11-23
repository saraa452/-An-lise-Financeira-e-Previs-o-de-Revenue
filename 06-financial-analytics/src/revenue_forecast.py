"""
Revenue Forecasting Module

This module provides forecasting models for revenue prediction including:
- Simple Moving Average
- Exponential Smoothing
- Linear Regression
- ARIMA models
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict
import warnings

warnings.filterwarnings('ignore')


class MovingAverageForecaster:
    """Simple Moving Average forecasting model."""
    
    def __init__(self, window: int = 3):
        """
        Initialize Moving Average Forecaster.
        
        Args:
            window: Number of periods for moving average
        """
        self.window = window
        self.data = None
        
    def fit(self, data: pd.Series) -> None:
        """
        Fit the model with historical data.
        
        Args:
            data: Historical revenue data
        """
        self.data = data.copy()
        
    def predict(self, periods: int) -> pd.Series:
        """
        Generate forecast for specified periods.
        
        Args:
            periods: Number of periods to forecast
            
        Returns:
            Forecasted values
        """
        if self.data is None:
            raise ValueError("Model not fitted. Call fit() first.")
            
        forecasts = []
        data_copy = self.data.copy()
        
        for _ in range(periods):
            forecast = data_copy.tail(self.window).mean()
            forecasts.append(forecast)
            data_copy = pd.concat([data_copy, pd.Series([forecast])])
            
        return pd.Series(forecasts)


class ExponentialSmoothingForecaster:
    """Exponential Smoothing forecasting model."""
    
    def __init__(self, alpha: float = 0.3):
        """
        Initialize Exponential Smoothing Forecaster.
        
        Args:
            alpha: Smoothing parameter (0 < alpha <= 1)
        """
        self.alpha = alpha
        self.data = None
        self.level = None
        
    def fit(self, data: pd.Series) -> None:
        """
        Fit the model with historical data.
        
        Args:
            data: Historical revenue data
        """
        self.data = data.copy()
        self.level = data.iloc[0]
        
    def predict(self, periods: int) -> pd.Series:
        """
        Generate forecast for specified periods.
        
        Args:
            periods: Number of periods to forecast
            
        Returns:
            Forecasted values
        """
        if self.data is None:
            raise ValueError("Model not fitted. Call fit() first.")
            
        level = self.level
        
        # Update level for each historical data point
        for value in self.data.iloc[1:]:
            level = self.alpha * value + (1 - self.alpha) * level
            
        forecasts = [level] * periods
        return pd.Series(forecasts)


class LinearRegressionForecaster:
    """Linear Regression forecasting model."""
    
    def __init__(self):
        """Initialize Linear Regression Forecaster."""
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.X_train = None
        self.data = None
        
    def fit(self, data: pd.Series) -> None:
        """
        Fit the model with historical data.
        
        Args:
            data: Historical revenue data
        """
        self.data = data.copy()
        
        # Create time index
        X = np.arange(len(data)).reshape(-1, 1)
        X_scaled = self.scaler.fit_transform(X)
        
        self.model.fit(X_scaled, data.values)
        self.X_train = X
        
    def predict(self, periods: int) -> pd.Series:
        """
        Generate forecast for specified periods.
        
        Args:
            periods: Number of periods to forecast
            
        Returns:
            Forecasted values
        """
        if self.model is None:
            raise ValueError("Model not fitted. Call fit() first.")
            
        # Create future indices
        last_idx = len(self.data)
        future_idx = np.arange(last_idx, last_idx + periods).reshape(-1, 1)
        future_idx_scaled = self.scaler.transform(future_idx)
        
        forecasts = self.model.predict(future_idx_scaled)
        return pd.Series(forecasts)
    
    def get_trend(self) -> float:
        """
        Get the trend coefficient from the model.
        
        Returns:
            Trend slope
        """
        return self.model.coef_[0]


def create_forecast_summary(actual: pd.Series, 
                           forecast: pd.Series,
                           model_name: str) -> Dict:
    """
    Create a summary of forecast performance.
    
    Args:
        actual: Actual historical values
        forecast: Forecasted values
        model_name: Name of the forecasting model
        
    Returns:
        Dictionary with forecast summary
    """
    last_actual = actual.iloc[-1] if len(actual) > 0 else 0
    first_forecast = forecast.iloc[0] if len(forecast) > 0 else 0
    avg_forecast = forecast.mean()
    
    change_percent = ((first_forecast - last_actual) / last_actual * 100) if last_actual != 0 else 0
    
    return {
        'model': model_name,
        'last_actual': last_actual,
        'first_forecast': first_forecast,
        'avg_forecast': avg_forecast,
        'change_percent': change_percent,
        'forecast_range': (forecast.min(), forecast.max())
    }
