import requests
import json

url = "https://wxcentral.medinfo-sanofi.cn/api/weixin/getmenus?appId=wx96dd1199091f4ea8"
proxy_servers = {
    'http': 'http://127.0.0.1:9000',
    'https': 'http://127.0.0.1:9000',
}
payload = {}
headers = {
    'Accept': 'text/plain',
    'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjE0YjJlMTQ0ZjM4YmZlMzExOWRhZTBiOWJlN2RkNGRjIiwidHlwIjoiSldUIn0.eyJuYmYiOjE2ODQ4MzU4OTAsImV4cCI6MTY4NDgzNzY5MCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5tZWRpbmZvLXNhbm9maS5jbiIsImF1ZCI6WyJodHRwczovL2lkZW50aXR5Lm1lZGluZm8tc2Fub2ZpLmNuL3Jlc291cmNlcyIsIndlY2hhdF9hcGkiLCJzZW1pbmFyX2FwaSJdLCJjbGllbnRfaWQiOiJhdXRob3JpemF0aW9uX2NvZGUiLCJzdWIiOiI2Q0UwQUM2NC02ODc1LTQ3NUYtODBDNy0yNkRGNzI4RUMxOTQiLCJhdXRoX3RpbWUiOjE2ODQ4MzU4ODQsImlkcCI6ImxvY2FsIiwibmFtZSI6IuacseWPi-aZtiIsInJvbGUiOlsic2VjdXJpdHlfYWRtaW4iLCJubXIiXSwiZW1haWwiOiJjaHJpcy56aHVAc2Fub2ZpLmNvbSIsInNjb3BlIjpbIndlY2hhdF9hcGkiLCJzZW1pbmFyX2FwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJwd2QiXX0.VRv65ctIxSrGQMzneMFIdOE7Yi62Ea7WoNv_D3gLHWtlQ35jjwNZ5QK_muxrGnCjri8RxPFEwIgMyCgF5R5JC05Yya_YM4kcKRcYpYERAZcYx6wZ9ZIAWMupo3Vq5yvkpwdW9z3DHEusMOWhO17udWaZMxTrNFkq9i4I5FpgetiYIUOhjssklwmFwTjlFmCYpUdoPY_kJW11K1Dgj9cF6su62AsJFHpinL1NcxldoYobaSXEhh7mI6g1nCXxXBnuhx9WcAxO9Plzs2vFVj8fWHUCfwq9gUewr-39URMTcwYGRnnojN9IRmDursrBOanYqvPhaTDenOPnu5SyVq8AsA'
}


def parse_tags():
    for item in response_json['tags']:
        print(f'{item["id"]}\t{item["name"]}')


def parse_menus():
    for menu in response_json['conditionalmenu']:
        match_rule = menu['matchrule']
        print(match_rule['group_id'])


response = requests.request("GET", url, headers=headers, data=payload, proxies=proxy_servers)
# print(response.text)
response_json = json.loads(response.text)
parse_menus()