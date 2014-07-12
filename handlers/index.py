import webapp2

from utils import index_template

class IndexHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(index_template.render())