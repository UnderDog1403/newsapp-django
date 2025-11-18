from ..models import Category

class CategoryRepository:
    def get_all(self):
        return Category.objects.all()
    def get_by_name(self,name):
        return Category.objects.filter(name=name).first()
    def get_by_id(self,id):
        return Category.objects.filter(id=id).first()
    def create_category(self,name):
        category = Category(name =name)
        category.save()
        return category
    def update_category(self, id, **kwargs):
        category =self.get_by_id(id=id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category
    def delete_category(self,id):
        category = Category.objects.filter(id=id).first()
        category.delete()
        return True
