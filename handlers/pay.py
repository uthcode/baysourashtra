import webapp2
from models.person import PersonEntityClass

from utils import pay_template, form_template, cancel_template, email_template
from utils.email import send_email


class PaypalHandler(webapp2.RequestHandler):
  def get(self, email):
    if email:
      person_query = PersonEntityClass.query(PersonEntityClass.email==email)
      if person_query.count():
        person = person_query.fetch()[0]
        values = {
          'name': person.name,
          'spouse': person.spouse,
          'family': person.family,
          'veg': person.veg,
          'total_veg_cost': person.total_veg_cost,
          'nonveg': person.nonveg,
          'total_non_veg_cost': person.total_non_veg_cost,
          'total_food_cost': person.total,
          'email': person.email
        }
        self.response.write(pay_template.render(values))
        send_email(values)
      else:
        self.response.write(cancel_template.render())
    else:
      self.redirect('/')