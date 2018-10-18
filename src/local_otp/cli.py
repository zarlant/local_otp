import click
from local_otp.local import otp

@click.group()
def cli():
    pass

cli.add_command(otp)

if __name__ == '__main__':
    cli()
