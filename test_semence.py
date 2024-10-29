import requests
token_str="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODY1NjQ3LCJpYXQiOjE3Mjk4NjUzNDcsImp0aSI6IjZjOTM4YWU2MmI1ZDRiMjU4MzI4ZTNjODAzZGY1MTZiIiwidXNlcl9pZCI6MTcsImVtYWlsIjoic3VzYW50ZXN0QGdtYWlsLmNvbSIsInRlbGVwaG9uZSI6IjEyMzQ1Njc4OTAifQ.9RfWyhkNi5FEXNs7w1ZiqKxPIE17E0D8IDjcjCuZ_Ik"
headers = {"Authorization": f"Bearer {token_str}"}
response = requests.get("http://127.0.0.1:8001/syst_type_semences/", headers=headers)
print(response.json())
