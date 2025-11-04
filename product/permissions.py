from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsModerator(BasePermission):
    """
    Разрешает доступ сотрудникам (is_staff=True) для просмотра любых продуктов,
    изменять и удалять чужие продукты, а создавать продукты (POST) — только модератору.
    """
    def has_permission(self, request, view):
        # Только сотрудники (модераторы)
        if not request.user or not request.user.is_staff:
            return False
        # Разрешить POST только модератору
        if request.method == 'POST':
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        # Только сотрудники (модераторы)
        if not request.user or not request.user.is_staff:
            return False
        # Модератор может просматривать любые продукты
        if request.method in SAFE_METHODS:
            return True
        # Модератор может изменять/удалять только чужие продукты
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.owner != request.user
        # POST не применяется к объекту
        return False