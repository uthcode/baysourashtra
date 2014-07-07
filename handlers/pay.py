import webapp2
from models.person import PersonEntityClass

from utils import pay_template

class PaypalHandler(webapp2.RequestHandler):
  def get(self, email):
    person = PersonEntityClass.query(PersonEntityClass.email==email).fetch()[0]
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