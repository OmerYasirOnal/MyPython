import requests
from datetime import datetime

# API anahtarınızı buraya girin
api_key = 'f151e8ff780975f3ef74b337fe8027cd'

# Hava durumu bilgisi almak istediğiniz şehri buraya girin
city_name = 'istanbul'

# API isteği için URL oluşturma
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

# API'ye istek gönderme ve yanıtı alınması
response = requests.get(url)

# Yanıtın durum kodunu kontrol edin
if response.status_code == 200:
    # JSON verilerini alın
    data = response.json()
    
    # Sıcaklık birimi Celsius olduğu için Kelvin'den dönüştürme
    temperature = round(data['main']['temp'] - 273.15, 1)
    
    # Unix zaman damgasını datetime objesine dönüştürme
    dt = datetime.fromtimestamp(data['dt'])
    
    # Şehir adı, sıcaklık değeri ve tarih bilgisini yazdırma
    print(f"Hava durumu bilgisi {city_name} için:")
    print(f"Sıcaklık: {temperature}°C")
    print(f"Tarih: {dt}")
else:
    # Yanıt durum kodu hatalı ise hata mesajı yazdırın
    print("Hata: API'ye istek gönderilemedi.")
