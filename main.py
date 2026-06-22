from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from features.currency import run_currency_converter
from features.tasks import run_tasks
from features.weather import run_weather

console = Console()


def show_logo():
    logo = r"""
██████╗  █████╗  ██████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██║     
██╔═══╝ ██╔══██║██║     
██║     ██║  ██║╚██████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝
"""

    logo_text = Text()
    logo_text.append(logo, style="bold cyan")
    logo_text.append("\nPython Assistant CLI", style="bold magenta")

    console.print(
        Panel(
            Align.center(logo_text),
            border_style="cyan",
            box=box.DOUBLE,
        )
    )


def show_menu():
    menu = Table.grid(padding=(0, 2))
    menu.add_column(justify="right")
    menu.add_column(justify="left")

    menu.add_row("[bold cyan]1[/bold cyan]", "[bold green]Weather[/bold green]")
    menu.add_row("[bold cyan]2[/bold cyan]", "[bold yellow]Tasks[/bold yellow]")
    menu.add_row(
        "[bold cyan]3[/bold cyan]", "[bold blue]Currency Converter[/bold blue]"
    )
    menu.add_row("[bold red]0[/bold red]", "[bold red]Exit[/bold red]")

    console.print(
        Panel(
            Align.center(menu),
            title="[bold magenta]MAIN MENU[/bold magenta]",
            border_style="magenta",
            box=box.ROUNDED,
        )
    )


def main():
    while True:
        console.clear()
        show_logo()
        show_menu()

        choice = Prompt.ask("[bold yellow]Choose option[/bold yellow]").strip()

        if choice == "1":
            run_weather()

        elif choice == "2":
            run_tasks()

        elif choice == "3":
            run_currency_converter()

        elif choice == "0":
            console.print("[bold green]Goodbye[/bold green]")
            break

        else:
            console.print("[bold red]Wrong option Try again[/bold red]")

        Prompt.ask("\n[dim]Press Enter to continue[/dim]", default="")


if __name__ == "__main__":
    main()
