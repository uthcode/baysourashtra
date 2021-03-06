import webapp2

from handlers import PersonHandler, PaypalHandler, ThankyouHandler, CancelHandler, StepbyStepHandler, \
  ListAllHandler, IndexHandler

app = webapp2.WSGIApplication(
  [('/', PersonHandler),
   ('/pay/(.*)', PaypalHandler),
   ('/thanks/(.*)', ThankyouHandler),
   ('/cancel', CancelHandler),
   ('/stepbystep', StepbyStepHandler),
   ('/list', ListAllHandler),
   ('/index', IndexHandler)
  ],
  debug=True)
