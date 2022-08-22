import requests
import json
import typer
from rich.console import Console
console = Console()
app = typer.Typer()


@app.command()
def linkVertise(type: str, link: str):
    match type:
        case "single":
            try:
                result = requests.get(
                    "https://bypass.bot.nu/bypass2?url=%s" % (link))
                read = json.loads(result.text)
                res = read["destination"]
                console.print(
                    "[cyan] %s [white]-> [bold green] %s" % (link, res))
            except Exception as e:
                console.print(
                    "[red] Error [white]-> [bold red] Can't Connect To Server Maybe Wrong Link")

        case "mass":
            try:
                read = open(link, 'r').read().splitlines()
                for x in read:
                    result = requests.get("https://bypass.bot.nu/bypass2?url=%s" %
                                          (str(x)))
                    read = json.loads(result.text)
                    res = read["destination"]
                    console.print(
                        "[cyan] %s [white]-> [bold green] %s" % (x, res))
            except Exception as e:
                # print(e)
                console.print(
                    "[red] Error [white]-> [bold red] Can't Connect To Server Maybe Wrong Link")

        case _:
            console.print(
                "[red] Error [white]-> [bold red] Wrong")


app()
