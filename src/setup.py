import os
from setuptools import setup, find_packages

base_version = "1.0.{}"
version = os.environ.get("CI_PIPELINE_IID", None)
branch = os.environ.get("CI_COMMIT_REF_SLUG", "master")

if not version:
    full_version = base_version.format("dev0")
else:
    if branch != "master":
        full_version = base_version.format("dev{}".format(version))
    else:
        full_version = base_version.format(version)

setup(
    name='local-otp',
    version=full_version,
    entry_points={
        'console_scripts': ['lotp=local_otp.cli:cli']
    },
    description='Local Python OTP Authenticator',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['click', 'pyotp']
)
