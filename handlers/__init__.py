__all__ = ['PaypalHandler', 'PersonHandler', 'ThankyouHandler', 'CancelHandler', 'StepbyStepHandler', 'ListAllHandler', 'IndexHandler']

from .person import PersonHandler
from .pay import PaypalHandler
from .thankyou import ThankyouHandler
from .cancel import CancelHandler
from .stepbystep import StepbyStepHandler
from .listall import ListAllHandler
from .index import IndexHandler
from .games import GamesHandler