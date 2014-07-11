import webapp2
from models.person import PersonEntityClass
from utils import list_template

class ListAllHandler(webapp2.RequestHandler):
  def get(self):
    person_query = PersonEntityClass.query().fetch()
    values = {
      'allrecords': person_query
    }
    self.response.write(list_template.render(values))
