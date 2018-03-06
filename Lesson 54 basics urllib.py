import urllib.request

response = urllib.request.urlopen("file:\E:\PythonLearning\Webpage.html")
html = response.read()
print(html)

html = html.decode("utf-8")
print(html)