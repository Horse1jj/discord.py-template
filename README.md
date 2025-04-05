# Discord.py + SQLite Bot Template

A simple and extensible Discord bot template built with `discord.py` and `sqlite3`.  
This template is ideal for developers who want to quickly build a feature-rich Discord bot with database support and clean project structure.

## Features

- Modular cog loading system
- JSON-based configuration
- SQLite support for persistent data

---

## Getting Started

### Prerequisites

- Python 3.8 or newer
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)

### Installation

1. **Clone this repository:**

```bash

git clone https://github.com/feelingnothing/discord.py-template.git
cd discord.py-template

```

```bash 
Install required packages:
pip install -r requirements.txt
```


Create a config.json file in the root directory:

```json
{
  "botToken": "YOUR_DISCORD_BOT_TOKEN",
  "botPrefix": "!",
  "db_file": "general.db"
}

```

Run the bot:

```bash
python bot.py
```

# Creating a Cog

Add a .py file in the cogs/ folder like this:


```py

from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(Example(bot))

```

Database Example

```py

from modules.sql import connect, close

conn, cursor = connect()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
close(conn)

```