from flask import make_response, abort
from app.models.cat import Cat
from app.models.caretaker import Caretaker

def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    cat = Cat.query.get(id)

    if not cat:
        abort(make_response({"message":f"cat {id} not found"}, 404))
    
    return cat

def validate_caretaker(caretaker_id):
    try:
        caretaker_id = int(caretaker_id)
    except:
        abort(make_response({"message":f"caretaker {caretaker_id} invalid"}, 400))
    caretaker = Caretaker.query.get(caretaker_id)
    if not caretaker:
        abort(make_response({"message":f"caretaker {caretaker_id} not found"}, 404))
    return caretaker