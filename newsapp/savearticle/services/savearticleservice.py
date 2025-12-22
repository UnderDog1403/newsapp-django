from ..repositories.savearticlerepository import SavearticleRepository
from user.repositories.userrepository import UserRepository


class SavearticleService:
    def __init__(self):
        self.reponsitory = SavearticleRepository()
        self.userrepon = UserRepository()
    def get_all(self):
        return self.reponsitory.get_all()
    def get_by_id(self,id):
        result = self.reponsitory.get_by_id(id)
        if result is None:
            raise ValueError("khong ton tai bai viet nay" )
        return result
    def get_paginated_savearticle(self,user_id, page, per_page):
        user = self.userrepon.get_by_id(user_id)
        if user is None:
            raise ValueError("khong ton tai user")
        result = self.reponsitory.get_paginated_savearticle(user_id,page,per_page)
        if not result:
            raise ValueError("khong co bai viet nao")
        return result
    def delete_savearticle(self,id):
        delete_aticle = self.reponsitory.get_by_id(id)
        if delete_aticle is None:
            raise ValueError("khong ton tai bai viet nay")
        self.reponsitory.delete_savearticle(id)
        return True

