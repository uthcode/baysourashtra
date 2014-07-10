import webapp2

from utils import step_by_step_template

class StepbyStepHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(step_by_step_template.render())