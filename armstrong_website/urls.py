from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from armstrong.core.arm_wells.views import SimpleWellView

urlpatterns = patterns('',
    url(r'^contact/', include('contact_form.urls')),
    url(r'^$', SimpleWellView.as_view(template_name='home/index.html',
                                      well_title='Generic'), name='home'),

    url(r'favicon\.ico', 'django.views.generic.simple.redirect_to', 
        {'url': 'http://www.armstrongcms.org/images/logo/favicon_16.png'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
