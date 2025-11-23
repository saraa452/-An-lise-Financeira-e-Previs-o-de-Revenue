"""
Financial Ratios Calculation Module

This module provides functions to calculate various financial ratios including:
- Liquidity ratios (Current Ratio, Quick Ratio)
- Profitability ratios (Profit Margin, ROA, ROE)
- Efficiency ratios (Asset Turnover, Receivables Turnover)
"""

import pandas as pd
import numpy as np
from typing import Dict, Union


def calculate_current_ratio(current_assets: float, current_liabilities: float) -> float:
    """
    Calculate Current Ratio.
    
    Current Ratio = Current Assets / Current Liabilities
    Measures short-term liquidity.
    
    Args:
        current_assets: Total current assets
        current_liabilities: Total current liabilities
        
    Returns:
        Current ratio value
    """
    if current_liabilities == 0:
        return np.nan
    return current_assets / current_liabilities


def calculate_quick_ratio(current_assets: float, inventory: float, 
                         current_liabilities: float) -> float:
    """
    Calculate Quick Ratio (Acid Test Ratio).
    
    Quick Ratio = (Current Assets - Inventory) / Current Liabilities
    More conservative measure of liquidity.
    
    Args:
        current_assets: Total current assets
        inventory: Inventory value
        current_liabilities: Total current liabilities
        
    Returns:
        Quick ratio value
    """
    if current_liabilities == 0:
        return np.nan
    return (current_assets - inventory) / current_liabilities


def calculate_profit_margin(net_income: float, revenue: float) -> float:
    """
    Calculate Net Profit Margin.
    
    Profit Margin = Net Income / Revenue * 100
    
    Args:
        net_income: Net income
        revenue: Total revenue
        
    Returns:
        Profit margin percentage
    """
    if revenue == 0:
        return np.nan
    return (net_income / revenue) * 100


def calculate_roa(net_income: float, total_assets: float) -> float:
    """
    Calculate Return on Assets (ROA).
    
    ROA = Net Income / Total Assets * 100
    
    Args:
        net_income: Net income
        total_assets: Total assets
        
    Returns:
        ROA percentage
    """
    if total_assets == 0:
        return np.nan
    return (net_income / total_assets) * 100


def calculate_roe(net_income: float, shareholders_equity: float) -> float:
    """
    Calculate Return on Equity (ROE).
    
    ROE = Net Income / Shareholders' Equity * 100
    
    Args:
        net_income: Net income
        shareholders_equity: Total shareholders' equity
        
    Returns:
        ROE percentage
    """
    if shareholders_equity == 0:
        return np.nan
    return (net_income / shareholders_equity) * 100


def calculate_debt_to_equity(total_debt: float, shareholders_equity: float) -> float:
    """
    Calculate Debt-to-Equity Ratio.
    
    D/E Ratio = Total Debt / Shareholders' Equity
    
    Args:
        total_debt: Total debt
        shareholders_equity: Total shareholders' equity
        
    Returns:
        Debt-to-equity ratio
    """
    if shareholders_equity == 0:
        return np.nan
    return total_debt / shareholders_equity


def calculate_asset_turnover(revenue: float, total_assets: float) -> float:
    """
    Calculate Asset Turnover Ratio.
    
    Asset Turnover = Revenue / Total Assets
    
    Args:
        revenue: Total revenue
        total_assets: Total assets
        
    Returns:
        Asset turnover ratio
    """
    if total_assets == 0:
        return np.nan
    return revenue / total_assets


def calculate_financial_ratios_dataframe(df: pd.DataFrame, 
                                        mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Calculate multiple financial ratios from a DataFrame.
    
    Args:
        df: Input DataFrame with financial data
        mapping: Dictionary mapping required columns to dataframe columns
        
    Returns:
        DataFrame with calculated ratios
    """
    ratios = pd.DataFrame()
    
    # Liquidity Ratios
    if 'current_assets' in mapping and 'current_liabilities' in mapping:
        ratios['current_ratio'] = df.apply(
            lambda row: calculate_current_ratio(row[mapping['current_assets']], 
                                               row[mapping['current_liabilities']]),
            axis=1
        )
    
    # Profitability Ratios
    if 'net_income' in mapping and 'revenue' in mapping:
        ratios['profit_margin'] = df.apply(
            lambda row: calculate_profit_margin(row[mapping['net_income']], 
                                               row[mapping['revenue']]),
            axis=1
        )
    
    if 'net_income' in mapping and 'total_assets' in mapping:
        ratios['roa'] = df.apply(
            lambda row: calculate_roa(row[mapping['net_income']], 
                                     row[mapping['total_assets']]),
            axis=1
        )
    
    if 'net_income' in mapping and 'shareholders_equity' in mapping:
        ratios['roe'] = df.apply(
            lambda row: calculate_roe(row[mapping['net_income']], 
                                     row[mapping['shareholders_equity']]),
            axis=1
        )
    
    return ratios
