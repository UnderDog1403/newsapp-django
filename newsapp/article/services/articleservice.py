from ..repositories.articlerepository import ArticleRepository


class ArticleService:
    def __init__(self):
        self.articlerepository = ArticleRepository()
    def get_articles_paginated(page, per_page):
        return ArticleRepository.get_paginated_articles(page, per_page)
    def get_article_paginated_by_categoryslug(self,categoryslug,page,per_page):
        data = self.articlerepository.get_by_categoryslug(categoryslug,page,per_page)
        return data
