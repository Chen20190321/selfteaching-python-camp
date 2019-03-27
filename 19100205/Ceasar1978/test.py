text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text = text.replace("better","worse")
print(text)

list_text = text.split()
list_text1 = []
for i in list_text:
    if "ea" not in i:
        list_text1.append(i)
text = " ".join(list_text1)
print(text)

text = text.swapcase()
print(text)

text = text.replace(",","")
text = text.replace("--","")
text = text.replace("!","")
text = text.replace("*","")
text = text.replace(".","")

list_text = text.split()
list_text.sort()
print(list_text)

