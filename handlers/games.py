import webapp2

from utils import games_template

class GamesHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(games_template.render())
