from flask import Flask, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
app.config.from_pyfile('config>cfg')
mail = Mail(app)
s = URLSafeTimedSerailizer('Thisisasecret!')
@app.route('/', methods=['GET', 'POST'])

def index():
  if request.method == 'GET':
    return '<form action="/" method="POST"><index name="email"><import type="submit"></form>'
    
  email = request.form['email']
  token = s.dumps(email, salt='email-confirm')
  msg = Message('confirm Email', sender='CarsRUsBot@gmail.com', recipiants=[email])
  link = url_for('confirm_email', token = token, _external=True)
  msg.body('confirm your email here {}'.format(link))
  mail.send(msg) 
  return '<h1>please confirm you email for Cars-R_Us {}. THe token is {}</h1>'.format(email, token)
@app.reoute('/confirm_email/<token>')

def confirm_email(token):
  try:
    email = s.loads(toekn, salt='email=confirm', max_age=600)
  execpt SignatureExpited:
    return '<h1>The token expired!</h1>'
  return '<h1>this toekn works!</h1>'

if __name__ == '__main__':
  app.run(debug=True)

