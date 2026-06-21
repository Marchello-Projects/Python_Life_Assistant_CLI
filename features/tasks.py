class TaskManager:
    __hashtags = (
        "#study",
        "#work",
        "#project",
        "#python",
        "#api",
        "#oop",
        "#bug",
        "#feature",
        "#fix",
        "#docs",
        "#test",
        "#urgent",
        "#important",
        "#low",
        "#medium",
        "#high",
    )

    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return [task.copy() for task in self._tasks]

    @tasks.setter
    def tasks(self, task_data):
        if not isinstance(task_data, dict):
            raise TypeError("Task data must be a dictionary.")

        name = task_data.get("name")
        description = task_data.get("description")
        hashtag = task_data.get("hashtag")

        if not name or not name.strip():
            raise ValueError("Task name can't be empty.")

        if not description or not description.strip():
            raise ValueError("Task description can't be empty.")

        if hashtag not in self.__hashtags:
            raise ValueError("This hashtag doesn't exist.")

        task = {
            "name": name.strip(),
            "description": description.strip(),
            "hashtag": hashtag,
        }

        self._tasks.append(task)

    def take_a_specific_task(self, task_name):
        for task in self._tasks:
            if task_name == task.get("name"):
                return task.copy()

        return None