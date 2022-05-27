import requests

token="1954972158:AAGksFgEIsJWyeo2yM6YUjVfQgnS4DQvhZE"
method = "sendMessage"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={"chat_id": 1035687268, 'text': "Salom /start yoqib qoldimi?"}
    ).json()
print(response)