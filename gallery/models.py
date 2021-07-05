from django.db import models

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        class Meta:
            ordering = ["name"]
            verbose_name = "Location"
            verbose_name_plural = "Locations"
        
        
    def save_location(self):
        self.save()
        
    
    def delete_location(self):
        self.delete()

class Image(models.Model):
    label = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/", default='logo.png')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    year_taken = models.DateField(auto_now_add=False, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label 

    class Meta:
        ordering = ['-uploaded_at']
    
    # search photos by category
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
