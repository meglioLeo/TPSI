from fetcher import UserFetcher
from filter import UserFilter

def main():
    """Orchestrates the fetching, filtering, and displaying of users."""
    fetcher = UserFetcher()
    users = fetcher.fetch_users() # Fetch user list as UserModel instances
    if not users:
        print("No users found or API request failed.")
        return
    filtered_users = UserFilter.filter_by_state(users) # Filter users by state
    print("\nUsers in Illinois:")
    for user in filtered_users:
        print(f"- {user.name} ({user.email}) - {user.company}")

if __name__ == "__main__":
    main()