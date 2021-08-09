from rest_framework.permissions import BasePermission, SAFE_METHODS

from escape_rooms.escape_app.models import Team, Room
from escape_rooms.organizations_app.models import Employee


def is_company_employee(user_id, company_id):

    try:
        employee = Employee.objects.get(user__pk=user_id)
    except Employee.DoesNotExist:
        employee = None

    if employee and employee.company.id == company_id:
        return True

    return False


def is_team_member(user_id, team_id):

    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        team = None

    if team and team.players.filter(id=user_id).exists():
        return True

    return False


def get_room_owner_company_id(room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        room = None

    if room:
        return room.owner_company.id


class IsOwnerCompanyEmployeeOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        if 'owner_company' in request.data:
            return is_company_employee(request.user.id, request.data['owner_company'])

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        return is_company_employee(request.user.id, obj.owner_company.id)


class IsMemberOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        if 'players' in request.data:
            return request.user.id in request.data['players']

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True
        if request.user in obj.players.all():
            return True

        return False


class IsRoomOwnerCompanyEmployeeOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        if 'room' in request.data:
            return is_company_employee(request.user.id, get_room_owner_company_id(request.data['room']))

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        return is_company_employee(request.user.id, get_room_owner_company_id(obj.room.id))


class IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        if 'team' in request.data and 'room' in request.data:
            if not is_team_member(request.user.id, request.data['team']) and \
                    not is_company_employee(request.user.id, get_room_owner_company_id(request.data['room'])):
                return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        return is_team_member(request.user.id, obj.team.id) or \
               is_company_employee(request.user.id, get_room_owner_company_id(obj.room.id))


class IsUserReviewOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user and request.user.is_superuser):
            return True

        if obj.player.id == request.user.id:
            return True

        return False
