# download a picture from a web
import urllib.request

response = urllib.request.urlopen("file:///E:/PythonLearning/Webpage55.html")

gakki_img = response.read()

with open("gakki_lesson 55.jpg","wb") as f:
    f.write(gakki_img)

# python translator lesson 55