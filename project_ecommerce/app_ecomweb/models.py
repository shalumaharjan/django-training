from django.db import models

# Create your models here.
class MetaDescription(models.Model):
    meta_title = models.CharField(max_length=255, blank=False, null=False)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.meta_title
    
class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=255, blank=False, null=False)
    site_logo = models.ImageField(upload_to='site_logo/')
    site_favicon = models.ImageField(upload_to='site_favicon/')
    contact_email = models.EmailField(unique=True)
    contact_phont = models.CharField(max_length=20)
    address = models.TextField(max_length=255, blank=False, null=False)
    company_name = models.CharField(max_length=255, blank=False, null=False)
    company_pan = models.IntegerField()
    company_vat = models.IntegerField()
    verification_code = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.site_name

DOCUMENT_TYPR_CHOICES = [
    ('company_pan', 'Company PAN'),
    ('company_vat', 'Company VAT')
]

class CompanyDocument(models.Model):
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPR_CHOICES)
    document_name = models.CharField(max_length=255, blank=False, null=False)
    document_file = models.FileField(upload_to='company_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_name
