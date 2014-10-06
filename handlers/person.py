import webapp2

from models.person import PersonEntityClass
from utils import form_template, veg_cost, non_veg_cost, thankyou_template, \
    adults_cost, kids_cost


class PersonHandler(webapp2.RequestHandler):
  def get(self):
    values = {
      'veg_cost' : veg_cost,
      'non_veg_cost': non_veg_cost,
      'adult_cost': adults_cost,
      'kids_cost': kids_cost
    }
    self.response.write(form_template.render(values))

  def post(self):
    self.redirect("/thanks/")

  def _post(self):
    name = self.request.get("name")
    spouse = self.request.get("spouse")
    family = self.request.get("family")
    email = self.request.get("email").lower()
    veg = int(self.request.get("veg", 0))
    nonveg = int(self.request.get("nonveg", 0))
    adults = int(self.request.get("adults", 0))
    kids = int(self.request.get("kids", 0))
    total_veg_cost = veg * veg_cost
    total_non_veg_cost = nonveg * non_veg_cost
    #total = total_veg_cost + total_non_veg_cost
    total_adults_cost = adults * adults_cost
    total_kids_cost = kids * kids_cost
    total = total_adults_cost + total_kids_cost

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
      'adults': adults,
      'kids': kids,
      'total_adults_cost': total_adults_cost,
      'total_kids_cost': total_kids_cost,
      'total': total,
    }
    person_query = PersonEntityClass.query(PersonEntityClass.email==email)

    if person_query.count() and person_query.fetch()[0].paid:
      self.redirect('/thanks/%s' % email)
    else:
      person_entity = PersonEntityClass(**form_values)
      person_entity.put()
      self.redirect('/pay/%s' % email)
