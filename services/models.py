from django.db import models
from django.urls import reverse


class ServiceCategory(models.Model):
    """Service category model for Grow Sale Products printing services."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    resolution_dpi = models.CharField(
        max_length=50,
        verbose_name='Resolution (DPI)',
        help_text='Print resolution range, e.g. "600 to 1200 DPI"',
        default='300 DPI',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Service Category'
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_list')


class Quote(models.Model):
    """Quote request model for Grow Sale Products."""

    MATERIAL_CHOICES = [
        ('fabric', 'Fabric'),
        ('silk', 'Silk'),
        ('plastics', 'Plastics'),
        ('cardboard', 'Cardboard'),
    ]

    FINISH_TYPE_CHOICES = [
        ('glossy', 'Glossy'),
        ('matte', 'Matte'),
        ('textured', 'Textured'),
    ]

    client_name = models.CharField(max_length=200, verbose_name='Full Name')
    company_email = models.EmailField(verbose_name='Email Address')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    material_choice = models.CharField(
        max_length=20,
        choices=MATERIAL_CHOICES,
        verbose_name='Material',
    )
    finish_type = models.CharField(
        max_length=20,
        choices=FINISH_TYPE_CHOICES,
        verbose_name='Finish Type',
    )
    design_file = models.FileField(
        upload_to='quotes/designs/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='Design File',
        help_text='Upload your design file (PDF, AI, PSD, PNG, JPG)',
    )
    message = models.TextField(
        verbose_name='Project Details',
        help_text='Describe your printing requirements',
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Quote Request'
        verbose_name_plural = 'Quote Requests'

    def __str__(self):
        return f"Quote from {self.client_name} - {self.submitted_at.strftime('%Y-%m-%d')}"


class Product(models.Model):
    """Product model to showcase screen printing items under specific service categories."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='products/images/',
        blank=True,
        null=True,
        verbose_name='Product Image',
        help_text='Upload the actual product mockup image'
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Service Category',
        help_text='Select the category this product falls under'
    )
    is_featured = models.BooleanField(default=True, verbose_name='Featured Product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')
