from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


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
            raise TypeError("Task data must be a dictionary")

        name = task_data.get("name")
        description = task_data.get("description")
        hashtag = task_data.get("hashtag")

        if not name or not name.strip():
            raise ValueError("Task name can't be empty")

        if not description or not description.strip():
            raise ValueError("Task description can't be empty")

        if hashtag not in self.__hashtags:
            raise ValueError("This hashtag doesn't exist")

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

    def delete_a_specific_task(self, task_name):
        for index, task in enumerate(self._tasks):
            if task_name == task.get("name"):
                del self._tasks[index]
                return True

        return False

    @classmethod
    def get_hashtags(cls):
        return cls.__hashtags


task_manager = TaskManager()


def run_tasks():
    while True:
        console.print(
            Panel.fit(
                """
[bold cyan][1][/bold cyan] Add task
[bold cyan][2][/bold cyan] Show all tasks
[bold cyan][3][/bold cyan] Find task by name
[bold cyan][4][/bold cyan] Show available hashtags
[bold cyan][5][/bold cyan] Delete task by name
[bold red][0][/bold red] Back to main menu
""",
                title="[bold magenta]TASKS[/bold magenta]",
                border_style="magenta",
                box=box.ROUNDED,
            )
        )

        choice = Prompt.ask("[bold yellow]Choose option[/bold yellow]").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            show_all_tasks()

        elif choice == "3":
            find_task()

        elif choice == "4":
            show_hashtags()

        elif choice == "5":
            delete_task()

        elif choice == "0":
            break

        else:
            console.print("[bold red]Wrong option Try again[/bold red]")


def add_task():
    name = Prompt.ask("[bold cyan]Task name[/bold cyan]").strip()
    description = Prompt.ask("[bold cyan]Task description[/bold cyan]").strip()
    hashtag = Prompt.ask("[bold cyan]Task hashtag[/bold cyan]").strip()

    try:
        task_manager.tasks = {
            "name": name,
            "description": description,
            "hashtag": hashtag,
        }

        console.print("[bold green]Task added successfully[/bold green]")

    except ValueError as error:
        console.print(f"[bold red]Error:[/bold red] {error}")

    except TypeError as error:
        console.print(f"[bold red]Error:[/bold red] {error}")


def show_all_tasks():
    tasks = task_manager.tasks

    if not tasks:
        console.print("[bold yellow]Task list is empty[/bold yellow]")
        return

    table = Table(
        title="Your tasks",
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold magenta",
    )

    table.add_column("№", justify="center", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Description", style="white")
    table.add_column("Hashtag", style="yellow")

    for index, task in enumerate(tasks, start=1):
        table.add_row(
            str(index),
            task["name"],
            task["description"],
            task["hashtag"],
        )

    console.print(table)


def find_task():
    task_name = Prompt.ask("[bold cyan]Enter task name[/bold cyan]").strip()

    if not task_name:
        console.print("[bold red]Task name can't be empty[/bold red]")
        return

    task = task_manager.take_a_specific_task(task_name)

    if task is None:
        console.print("[bold yellow]Task not found[/bold yellow]")
        return

    table = Table(
        title="Task found",
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold magenta",
    )

    table.add_column("Name", style="green")
    table.add_column("Description", style="white")
    table.add_column("Hashtag", style="yellow")

    table.add_row(
        task["name"],
        task["description"],
        task["hashtag"],
    )

    console.print(table)


def delete_task():
    task_name = Prompt.ask("[bold cyan]Enter task name to delete[/bold cyan]").strip()

    if not task_name:
        console.print("[bold red]Task name can't be empty[/bold red]")
        return

    is_deleted = task_manager.delete_a_specific_task(task_name)

    if is_deleted:
        console.print("[bold green]Task deleted successfully[/bold green]")
    else:
        console.print("[bold yellow]Task not found[/bold yellow]")


def show_hashtags():
    hashtags = TaskManager.get_hashtags()

    table = Table(
        title="Available hashtags",
        box=box.ROUNDED,
        header_style="bold magenta",
    )

    table.add_column("№", justify="center", style="cyan")
    table.add_column("Hashtag", style="yellow")

    for index, hashtag in enumerate(hashtags, start=1):
        table.add_row(str(index), hashtag)

    console.print(table)
