from django.db import models

# Create your models here.

from django.urls import reverse


class Project(models.Model):

    CATEGORY_CHOICES = [
        ("ecommerce", "E-Commerce"),
        ("saas", "SaaS"),
        ("marketing", "Marketing"),
        ("finance", "Finance"),
        ("other", "Other"),
    ]

    # BASIC
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    short_description = models.TextField()

    cover_image = models.ImageField(
        upload_to="projects/covers/"
    )

    featured = models.BooleanField(default=False)

    # PROJECT INFO
    duration = models.CharField(
        max_length=100,
        blank=True
    )

    budget = models.CharField(
        max_length=100,
        blank=True
    )

    tools_used = models.CharField(
        max_length=255,
        blank=True
    )

    # CASE STUDY
    challenge = models.TextField()

    approach = models.TextField()

    solution = models.TextField()

    # TESTIMONIAL
    client_name = models.CharField(
        max_length=100,
        blank=True
    )

    client_position = models.CharField(
        max_length=100,
        blank=True
    )

    testimonial = models.TextField(
        blank=True
    )

    # RESULTS
    metric_1_label = models.CharField(
        max_length=100,
        blank=True
    )

    metric_1_value = models.CharField(
        max_length=50,
        blank=True
    )

    metric_2_label = models.CharField(
        max_length=100,
        blank=True
    )

    metric_2_value = models.CharField(
        max_length=50,
        blank=True
    )

    metric_3_label = models.CharField(
        max_length=100,
        blank=True
    )

    metric_3_value = models.CharField(
        max_length=50,
        blank=True
    )

    metric_4_label = models.CharField(
        max_length=100,
        blank=True
    )

    metric_4_value = models.CharField(
        max_length=50,
        blank=True
    )

    # GALLERY
    image_1 = models.ImageField(
        upload_to="projects/gallery/",
        blank=True,
        null=True
    )

    image_2 = models.ImageField(
        upload_to="projects/gallery/",
        blank=True,
        null=True
    )

    image_3 = models.ImageField(
        upload_to="projects/gallery/",
        blank=True,
        null=True
    )

    image_4 = models.ImageField(
        upload_to="projects/gallery/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "project_detail",
            kwargs={"slug": self.slug}
        )