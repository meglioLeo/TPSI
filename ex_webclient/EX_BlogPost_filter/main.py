from fetcher import PostFetcher
from filter import PostFilter

def main():
    fetcher = PostFetcher
    posts = fetcher.fetch_posts()
    if not posts:
        print("No posts found or API request failed.")
        return
    filtered_posts = PostFilter.filter_by_comment_count(posts)
    print("\nPosts with more than 5 comments:")
    for task in posts:
        print(f"- {task.title} ({task.body}) - {task.comment_count}")
        
if __name__ == "__main__":
    main()