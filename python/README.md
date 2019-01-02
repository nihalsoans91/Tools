# Python Tools

### rcn_ano_convert.py
Used to convert a XML file into a lables txt for Faster RCN especially when you are using LabelME from MIT

### downloadfiles.py
Downloads files from http protocol 

### mailer.py
Send email from anywhere provided there is connection to internet using python
#### Usage:
##### Initilize
```python
import mailer
m=mailer("username","password","toaddress")
```
Username has to be full email address example: name@gmail.com
##### To send
```python
m.sendmail(<content as a string>,<subject as a string>)
```
