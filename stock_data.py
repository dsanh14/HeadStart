import requests
from config import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_BASE_URL

def get_stock_price(symbol):
    """Get the current stock price for a given symbol"""
    if not ALPHA_VANTAGE_API_KEY:
        print("Alpha Vantage API key not found. Please set it in your .env file.")
        return None
    
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': ALPHA_VANTAGE_API_KEY
    }
    
    try:
        response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'Global Quote' in data:
            quote = data['Global Quote']
            return {
                'symbol': symbol,
                'price': float(quote['05. price']),
                'change': float(quote['09. change']),
                'change_percent': quote['10. change percent']
            }
        else:
            print(f"No data found for symbol {symbol}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return None 