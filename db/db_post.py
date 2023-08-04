from db.models import DbPost
from db.service import MixinObject


class Post(MixinObject):
    model = DbPost
