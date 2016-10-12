import webapp2

from handlers import PersonHandler, PaypalHandler, ThankyouHandler, CancelHandler, StepbyStepHandler, \
  ListAllHandler, IndexHandler, GamesHandler, PayPalBalanceHandler

app = webapp2.WSGIApplication(
  [('/', PersonHandler),
   ('/pay/(.*)', PaypalHandler),
   ('/thanks/(.*)', ThankyouHandler),
   ('/cancel', CancelHandler),
   ('/stepbystep', StepbyStepHandler),
   ('/list', ListAllHandler),
   ('/index', IndexHandler),
   ('/paypalbalance/(.*)', PayPalBalanceHandler)
  ],
  debug=True)
