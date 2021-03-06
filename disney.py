import requests

data_url = "https://disneyworld.disney.go.com/vas/api/v1/park-reservation/eligibility/dates"

print(data_url)
res = requests.get(data_url, timeout=15)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)

print(res.text)
