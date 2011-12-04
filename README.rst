Django-permission-backend-nonrel
====================================

A Django authentication backend that supports Django's user and group permissions on Django-Nonrel_.


Installation
====================================

* Get the code form Github:

    git clone https://fhahn@github.com/django-nonrel/django-permission-backend-nonrel.git

* add **permission_backend_nonrel.backends.NonrelPermissionBackend** to your *AUTHENTICATION_BACKENDS*
  and **permission_backend_nonrel** to your *INSTALLED_APPS*

   settings.py::
   
        AUTHENTICATION_BACKENDS = (
            ...
            'permission_backend_nonrel.backends.NonrelPermissionBackend',
        )       

        INSTALLED_APPS = (      
            ...
            'permission_backend_nonrel',
        )   
  
* It's important to put **'permission_backend_nonrel** after **djangotoolbox**, 
  because **permission_backend_nonrel.admin** replaces **djangotoolbox**'s User admin site.

  Permission and groups can be assigned and modified via Django's admin interface:


  .. figure:: http://floooofiles.appspot.com/serve/files/admin.jpeg/
      :scale: 50 %
      :alt: Django-nonrel admin with user_permissions and groups 

      Django-gaeauth admin interface with user_permissions and groups 


* Now you should be able to use all the standard Django permission methods and decorators, 
  like *user.has_perm('foo')* and so on.


.. _Django-Nonrel: http://www.allbuttonspressed.com/projects/django-nonrel
