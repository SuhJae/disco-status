import nextcord
import psutil
import time
from nextcord import Interaction

client = nextcord.Client()

# Set your server ID and channel ID here
SERVER_ID = 1023440388352114749
CHANNEL_ID = 1080393241322594304

# Default interval for updating message in seconds
DEFAULT_INTERVAL = 1

# Global variables to hold the latest system resource usage
cpu_usage = 0
ram_usage = 0
disk_usage = 0
swap_usage = 0


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")


async def get_resource_usage():
    global cpu_usage, ram_usage, disk_usage, swap_usage

    # Get system resource usage
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    swap_usage = psutil.swap_memory().percent

def bar(value, max_value, length):
    # Calculate the number of blocks to fill
    filled = int(round(length * value / max_value))
    # Return the bar
    return '#' * filled + ' ' * (length - filled)

@client.slash_command(name = 'useage', description = 'Check the system resource usage.')
async def htop(interaction: Interaction):
    await interaction.response.defer(ephemeral=False, with_message=True)

    loadavg = psutil.getloadavg()

    io_counters_start = psutil.net_io_counters()
    time.sleep(1)
    io_counters_end = psutil.net_io_counters()

    bytes_sent = io_counters_end.bytes_sent - io_counters_start.bytes_sent
    bytes_recv = io_counters_end.bytes_recv - io_counters_start.bytes_recv

    embed = nextcord.Embed(title='System Resource Usage', description=f'''Uptime: **{time.strftime("%H:%M:%S", time.gmtime(time.time() - psutil.boot_time()))}**
    
`CPU` 1m **{round(loadavg[0], 2)}** | 5m **{round(loadavg[1], 2)}** | 15m **{round(loadavg[2], 2)}** ({psutil.cpu_percent()}%)
`RAM` Available **{psutil._common.bytes2human(psutil.virtual_memory().available)}** | Total **{psutil._common.bytes2human(psutil.virtual_memory().total)}** ({psutil.virtual_memory().percent}%)
`SWAP` Available **{psutil._common.bytes2human(psutil.swap_memory().free)}** | Total **{psutil._common.bytes2human(psutil.swap_memory().total)}** ({psutil.swap_memory().percent}%)
`DISK` Free **{psutil._common.bytes2human(psutil.disk_usage('/').free)}** | Total **{psutil._common.bytes2human(psutil.disk_usage('/').total)}**
`NET` Download **{psutil._common.bytes2human(bytes_recv)}/s** Upload **{psutil._common.bytes2human(bytes_sent)}/s**
''', color=nextcord.Color.blue())

    cpu_per = psutil.cpu_percent(percpu=True)

    # repeat for number of CPU cores
    for i in range(psutil.cpu_count()):
        embed.add_field(name=f'**Core {i}**', value=f'`[{bar(cpu_per[i], 100, 15)}]` {cpu_per[i]}%', inline=True)

    embed.set_footer(text=f'Time: {time.strftime("%H:%M:%S (%Z)")}')

    await interaction.followup.send(embed=embed)

# Set your Discord bot token here
client.run("Your Token")
