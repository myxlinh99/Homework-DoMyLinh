from gmail import *
import random

r = [r.strip() for r in (open("contents.txt",encoding = "utf-8").readlines())]
print(r)
print(random.choice(r))

gmail = GMail('<c4e.201708@gmail.com >','codethechange')

html_content = open("content.txt", encoding = "utf-8").read()

html_content = html_content.replace("{reason}", (random.choice(r)))

msg = Message('1234',to='<c4e.201708@gmail.com>',html = html_content)
gmail.send(msg)
