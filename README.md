pizza py
========

Script that lets you order pizza from http://www.pizzahut.com.ph/

Python + Selenium

Setup:

Create Virtualenv and install selenium:
```
$ mkvirtualenv -a <Projects path>/pizzapy --no-site-packages pizzapy
(pizzapy)$ sudo pip install selenium
```

Create a config dir and file which will contain your credentials:
```
(pizzapy)$ mkdir config
(pizzapy)$ cd config
(pizzapy)$ touch settings.py

```

In config/settings.py add this:
```
credentials = {'username': 'some@email.com', 'pwd': 'somepassword'}
```

Run the script:
```
(pizzapy)$ python main.py
```
