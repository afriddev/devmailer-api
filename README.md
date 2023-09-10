


# pythonemailapi
  pythonemailapi is written in pure python with the help of fastapi,you can sned emails by using this api and seamlessly integrate this api in you code very easily

## use in your code 
- [python](https://pypi.org/project/emailotp/)
- [dart](https://pub.dev/packages/email_sender)
  
## installing dependencies
  Install required modules for this project

```
pip install -r requirements.txt
```

## run
  Run the server from your local machine
```python
 python main.py
```

## useage
```python
pip install requests
import requests
response = requests.get('http://localhost:8000')
print(response.json())  

```
## sendEmail
```python
pip install requests
import requests
response = requests.post('http://localhost:8000/sendEmail',
  json={
      "toEmail":"toemail@gmail.com"
          }
  )
print(response.json())  

```
## generate passkey

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
      "title":"your titlt",
      "subject":"your subject",
      "body":"your body message"
  }
  
```



## Authors

- [SHAIK AFRID](https://www.github.com/afriddev)



