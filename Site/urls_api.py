from rest_framework import routers

from .views import NewsletterViewsSet, ContactViewsSet, QuoteViewsSet

router = routers.DefaultRouter()
router.register('Contact', ContactViewsSet)
router.register('Newsletter', NewsletterViewsSet)
router.register('Quote', QuoteViewsSet)
