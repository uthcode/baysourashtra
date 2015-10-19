import jinja2

veg_cost = 10.00
non_veg_cost = 10.00
adults_cost = 21.00
kids_cost = 13.00

def format_currency(value):
    return "${:,.2f}".format(value)

JINJA_ENVIRONMENT = jinja2.Environment(
  # templates directory is relative to app root.
  loader=jinja2.FileSystemLoader('templates'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

JINJA_ENVIRONMENT.filters.update(
    {'format_currency': format_currency}
)

form_template = JINJA_ENVIRONMENT.get_template('form.html')
pay_template = JINJA_ENVIRONMENT.get_template('paypal.html')
thankyou_template = JINJA_ENVIRONMENT.get_template('thankyou.html')
cancel_template = JINJA_ENVIRONMENT.get_template('cancel.html')
step_by_step_template = JINJA_ENVIRONMENT.get_template('stepbystep.html')
email_template = JINJA_ENVIRONMENT.get_template('email_template.html')
list_template = JINJA_ENVIRONMENT.get_template('list.html')
index_template = JINJA_ENVIRONMENT.get_template('index.html')
