from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from api.currency_api import CurrencyApi

console = Console()


def run_currency_converter():
    currency_api = CurrencyApi()

    try:
        amount = float(Prompt.ask("[bold cyan]Enter amount[/bold cyan]"))
    except ValueError:
        console.print("[bold red]Amount must be a number[/bold red]")
        return

    from_currency = Prompt.ask(
        "[bold cyan]From currency example USD[/bold cyan]"
    ).strip()
    to_currency = Prompt.ask("[bold cyan]To currency example EUR[/bold cyan]").strip()

    if not from_currency or not to_currency:
        console.print("[bold red]Currency fields can't be empty[/bold red]")
        return

    result = currency_api.get_data(
        {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
        }
    )

    if result is None:
        console.print("[bold yellow]Couldn't convert currency[/bold yellow]")
        return

    table = Table(
        title="Currency converter",
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold cyan",
    )

    table.add_column("Parameter", style="magenta")
    table.add_column("Value", style="green")

    table.add_row("Amount", f'{result["amount"]} {result["from_currency"]}')
    table.add_row("Converted", f'{result["converted_amount"]} {result["to_currency"]}')
    table.add_row(
        "Rate",
        f'1 {result["from_currency"]} = {result["rate"]} {result["to_currency"]}',
    )

    console.print(
        Panel(
            table,
            title="[bold green]CURRENCY INFO[/bold green]",
            border_style="green",
            box=box.ROUNDED,
        )
    )
