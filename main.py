import discord
from discord.ext import commands
import random

token = "add_ur_bot_token_here"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")


@bot.slash_command(name="randomrole", description="dahobby goated dev")
async def randomrole(ctx, how_many_members: int, role1: discord.Role, role2: discord.Role = None, role3: discord.Role = None, role4: discord.Role = None, role5: discord.Role = None, role6: discord.Role = None, role7: discord.Role = None, role8: discord.Role = None, role9: discord.Role = None, role10: discord.Role = None):
    if how_many_members < 1:
        await ctx.respond("Invalid number of members. Must be a positive integer.")
        return

    roles = [role for role in [role1, role2, role3, role4, role5, role6, role7, role8, role9, role10] if role is not None]
    if len(roles) < 1:
        await ctx.respond("No roles specified.")
        return
    if len(roles) > 10:
        await ctx.respond("Too many roles specified. Maximum of 10 roles allowed.")
        return

    guild = ctx.guild
    members = [member async for member in guild.fetch_members(limit=None)]
    if len(members) < how_many_members:
        await ctx.respond(f"Not enough members in the server to assign roles to {how_many_members} members.")
        return

    if not ctx.author.guild_permissions.manage_roles:
        await ctx.respond("You don't have the necessary permissions to manage roles.")
        return

    if not ctx.me.guild_permissions.manage_roles:
        await ctx.respond("I dont have perms LOL! Put my role above the others and give my role the manage roles perms! :3 ")
        return

    random_members = random.sample(members, how_many_members)
    for member in random_members:
        role = random.choice(roles)
        try:
            await member.add_roles(role)
            print(f"Added role {role.name} to {member.display_name}")
        except discord.Forbidden:
            await ctx.respond("I don't have the necessary permissions to add roles to some members.")
            return
    await ctx.send(f"Random roles assigned to {how_many_members} members! go vouch dahobby for this amazing code :3")


bot.run(token)
