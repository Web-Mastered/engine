from django.db import models
from django.shortcuts import render

from blocks.fields import BlogListingPageFields, BlogPostPageFields

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet

class BlogListingPage(RoutablePageMixin, Page, BlogListingPageFields):
    """A model for a blog listing page"""

    template = "blog/blog_listing_page.html"

    # We only need one blog listing page in the website
    max_count = 1

    subpage_types = [
        'blog.BlogPostPage',
    ]

    content_panels = Page.content_panels + BlogListingPageFields.content_panels

    # method which passes an array of blog posts in date order into template as context below
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogPostPage.objects.live().public().order_by('-first_published_at')
        return context

    class Meta:
        verbose_name = "Blog Listing Page"
        verbose_name_plural = "Blog Listing Pages"

    @route(r'^categories/$')
    def category_listing_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        categorySlug = request.GET.get('category')
        # if categorySlug != None and categorySlug != "":
        if categorySlug not in (None,""):
            context = self.get_context(request, *args, **kwargs)
            category = BlogPostCategory.objects.filter(slug=categorySlug)
            if len(category) != 1:
                context['blog_listing_page'] = BlogListingPage.objects.all()[0]
                context['errorTitle'] = "Category not found"
                context['errorMessage'] = "The category that you're looking for does not exist, please double check your query."
                return render(request, "blog/error_page.html", context)
            else:
                context['blog_listing_page'] = BlogListingPage.objects.all()[0]
                context['posts'] = BlogPostPage.objects.filter(categories__in=category).live().public().order_by('-first_published_at')
                context['category'] = category.first
                return render(request, "blog/category_post_listing_page.html", context)
        else:
            context['blog_listing_page'] = BlogListingPage.objects.all()[0]
            context['categories'] = BlogPostCategory.objects.all()
            return render(request, "blog/category_listing_page.html", context)



class BlogPostPage(Page, BlogPostPageFields):
    """A model for the blog posts"""

    template = "blog/blog_post_page.html"

    parent_page_type = [
        'blog.BlogListingPage',
    ]

    content_panels = Page.content_panels + BlogPostPageFields.content_panels
    settings_panels = Page.settings_panels + BlogPostPageFields.settings_panels
    promote_panels = Page.promote_panels + BlogPostPageFields.promote_panels


    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


@register_snippet
class BlogPostCategory(models.Model):
    """A category model to sort blog posts into categories"""

    name = models.CharField(max_length=255, help_text="Name your category.")
    slug = models.SlugField(allow_unicode=True, max_length=255, help_text="A slug to identify posts by this category.")
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Associate an image with this category."
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        ImageChooserPanel("image"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Post Category"
        verbose_name_plural = "Blog Post Categories"
        ordering = ["name"]

