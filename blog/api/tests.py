from rest_framework.test import APITestCase
from blog.models import BlogPost

class blogAPITestCase(APITestCase):
    def setUp(self):
        BlogPost.objects.create(title="Software Engineer", body="xyz..dfsdfsfs.sd.fs.f.sf.sd.fs.fs.df.sf.sfsfsfsfsfs",
                                image=None,date_published=True,date_updated=True,author="dinesh")

        title = models.CharField(max_length=60, null=False, blank=True)
        body = models.TextField(max_length=50000, null=False, blank=True)
        image = models.ImageField(upload_to=upload_location, null=False, blank=True)
        date_published = models.DateTimeField(auto_now_add=True, verbose_name='date published')
        date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        slug = models.SlugField(blank=True, unique=True)
