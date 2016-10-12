import webapp2

from models.person import PersonEntityClassDiwali2016
from utils import paypal_balance_template

class PayPalBalanceHandler(webapp2.RequestHandler):
    def get(self, email):
        if email:
            person_query = PersonEntityClassDiwali2016.query(PersonEntityClassDiwali2016.email == email)
            if person_query.count():
                person = person_query.fetch()[0]
                values = {
                    'total_food_cost': person.total,
                }
                self.response.write(paypal_balance_template.render(values))
        else:
            self.redirect('/')
