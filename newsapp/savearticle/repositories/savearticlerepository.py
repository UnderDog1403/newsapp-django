from django.core.paginator import Paginator

from ..models import SaveArticle
class SavearticleRepository:
    def get_all(self):
        return SaveArticle.objects.all()
    def get_by_id(self,id):
        return SaveArticle.objects.filter(id=id).first()
    def get_paginated_savearticle(self,user_id,page=1,per_page=5):
         articles= SaveArticle.objects.filter(user__id=user_id).all().order_by('create_at')
         paginator = Paginator(articles,per_page)
         return paginator.get_page(page)
    def delete_savearticle(self,id):
        article = self.get_by_id(id)
        article.delete()
        return True


