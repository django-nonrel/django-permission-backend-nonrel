from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Group

from models import UserPermissionList, GroupPermissionList


class NonrelPermissionBackend(ModelBackend):
    """
    Implements Django's permission system on Django-Nonrel
    """
    supports_object_permissions = False
    supports_anonymous_user = True

    def get_group_permissions(self, user_obj, obj=None, user_perm_list=None):
        """
        Returns a set of permission strings that this user has through his/her
        groups.
        """
        if user_obj.is_anonymous() or obj is not None:
            return set()
        if not hasattr(user_obj, '_group_perm_cache'):
            perms = set([])
            if not user_perm_list:
                user_perm_list, _ = UserPermissionList.objects.get_or_create(user=user_obj)
            groups = Group.objects.filter(id__in=user_perm_list.group_fk_list)
            group_perm_lists = GroupPermissionList.objects.filter(group__in=list(groups))

            for group_perm_list in group_perm_lists:
                perms.update(group_perm_list.permission_list)

            user_obj._group_perm_cache = perms
        return user_obj._group_perm_cache

    def get_all_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        if not hasattr(user_obj, '_perm_cache'):
            try:
                user_perm_list = UserPermissionList.objects.get(user=user_obj)
                user_obj._perm_cache = set(user_perm_list.permission_list)

            except UserPermissionList.DoesNotExist:
                user_perm_list = None
                user_obj._perm_cache = set()

            user_obj._perm_cache.update(self.get_group_permissions(user_obj, user_perm_list=user_perm_list))
        return user_obj._perm_cache
