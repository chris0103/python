import re


pattern = r'[a-zA-Z0-9_-]{18}'
string = '/api/WeChatUsers/WeChatUsers/o1g3rv9sJ_lemwEPkDvhVsonFV2k'

print(re.search(pattern, string))

if re.search(pattern, string):
    print('Union ID found')
else:
    print('Union ID not found')
