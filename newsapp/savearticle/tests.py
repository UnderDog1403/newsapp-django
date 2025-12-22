from django.test import TestCase

from savearticle.savearticlefactory import SaveArticleFactory
from .services.savearticleservice import SavearticleService

class SaveArticleServiceTest(TestCase):
    def setUp(self):
        self.save_article = SaveArticleFactory.create_batch(10)
    def test_get_by_id(self):
        service = SavearticleService()
        # print(service.get_all())
        print(service.get_paginated_savearticle(2,1,1))
        # print(service.get_by_id(1))      # test id tồn tại
        # print(service.get_by_id(9999))   # test id không tồn tại