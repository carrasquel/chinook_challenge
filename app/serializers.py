import json

from .encoders import AlchemyEncoder

def to_dict(obj):

    return json.loads(json.dumps(obj, cls=AlchemyEncoder))
