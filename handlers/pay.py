import webapp2
from models.person import PersonEntityClassDiwali2014

from utils import pay_template, form_template, cancel_template, email_template, thankyou_template
from utils.email import send_email


class PaypalHandler(webapp2.RequestHandler):
  def get(self, email):
    if email:
      person_query = PersonEntityClassDiwali2014.query(PersonEntityClassDiwali2014.email==email)
      if person_query.count():
        person = person_query.fetch()[0]
        values = {
          'name': person.name,
          'spouse': person.spouse,
          'family': person.family,
          'adults': person.adults,
          'kids': person.kids,
          'total_adults_cost': person.total_adults_cost,
          'total_kids_cost': person.total_kids_cost,
          'total_food_cost': person.total,
          'email': person.email
        }
        self.response.write(pay_template.render(values))
        if not person.email_sent:
          person.email_sent = True
          person.put()
          send_email(**values)
      else:
        self.response.write(cancel_template.render())
    else:
      self.redirect('/')