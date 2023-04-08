import uvicorn
import typer
from app import fast_app

manager = typer.Typer()


@manager.command(name='run')
def run():
    port = 8080
    uvicorn.run('manage:fast_app', host='0.0.0.0', port=int(port))

@manager.command()
def test():
    """
    This method needs to ve called when pytests are added. It will act as a runner for all pytests.
    """
    pass

if __name__ == "__main__":
    manager()
