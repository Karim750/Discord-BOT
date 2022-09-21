from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 'Karim#8206'  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

#Send salut tout seul and tag the user
@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        msg = "Salut tout seul"
        await message.channel.send(msg + message.author.mention)
    await bot.process_commands(message)
    
#get the name of the user
@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

#get a number between 1 and 6
@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1, 6))


#ban a user
@bot.command()
async def ban(ctx,  user: discord.Member, *, reason = None):
    return await ctx.guild.ban(user, reason = reason)

# Create roles and set them
#async def admin(ctx,  user : discord.Member):
 #   guild = ctx.guild
  #  if 'Admin' in discord.roles :
   #     return await user.add_roles(name = 'Admin')
    #else :
        #permissions=discord.Permissions(permissions= BAN_MEMBERS )
        #server = ctx.message.server
        #perms = discord.Permissions(send_messages=False, read_messages=True)
     #   await guild.create_role(name='Admin', permissions=None)
      #  return await user.add_roles(name = 'Admin')
    

token = ""
bot.run(token)  # Starts the bot