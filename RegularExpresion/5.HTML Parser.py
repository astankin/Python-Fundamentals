import re

text = input()
title_regex = r'<title>([^<>]*)<\/title>'
title = re.search(title_regex, text).group(1)
body_regex = r'<body>.*<\/body>'
body = re.findall(body_regex, text)[0]
content_regex = r">([^><]*)<"
content = re.findall(content_regex, body)
content = ''.join(content)
content = content.replace('\\n', '')
print(f"Title: {title}")
print(f'Content: {content}')

