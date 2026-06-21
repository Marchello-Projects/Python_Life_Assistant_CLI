from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from api.weather_api import WeatherApi

console = Console()


def run_weather():
    try:
        weather_api = WeatherApi()
    except ValueError as error:
        console.print(f"[bold red]{error}[/bold red]")
        return

    city = Prompt.ask("[bold cyan]Enter city[/bold cyan]").strip()

    if not city:
        console.print("[bold red]City can't be empty[/bold red]")
        return

    weather = weather_api.get_data(city)

    if weather is None:
        console.print("[bold yellow]Weather data not found[/bold yellow]")
        return

    print_weather(weather)


def print_weather(weather):
    table = Table(
        title="Weather",
        box=box.ROUNDED,
        show_lines=True,
        header_style="bold cyan",
    )

    table.add_column("Parameter", style="magenta")
    table.add_column("Value", style="green")

    table.add_row("City", f"{weather['city']}, {weather['country']}")
    table.add_row("Temperature", f"{weather['temperature']}°C")
    table.add_row("Feels like", f"{weather['feels_like']}°C")
    table.add_row("Humidity", f"{weather['humidity']}%")
    table.add_row("Wind speed", f"{weather['wind_speed']} m/s")
    table.add_row("Description", weather["description"])

    console.print(
        Panel(
            table,
            title="[bold blue]WEATHER INFO[/bold blue]",
            border_style="blue",
            box=box.ROUNDED,
        )
    )
