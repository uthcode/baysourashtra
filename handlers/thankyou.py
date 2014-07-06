import webapp2

from utils import thankyou_template

class ThankyouHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(thankyou_template.render())