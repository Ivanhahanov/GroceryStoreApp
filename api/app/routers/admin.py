from fastapi import APIRouter
from . import *

router = APIRouter()
db = mongo.store


@router.get('/users')
def users_list(current_user: User = Depends(get_current_user_if_admin)):
    return {'username': current_user.username, 'users': list(db.users.find({}, {'_id': False}))}


