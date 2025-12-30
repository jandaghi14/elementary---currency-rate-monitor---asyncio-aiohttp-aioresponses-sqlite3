# Currency Rate Monitor

A Python async application that fetches real-time exchange rates for multiple currencies concurrently and stores them in a SQLite database.

## Features

- Fetches exchange rates for 5 major currencies (EUR, GBP, JPY, INR, CAD)
- Concurrent API calls using asyncio for better performance
- Robust error handling (timeout, bad status, network errors)
- SQLite database storage with context manager
- Comprehensive test coverage with pytest
- Professional error logging

## Technologies Used

- **Python 3.7+**
- **aiohttp** - Async HTTP client
- **asyncio** - Asynchronous programming
- **SQLite3** - Database storage
- **pytest** - Testing framework
- **aioresponses** - Mocking async HTTP responses

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/currency-rate-monitor.git
cd currency-rate-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the currency rate fetcher:
```bash
python rate_fetcher.py
```

The application will:
- Fetch current exchange rates for EUR, GBP, JPY, INR, and CAD
- Calculate rates against USD
- Store results in `CurrencyCache.db`
- Display any errors encountered

## Running Tests

Run all tests:
```bash
pytest test_rate_fetcher.py -v
```

Test coverage includes:
- Successful API response handling
- Timeout error handling
- Bad HTTP status handling
- Network error handling

## Project Structure

```
currency-rate-monitor/
├── rate_fetcher.py          # Main async fetcher
├── database.py              # Database context manager
├── test_rate_fetcher.py     # Test suite
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

## API Used

- **ExchangeRate-API**: Free currency exchange rate API
- No authentication required for basic usage

## Error Handling

The application handles:
- **Timeout errors**: 10-second timeout per request
- **HTTP errors**: Non-200 status codes
- **Network errors**: Connection failures and other client errors

## Future Enhancements

- Add more currencies
- Historical rate tracking and trends
- Rate change notifications
- Web dashboard for visualization
- Export data to CSV/Excel

## License

MIT License