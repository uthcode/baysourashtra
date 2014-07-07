import webapp2

from utils import cancel_template

class CancelHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(cancel_template.render())
