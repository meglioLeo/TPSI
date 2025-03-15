from config import DEFAULT_STATE_FILTER
class UserFilter:
    """Provides methods to filter users based on specific criteria."""
    
    @staticmethod
    def filter_by_state(users, state=DEFAULT_STATE_FILTER):
        """Filters users based on the provided state."""
        return [user for user in users if user.state == state]