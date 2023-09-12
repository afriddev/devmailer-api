


# pythonemailapi
  pythonemailapi is written in pure python with the help of fastapi,you can sned emails by using this api and seamlessly integrate this api in you code very easily

## Use in your code 
- [python](https://pypi.org/project/emailotp/)
- [dart](https://pub.dev/packages/email_sender)
  
## Installing dependencies
  Install required modules for this project

```
pip install -r requirements.txt
```

## run
  Run the server from your local machine
```python
 python main.py
```

## Useage
```python
pip install requests
import requests
response = requests.get('http://0.0.0.0:8000')
print(response.json())  

```
## sendEmail
```python
pip install requests
import requests
response = requests.post('http://0.0.0.0:8000/sendEmail',
  json={
      "toEmail":"toemail@gmail.com"
          }
  )
print(response.json())  

```
## generate app password

-  [Click Here](https://support.google.com/accounts/answer/185833?hl=en)

## default credentials
if you dont pass this params automaticall api will send email with default credentials
```json
{
  "fromEmail":"defaultemailapi@gmail.com",
  "passkey":"my 16 digits passkey"
}

```

## post json format
```json

  {
      "fromEmail":"fromemail@gmail.com",
      "passkey":"16 DIGITS PASS KEY",  
      "toEmail":"toemail@gmail.com",
      "title":"your title",
      "subject":"your subject",
      "body":"your body message"
  }
  
```



## Authors

- [SHAIK AFRID](https://www.github.com/afriddev)



