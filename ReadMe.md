# Email Service 

Simple Django REST API for Email Service to customers using SendGrid and MailGun email service providers. 

## Steps to build
- Source a virtual environment
- Change directory to repo folder.
  Install dependencies:
  `pip3 install -r requirements.txt`
- Migrate:<br/>
    `python3 manage.py makemigrations`<br/>
    `python3 manage.py migrate`

## Run
  Run server:<br/>
  `python3 manage.py runserver`<br/>
  API Endpoint<br/>
  - For development server:
  `http://127.0.0.1:8000/API/`
  - For hosted server:
  `https://eserviceapp.herokuapp.com/API/`


  Change email address to your personal in API/settings.py as a value for `EMAIL_ADDRESS`
  Register on SendGrid and MailGun to obtain a credentials and an API Key through SMTP method.
  Add the keys in a file .env


## Testing
`python3 manage.py test`

## Functionalities
- GET /API<br/>
    Returns a list of all email requests.
- POST /API<br/>
    Form data = {<br/>
        'email_address': 'to@example.com',<br/>
        'mail_subject':'subject',<br/>
        'mail_body':'message'<br/>
    }

## Design
[<img src="https://i.imgur.com/iUeCqTI.jpg" alt="Design">]

## Assumptions
- Customers using this service can input an email address, subject, message and in return expect an email from the service.
- Database attachment for saving requests from customers.
- Usage of Factory pattern assuming providers might be updated/added by making changes in the Providers / ProviderFactory.


