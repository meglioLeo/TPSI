from fetcher import TaskFetcher
from filter import TaskFilter

def main():
    fetcher = TaskFetcher()
    tasks = fetcher.fetch_tasks()
    if not tasks:
        print("No tasks found or API request failed.")
        return
    filtered_tasks = TaskFilter.filter_by_completed(tasks)
    print("Uncompleted tasks:")
    for task in filtered_tasks:
        print(f"- {task.title}")
        
if __name__ == "__main__":
    main()