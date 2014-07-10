import webapp2

from handlers import PersonHandler, PaypalHandler, ThankyouHandler, CancelHandler, StepbyStepHandler

app = webapp2.WSGIApplication(
  [('/', PersonHandler),
   ('/pay/(.*)', PaypalHandler),
   ('/thanks/(.*)', ThankyouHandler),
   ('/cancel', CancelHandler),
   ('/stepbystep', StepbyStepHandler)
  ],
  debug=True)
