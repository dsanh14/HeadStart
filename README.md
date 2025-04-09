# Personal Finance Tracker

A Python-based personal finance tracking application that helps you record, categorize, analyze, and visualize your expenses and income. It also includes real-time stock price tracking capabilities.

## Features

- Track expenses and income
- Categorize transactions
- Visualize spending patterns
- View income vs expenses over time
- Check real-time stock prices
- MySQL database storage

## Prerequisites

- Python 3.9 or higher
- MySQL Server
- Alpha Vantage API key (optional, for stock data)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-finance-tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
   - Create a MySQL database named `finance_tracker`
   - Copy `.env.example` to `.env` and update the database credentials

5. Run the application:
```bash
python main.py
```

## Usage

1. Add expenses and income through the command-line interface
2. View visualizations of your spending patterns
3. Track stock prices (requires Alpha Vantage API key)

## Project Structure

- `main.py`: Main application entry point
- `database.py`: Database operations
- `visualization.py`: Data visualization functions
- `stock_data.py`: Stock market data retrieval
- `config.py`: Configuration settings
- `.env`: Environment variables (not in version control)

## License

MIT License
