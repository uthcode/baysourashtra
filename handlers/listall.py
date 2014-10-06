import webapp2
from models.person import PersonEntityClass
from utils import list_template

class ListAllHandler(webapp2.RequestHandler):
  def get(self):
    person_query = PersonEntityClass.query().fetch()
    values = {
      'allrecords': person_query,
      'total_registered': len(person_query),
      'total_adults': sum([p.adults for p in person_query]),
      'total_kids': sum([p.kids for p in person_query]),
      'total_payment': sum([p.total for p in person_query]),
      'total_received': sum([p.total for p in person_query if p.paid]),
    }

    self.response.write(list_template.render(values))
