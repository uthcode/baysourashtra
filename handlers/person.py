import webapp2

from models.person import PersonEntityClass
from utils import form_template, veg_cost, non_veg_cost


class PersonHandler(webapp2.RequestHandler):
  def get(self):
    values = {
      'veg_cost' : veg_cost,
      'non_veg_cost': non_veg_cost
    }
    self.response.write(form_template.render(values))

  def post(self):
    name = self.request.get("name")
    spouse = self.request.get("spouse")
    family = self.request.get("family")
    email = self.request.get("email").lower()
    veg = int(self.request.get("veg", 0))
    nonveg = int(self.request.get("nonveg", 0))
    total_veg_cost = veg * veg_cost
    total_non_veg_cost = nonveg * non_veg_cost
    total = total_veg_cost + total_non_veg_cost

    form_values = {
      'id': email,
      'name':name,
      'spouse': spouse,
      'family': family,
      'email': email,
      'veg': veg,
      'nonveg': nonveg,
      'total_veg_cost': total_veg_cost,
      'total_non_veg_cost': total_non_veg_cost,
      'total': total,
    }
    person_query = PersonEntityClass.query(PersonEntityClass.email==email)
    if person_query.count() and person_query.fetch()[0].paid:
      self.redirect('/thanks/%s' % email)
    else:
      person_entity = PersonEntityClass(**form_values)
      person_entity.put()
      self.redirect('/pay/%s' % email)
