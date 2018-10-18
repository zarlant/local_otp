import os
import sys
import configparser

import pyotp
import click


@click.command("print")
@click.option("--provider", required=True, help="Provider name as it appears in the config file")
@click.option("--config-location", default="~/.mfa", help="Config file should be ini style. See config-help for more details")
def print_otp(provider, config_location):
    config_path = os.path.expanduser(config_location)
    if os.path.exists(config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        if provider in config:
            otp_secret = config[provider]['secret']
            totp = pyotp.TOTP(otp_secret)
            click.echo(totp.now())
        else:
            click.echo("Provider: {} not found!".format(provider))
            sys.exit(1)
    else:
        click.echo("Config: {} not found!".format(config_path))
        sys.exit(2)

@click.command("config-help", help="Print example config format")
@click.option("--provider", required=False)
@click.option("--secret", required=False)
def print_config(provider, secret):
    config_format = """
[{provider}]
secret = {secret} 
"""
    if provider and secret:
        config_format = config_format.format(provider=provider, secret=secret)
    else:
        config_format = config_format.format(provider="PROVIDER_NAME", secret="SECRET_GOES_HERE")
    click.echo(config_format)

@click.group()
def otp():
    pass

otp.add_command(print_otp)
otp.add_command(print_config)
