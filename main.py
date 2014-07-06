import webapp2

from handlers import PersonHandler, PaypalHandler, ThankyouHandler

app = webapp2.WSGIApplication(
  [('/', PersonHandler),
   ('/pay/(.*)', PaypalHandler),
   ('/thanks', ThankyouHandler)
  ],
  debug=True)
