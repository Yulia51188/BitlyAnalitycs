# Bitly url shorterer

The script get a string as argument and check is it a bitlink. If it is then the script calculates the number of clicks to the input bitlink. Else the script tries to make a bitlink from input long url.

# How to install

To use Bitly you need a Generic Access Token. To get it, please:
- register at [bitly](https://bitly.com/)
- get your individual Generic Access Token
- create the file `.env` with record:
```python
BITLY_TOKEN=<your generic access token>
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```
# How to launch

To launch the script to count clicks in Linux do:
```bash
$ python3 main.py bit.ly/2DG7KlR
The number of clicks to bit.ly/2DG7KlR is 0
```
or to make a bitlink:
```bash
$ python3 main.py https://dvmn.org/modules/web-api/lesson/migration-from-website/#7
The input string is not a bitlink.
Success! Your bitlink is: bit.ly/2DG7KlR
```
The launch in Windows or Mac Os is the same.

# Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.