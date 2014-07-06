import webapp2

from models.person import PersonEntityClass
from utils import form_template

class PersonHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(form_template.render({}))

  def post(self):
    name = self.request.get("name")
    spouse = self.request.get("spouse")
    family = self.request.get("family")
    email = self.request.get("email")
    veg = int(self.request.get("veg", 0))
    nonveg = int(self.request.get("nonveg", 0))
    form_values = {
      'name':name,
      'spouse': spouse,
      'family': family,
      'email': email,
      'veg': veg,
      'nonveg': nonveg
    }
    person_entity = PersonEntityClass(**form_values)
    person_entity.put()
    self.redirect('/pay/%s' % email)
