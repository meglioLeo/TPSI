from config import DEFAULT_COMMENT_COUNT_FILTER

class PostFilter:
    @staticmethod
    def filter_by_comment_count(posts, count=DEFAULT_COMMENT_COUNT_FILTER):
        return[post for post in posts if post.comment_count > count]