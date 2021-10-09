import discord
from discord.ext import tasks
from discord.ext import commands


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_member_join(member):
    print("Event Called!")
    guild1 = client.get_guild(893391320813555713) # server which the person want to join
    guild3 = client.get_guild(893330054254317698) # logs server
    chenel = client.get_channel(893405205067083836) # logs channel where to send message
    guild2 = client.get_guild(893330054254317698) # main server where the role check will be done
    role = guild2.get_role(893391786586828800) # role to check
    # role2 = guild2.get_role(889469739066355732) #administrative role (if you want the bot to not kick the admins then remove those hashes)
    members = guild2.get_member(member.id)
    if member.guild != guild1:
        return
    else:
        if role in members.roles:
            print(f"{member.name} has joined")
            await chenel.send(f"{member.name}#{member.discriminator} Joined The Server and wasn't kicked out because he have the role")
            return
        # elif role2 in members.roles:
        #     print("ADMIN JOINED")
        #     await chenel.send(f"{member.name}#{member.discriminator} Joined The Server And Wasn't Kicked Because He Have CHAMP Role")
        #     return
        else:
            await member.kick()
            await member.send("Looks Like You Do Not Have The Role") # you can comment out this line(basically delete) if you don't want the bot to send message
            await chenel.send(f"{member.name}#{member.discriminator} was kicked from server because he don't have the role")
            
        
client.run("")
