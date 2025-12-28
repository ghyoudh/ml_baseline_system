import typer
from pathlib import Path
from ml_baseline.make_sample_feature_table import make_sample_feature_table

app = typer.Typer(help="ML Baseline System")

@app.command()
def help():
    """Show help information."""
    typer.echo(app.get_help(typer.Context(app)))

@app.command("make-sample-data")
def make_sample_data(n_users: int = 50) -> None:
    path = make_sample_feature_table(n_users=n_users)
    typer.echo(f"Sample feature table created at: {path}")

@app.command()
def train():
    """Train the ML model."""
    typer.echo("Training the model... (functionality to be implemented)")

@app.command()
def predict():
    """Make predictions using the ML model."""
    typer.echo("Making predictions... (functionality to be implemented)")

@app.command()
def show_run():
    """Show the latest run details."""
    typer.echo("Showing latest run... (functionality to be implemented)")
