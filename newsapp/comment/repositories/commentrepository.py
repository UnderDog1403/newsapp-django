
from ..models import Comment
class CommentRepository:
    def get_all(self):
        return Comment.objects.all()
    def get_by_article(self,article_slug):
        return Comment.objects.filter(article__slug=article_slug).all()
    def find_by_id(self,id):
        return Comment.objects.filter(id=id).first()
    def create_comment(self,comment,user_id,article_id):
        comment = Comment(comment=comment, user_id=user_id, article_id=article_id)
        comment.save()
        return comment
    def change_comment(self,comment, id):
        newcomment = Comment.objects.get(id=id)
        newcomment.comment =comment
        newcomment.save()
        return newcomment
    def delete_comment(self, id):
        comment = self.find_by_id(id)
        comment.delete()
        return True
