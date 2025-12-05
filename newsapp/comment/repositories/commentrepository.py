
from ..models import Comment
class CommentRepository:
    def get_all(self):
        return Comment.objects.all()
    def create_comment(self,comment,user,article):
        comment =Comment(comment=comment, user=user, article= article)
        comment.save()
        return comment
    def change_comment(self,comment, id):
        return Comment.objects.filter(id=id).update(comment=comment)
