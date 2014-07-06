from google.appengine.ext import ndb

class PersonEntityClass(ndb.Model):
  name = ndb.StringProperty(required=True)
  spouse = ndb.StringProperty(required=False)
  family = ndb.StringProperty(required=True)
  email = ndb.StringProperty(required=True)
  veg = ndb.IntegerProperty(default=0)
  nonveg = ndb.IntegerProperty(default=0)

