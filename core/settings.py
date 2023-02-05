from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    duty_yaroclavl: list
    duty_kamenny: list
    duty_seed: list
    chat_grup: int

@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID"),
            duty_yaroclavl=list(map(int, env.list("DUTY_YAROSLAVL"))),
            duty_kamenny=list(map(int, env.list("DUTY_KAMENNY"))),
            duty_seed=list(map(int, env.list("DUTY_SEED"))),
            chat_grup=env.int("CHAT_GRUP")
        )
    )


settings = get_settings('imput')


