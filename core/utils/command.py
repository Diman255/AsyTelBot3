from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeAllGroupChats


async def command_shtat(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='start'
        ),
    ]

    await bot.set_my_commands(command, BotCommandScopeAllGroupChats())

