import requests
import matplotlib.pyplot as plt

url = 'https://freecurrencyapi.com/'
params = {'base_currency': 'USD', 'target_currency': 'RUB', 'apikey': 'fca_live_a7wJo65vWDCC6bTs7magJRxY7ciZt6vCq7tWtLhk'}

response = requests.get(url, params = params)
data = response.json()

if response.status_code == 200:
    history = data['data']['history']

    dates = [entry['timestamp'] for entry in history]
    rates = [entry['rate'] for entry in history]

    plt.plot(dates, rates, label = 'USD to RUB')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.title('График зависимости цены доллара в рублях')
    plt.legend()
    plt.show()
else:
    print('Ошибка при получении данных')