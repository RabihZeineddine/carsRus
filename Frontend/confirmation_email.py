from flask import Flask
from flask import request
from flask import url_for
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

  token = s.dumps(email, salt='email-confirm')
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

