# **Disco-status**

Disco-status is a simple Discord bot that tracks your computer's resource usage in real-time. With Disco-status, you can easily keep an eye on your system's CPU, RAM, disk, and swap usage, and monitor your computer's performance without leaving your Discord server.

## **Setup**

To use Disco-status, you'll need to follow these steps:

1. Clone or download the Disco-status repository from GitHub.
2. Install the required dependencies by running **`pip install -r requirements.txt`**.
3. Create a new Discord bot and obtain its token. You can follow the instructions **[here](https://discordpy.readthedocs.io/en/latest/discord.html)** to create a bot and obtain its token.
4. Set your server ID and channel ID in the **`main.py`** file.
5. Set your Discord bot token in the **`config.ini`** file.
6. Run the **`main.py`** file using Python.

Once the bot is running, you can use the **`/usage`** command in your Discord server to check your computer's resource usage.

## **Dependencies**

Disco-status uses the following dependencies:

- nextcord
- psutil

You can install these dependencies by running **`pip install -r requirements.txt`**.

## **Usage**

To use Disco-status, simply run the **`main.py`** file using Python. Once the bot is running, you can use the **`/usage`** command in your Discord server to check your computer's resource usage. The bot will display the following information:

- CPU usage (1m, 5m, 15m)
- RAM usage (available, total)
- Swap usage (available, total)
- Disk usage (free, total)
- Network usage (download, upload)

The bot also displays a bar graph for each CPU core, showing the usage percentage for each core.

## **Contributions**

If you'd like to contribute to Disco-status, feel free to submit a pull request on GitHub. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.