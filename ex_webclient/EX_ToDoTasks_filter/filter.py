from config import DEFAULT_COMPLETED_FILTER

class TaskFilter:
    
    @staticmethod
    def filter_by_completed(tasks, completed = DEFAULT_COMPLETED_FILTER):
        return [task for task in tasks if task.completed == completed]