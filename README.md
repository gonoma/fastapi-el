# fastapi-el

The SECRET_KEY env variable.
To generate one run in the CLI -> `openssl rand -hex 32`

to set the env variables:
* In the zsh CLI -> `export $(xargs < .env)`
* In the fish shell -> `export (cat .env |xargs -L 1)`

