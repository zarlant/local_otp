# Local OTP

local-otp is a CLI that allows you to retrieve TOTP codes supported by Google Authenticator.

## Installation
Build with Docker locally:
```bash
docker build -t lotp .
```

Run locally as a sandboxed CLI:
```bash
alias lotp="docker run -it --rm -v ~/.mfa:/root/.mfa lotp"
```

To setup the configuration:
```bash
lotp otp config-help
```
