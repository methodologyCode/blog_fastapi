from db.models import DbComment
from db.service import MixinObject


class Comment(MixinObject):
    model = DbComment
