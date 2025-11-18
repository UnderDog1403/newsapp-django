from ..repositories.categoryrepository import CategoryRepository
class CategoryService:
    def __init__(self):
        self.categoryrepository = CategoryRepository()
    def list_category(self):
        return self.categoryrepository.get_all()
    def get_category(self, id):
        category=self.categoryrepository.get_by_id(id)
        if not category:
            raise ValueError("Khong co category nay")
        return category
    def create_category(self,name):
        if not name:
            raise ValueError("Khong dc de trong ten")
        return self.categoryrepository.create_category(name)
    def update_category(self,id,**kwargs):
        category = self.categoryrepository.get_by_id(id)
        if not category:
            raise ValueError("Khong tim thay category")
        return self.categoryrepository.update_category(id,**kwargs)
    def delete_category(self, id):
        category = self.categoryrepository.get_by_id(id)
        if not category:
            raise ValueError("Khong tim thay category")
        return self.categoryrepository.delete_category(id)


