from os.path import exists

from ..repositories.commentrepository import CommentRepository
from user.models import User

from article.models import Article


class CommentService:
    def __init__(self):
        self.commentrepository = CommentRepository()
    def get_all(self):
        return self.commentrepository.get_all()
    def get_by_article(self,article_slug):
        comments= self.commentrepository.get_by_article(article_slug)
        if comments is None:
            raise ValueError("khong co article")
        return comments
    def create_comment(self, comment, user, article):
        check_user = User.objects.filter(id=user).first()
        check_article = Article.objects.filter(id=article).first()
        if not check_user:
            raise ValueError("khong tim thay user")
        if not check_article:
            raise ValueError("khong tim thay article")
        return self.commentrepository.create_comment(comment,user,article)
    def change_comment(self,comment,id):
        newcomment= self.commentrepository.find_by_id(id)
        if not newcomment:
            raise ValueError("khong co comment")
        return self.commentrepository.change_comment(comment,id)
    def delete_comment(self,id):
        delete_comment =self.commentrepository.find_by_id(id)
        if not delete_comment:
            raise ValueError("khong tim thay comment")
        return self.commentrepository.delete_comment(id)