import webapp2

from models.person import PersonEntityClassDiwali2015
from utils import form_template, adults_cost, kids_cost


class PersonHandler(webapp2.RequestHandler):
  def get(self):
    values = {
      'adults_cost': adults_cost,
      'kids_cost': kids_cost
    }
    self.response.write(form_template.render(values))

  def post(self):
    name = self.request.get("name")
    spouse = self.request.get("spouse")
    family = self.request.get("family")
    email = self.request.get("email").lower()
    adults = int(self.request.get("adults", 0))
    kids = int(self.request.get("kids", 0))
    total_adults_cost = adults * adults_cost
    total_kids_cost = kids * kids_cost
    total = total_adults_cost + total_kids_cost

    form_values = {
      'id': email,
      'name':name,
      'spouse': spouse,
      'family': family,
      'email': email,
      'adults': adults,
      'kids': kids,
      'total_adults_cost': total_adults_cost,
      'total_kids_cost': total_kids_cost,
      'total': total,
    }
    person_query = PersonEntityClassDiwali2015.query(PersonEntityClassDiwali2015.email==email)

    if person_query.count() and person_query.fetch()[0].paid:
      self.redirect('/thanks/%s' % email)
    else:
      person_entity = PersonEntityClassDiwali2015(**form_values)
      person_entity.put()
      self.redirect('/pay/%s' % email)
