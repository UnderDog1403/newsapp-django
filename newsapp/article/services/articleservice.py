from rest_framework.exceptions import NotFound

from ..repositories.articlerepository import ArticleRepository


class ArticleService:
    def __init__(self):
        self.articlerepository = ArticleRepository()

    def get_articles_paginated(self, page, per_page):
        data = self.articlerepository.get_paginated_articles(page, per_page)
        if not data:
            raise ValueError("Không có bài viết nào")
        return data
    def get_article_paginated_by_categoryslug(self,categoryslug,page,per_page):
        data = self.articlerepository.get_by_categoryslug(categoryslug,page,per_page)
        if data is None:
            raise NotFound("Không có thể loại này")
        if data.paginator.count == 0:
            raise ValueError("Không có bài viết nào")
        return data
    def get_articles_paginated_featured(self,page,per_page):
        data = self.articlerepository.get_feature_articles(page,per_page)
        if not data:
            raise ValueError("Không có bài viết nào")
        return data
    def get_by_slug(self, slug):
        data = self.articlerepository.get_by_articleslug(slug)
        if not data:
            raise ValueError("Không có bài viết nào")
        return data
