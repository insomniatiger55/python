import faust
from datetime import datetime
class Order(faust.Record):
    acct_id: str 
    amount: float

class userINFO(faust.Record,isodates=True, serializer='json'):
    timestamp: str 
    name: str
    address: str
    created_at:int    