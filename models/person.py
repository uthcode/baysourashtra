from google.appengine.ext import ndb

class PersonEntityClass(ndb.Model):
  name = ndb.StringProperty(required=True)
  spouse = ndb.StringProperty(required=False)
  family = ndb.StringProperty(required=True)
  email = ndb.StringProperty(required=True)
  veg = ndb.IntegerProperty(default=0)
  nonveg = ndb.IntegerProperty(default=0)
  total_veg_cost = ndb.FloatProperty(default=0.0)
  total_non_veg_cost = ndb.FloatProperty(default=0.0)
  total = ndb.FloatProperty(default=0.0)

