import webapp2

from handlers import PersonHandler, PaypalHandler, ThankyouHandler, CancelHandler

app = webapp2.WSGIApplication(
  [('/', PersonHandler),
   ('/pay/(.*)', PaypalHandler),
   ('/thanks/(.*)', ThankyouHandler),
   ('/cancel', CancelHandler)
  ],
  debug=True)
