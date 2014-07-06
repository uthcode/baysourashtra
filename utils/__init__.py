import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
  # templates directory is relative to app root.
  loader=jinja2.FileSystemLoader('templates'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

form_template = JINJA_ENVIRONMENT.get_template('form.html')
pay_template = JINJA_ENVIRONMENT.get_template('paypal.html')
thankyou_template = JINJA_ENVIRONMENT.get_template('thankyou.html')
