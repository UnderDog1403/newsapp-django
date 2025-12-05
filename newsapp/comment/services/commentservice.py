
from ..repositories.commentrepository import CommentRepository
class CommentService:
    def __init__(self):
        self.commentrepository = CommentRepository()

    def create_comment(self, comment, user, article):
        return self.commentrepository.create_comment(comment,user,article)
    def change_comment(self,comment,id):
        return self.commentrepository.change_comment(comment,id)
