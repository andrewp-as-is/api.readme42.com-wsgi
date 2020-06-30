from django.conf import settings
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.utils.text import slugify

class Template(models.Model):
    code = models.TextField()
    name = models.TextField()
    slug = models.TextField()
    description = models.TextField(null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    tsv = SearchVectorField(null=True)

    class Meta:
        db_table = 'template_template'
        managed=False

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/templates/%s/%s' % (self.created_by.login,self.slug)
