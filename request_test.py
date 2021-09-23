import requests

data = {"male":1,
        "age":1,
        "education":1,
        "cigsPerDay":1,
        "sysBP":1,
        "heartRate":1,
        "TenYearCHD":1}
#10.40.0.10
#127.0.0.1
url = "http://127.0.0.1:8000/api/m/get_predictions_one?name=test3&data=%s&target=TenYearCHD"%(data)
data = requests.get(url=url)
print(data.text)