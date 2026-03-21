import requests

url = "http://127.0.0.1:8000/analyze"
files = {'resume': ('dummy.pdf', b'dummy content', 'application/pdf')}
data = {'jd_text': 'test job description'}

try:
    response = requests.post(url, files=files, data=data)
    print("STATUS CODE:", response.status_code)
    print("RESPONSE BODY:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print("CONNECTION ERROR:", str(e))
