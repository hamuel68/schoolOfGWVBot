import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")


    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command()
    async def createticket(ctx):
        guild = ctx.guild
        author = ctx.author
        ticket_channel_name = f"ticket-{author.name}"

        # Check if a channel with this name already exists
        existing_channel = discord.utils.get(guild.text_channels, name=ticket_channel_name)
        if existing_channel:
            await ctx.send("You already have an open ticket.")
            return
        
        # Check if the "Tickets" category exists, if not, create it
        category_name = "Tickets"
        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            category = await guild.create_category(category_name)

        # Define permissions
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            author: discord.PermissionOverwrite(read_messages=True),
            discord.utils.get(guild.roles, name="Head teacher"): discord.PermissionOverwrite(read_messages=True)
        }

        # Create the channel
        ticket_channel = await guild.create_text_channel(name=ticket_channel_name, overwrites=overwrites, category=category)

        # Notify in the tickets channel
        tickets_channel = discord.utils.get(guild.text_channels, name="tickets")
        if tickets_channel:
            await tickets_channel.send(f"{author.mention} has created a ticket. {ticket_channel.mention}")

        head_teacher_role = discord.utils.get(guild.roles, name="Head teacher")
        await ctx.send(f"{author.mention}, your ticket has been created: {ticket_channel.mention}")
        await ticket_channel.send(
            f"{head_teacher_role.mention} A new ticket has been created by {author.mention}: {ticket_channel.mention}"
        )

    @bot.command()
    async def closeticket(ctx):
        # This command should only work in ticket channels.
        if ctx.channel.name.startswith("ticket-"):
            await ctx.channel.delete()
            # You can add additional logic here if needed, like logging the closure of the ticket.
        else:
            await ctx.send("This command can only be used in ticket channels.")


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == '__main__':
    run()