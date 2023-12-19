import requests

def get_historical_dollar_prices(api_key, start_date, end_date):
    base_url = "https://api.freecurrencyapi.com/v1/historical"
    base_currency = "USD"
    target_currency = "RUB"

    headers = {
        "apikey": api_key
    }

    params = {
        "base_currency": base_currency,
        "target_currency": target_currency,
        "start_date": start_date,
        "end_date": end_date
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage with multiple dates
api_key = "fca_live_a7wJo65vWDCC6bTs7magJRxY7ciZt6vCq7tWtLhk"
date_list = ["2023-01-01", "2023-04-04", "2023-07-07", "2023-10-10"]

for date in date_list:
    historical_data = get_historical_dollar_prices(api_key, date, date)

    if historical_data:
        print(f"Historical data for {date}: {historical_data}")
        # Process the historical data as needed
    else:
        print(f"Failed to retrieve historical data for {date}.")