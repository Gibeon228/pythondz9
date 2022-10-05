import requests

city = input("Введите название города(например Лондон) => ")
print(city)

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)