import requests
import matplotlib.pyplot as plt

api_key = 'fca_live_a7wJo65vWDCC6bTs7magJRxY7ciZt6vCq7tWtLhk'
base_url = 'https://api.freecurrencyapi.com/v1/historical'
base_currency = 'USD'
target_currency = 'RUB'
dates = ['2023-01-01', '2023-02-02', '2023-04-04', '2023-06-06', '2023-08-08', '2023-10-10', '2023-12-12']

result_list = []

for date in dates:
    params = {
        'apikey': api_key,
        'base_currency': base_currency,
        'target_currency': target_currency,
        'date': date
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            # Получаем стоимость 1 доллара в рублях
            price = data['data'][date][target_currency]
            result_list.append((date, price))
        except KeyError:
            print(f'Ошибка при извлечении данных для даты {date}.')
    else:
        print(f'Ошибка при запросе данных для даты {date}. Код ответа: {response.status_code}')

# Извлекаем даты и цены для построения графика
dates, prices = zip(*result_list)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, marker='o')
plt.title(f'Стоимость 1 {base_currency} в {target_currency}')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Отображение графика
plt.show()
