# birthday-finder
This is an app where you will be given a message if it is your birthday today. 
1. Add your datafiles_birthdays.json in the given format. 
2. Create a Twilio account and obtain your      ```ACCOUNT_SID``` and ```AUTH_TOKEN```.
3. Export ```FROM``` phone number ```ACCOUNT_SID``` and ```AUTH_TOKEN``` to your local environment variable. 

```
export FROM=yourtwiliophonenumber
export AUTH_TOKEN=twilioauthtoken
export AUTH_SID=twilioauthsid
```

Lastly run python3 app.py, to run the program. 