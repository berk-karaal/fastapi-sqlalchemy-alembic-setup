import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if it exists


class _NoArg:
    """A sentinel value to indicate that a parameter was not given"""


NO_ARG = _NoArg()


def get_env_var(key: str, default: str | _NoArg = NO_ARG) -> str:
    """Get an environment variable, raise an error if it is missing and no default is given."""
    try:
        return os.environ[key]
    except KeyError:
        if isinstance(default, _NoArg):
            raise ValueError(f"Environment variable {key} is missing")

        return default


PG_HOST = get_env_var("PG_HOST")
PG_PORT = get_env_var("PG_PORT")
PG_USER = get_env_var("PG_USER")
PG_PASSWORD = get_env_var("PG_PASSWORD")
PG_DB = get_env_var("PG_DB")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)
SQLALCHEMY_ECHO = get_env_var("SQLALCHEMY_ECHO", "") == "true"
