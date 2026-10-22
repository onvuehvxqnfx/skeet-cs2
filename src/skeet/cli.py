"""Typer entrypoint for the skeet-cs2 dump host."""
from __future__ import annotations

import typer
from rich.console import Console

from skeet.host import PluginHost
from skeet.loader import load_builtin_plugins
from skeet.registry.signatures import CS2_BUILDS

app = typer.Typer(add_completion=False, help="Gamesense.pub (Skeet) CS2 dump tooling")
console = Console()


@app.command()
def dump(
    build: str = typer.Option("2401", help="CS2 build id from registry/signatures"),
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> None:
    if build not in CS2_BUILDS:
        console.print(f"[red]unknown CS2 build[/] {build}")
        raise typer.Exit(2)
    host = PluginHost()
    load_builtin_plugins(host)
    console.print(f"[cyan]skeet-cs2[/] host up, {len(host.registry)} plugins registered")
    if dry_run:
        console.print("[yellow]dry run[/] — no memory reads performed")
        return
    host.run(build=build)


@app.command()
def plugins() -> None:
    host = PluginHost()
    load_builtin_plugins(host)
    for name, meta in host.registry.items():
        console.print(f"  {name:<24} v{meta.version}  {meta.description}")


if __name__ == "__main__":
    app()