
class AuthorisationError(Exception):
    pass


gym_members = []


def cancel_membership(membership_id, user):
    """
    Canel Gym membership for an existing member.
    """
    if not user.is_admin():
        raise AuthorisationError('Must be admin to cancel')
    if not gym_members.membership_exists(membership_id):
        raise ValueError('Unknown id')

    gym_members.find_membership(membership_id).delete()


