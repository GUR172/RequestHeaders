import re

headers_text = '''
在此填入请求头
'''
if 'cookie:' in headers_text:
    cookie_text = re.findall('cookie:(.*?)\n', headers_text)[0]
    headers_text = headers_text.replace('\ncookie:' + cookie_text, '')
    cookie_list = cookie_text.split(';')
    cookie_dict = {}
    for i in cookie_list:
        i = i.split('=')
        cookie_dict[i[0]] = i[1]
    print(cookie_dict)
    print('-'*50)
pattern = '^(.*?):(.*)$'
headers = ''
for line in headers_text.splitlines():
    headers = headers + re.sub(pattern, '\'\\1\':\'\\2\',', line) + '\n'
print(headers)