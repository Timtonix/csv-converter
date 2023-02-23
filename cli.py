from typing import List
import typer
from pathlib import Path
import csv_api


app = typer.Typer()


@app.command()
def update_csv(to_update_file: Path, target_file: Path, headers: List[str]):
    if not to_update_file.is_file():
        print("The csv doesn't exist")
        typer.Abort()
    csv_converter = csv_api.CSVConverter(to_update_file)
    new_csv = csv_converter.write_new_csv(headers, target_file)
    print(f"The new csv have been writen !")


@app.command()
def hello(name: str):
    print(f"Hello {name} !")


if __name__ == "__main__":
    app()