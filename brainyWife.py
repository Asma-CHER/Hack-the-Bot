import discord 
import random 
import json
import os 
from discord import channel
from discord.ext import commands 
from json import  loads
#from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.messages = True
 

client = commands.Bot(command_prefix='+', intents=intents)  

@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('Hello there!'))
    print("Bot is ready.")

@client.event
async def on_member_join(member): 
    guild= member.guild
    await  member.send(f'hello, dear **{member.name}** welcome to  **{guild.name}** :heart_eyes: \n we are so happy to have you here with us \n I’m brainy\'s wife bot, I can help you discover the server here and I’ll try to answer your questions.\n first of please read the rules carefully in #rules \n so you can introduce yourself in #introduce-yourself-:wave: \n and we have a whole category dedicated to a tech called tech-zone having several channels about different tech fields like #cyber-sec-🔐 , #web-dev-💻 , #mobile-dev-📲 … \n and other categories:  entertainment & hobbies, gaming zone... \n we also have weekly events: like techpoint (type +techpoint to get more information)  that take place each Saturday, and you’ll learn about other events in #announcements \n') 

save =""
@client.command(aliases=['hello','hi'])
async def helo(ctx):
    responses=['Hello there :heart:','Hello :heart: !','Hi, i hope you are doing well']
    await ctx.send(random.choice(responses))

@client.command()
async def by(ctx):
    await ctx.send('by have a nice day :heart: !')

@client.command(aliases=['gdg','GDG_ALGIERS','About_GDG_ALGIERS'])
async def about_GDG_ALGIERS(ctx):
    await ctx.send('GDG Algiers is a local community located at the National Higher School of Computer Science, Algiers, Algeria.It is part of the big global community of developers "Google Developers Group" (960 communities worldwide) Our community is made up of passionate developers and motivated young students.It has started from the simple status of GTUG (Google Technology User Group) in 2011 to become today one of the most active GDGs in the MENA region.GDG Algiers Chapter hosts a variety of technical activities for developers through the different events we organize, aiming to help the developers community get the latest technology updates.')
    global save
    save="gdg"

@client.command()
async def when(ctx):
    global save
    if(save=="wtm_event") :
        await ctx.send('The event will start the 20th May')
    elif (save=="iwd_event") :
        await ctx.send("The will will start the 22th May")
    else :
        await ctx.send("When what?")
    save ="when"

@client.command(aliases=['where','win'])
async def wher(ctx):
    global save 
    if(save=="wtm_event") :
        await ctx.send('The event will be fully Virtual ')
    elif (save=="iwd_event") :
        await ctx.send("The will take place in GDG local")
    elif (save=="gdg") :
        await ctx.send("GDG local is in ESI")
    else :
        await ctx.send("Where what?")
    save ="where"

@client.command(aliases=['thanks','merci','saha'])
async def thank(ctx):
    responses=['you are welcome','avec plasir','bla mziya']
    await ctx.send(random.choice(responses))

@client.command()
async def wtm(ctx):
    await ctx.send('Women Techmakers Algiers')
    global save
    if(save=="where") :
         await ctx.send('The event will be fully Virtual ')
    save = "wtm_event"
    
@client.command()
async def about_wtm(ctx):
    await ctx.send('Shaping the future of technology that will create the outlook we all want to live in by increasing visibility, community, and resources for women in the field. In view of this, Google’s Women Techmakers program has been created in 2012, in order to spread learning and build role models globally, since, more than 200 communities have been launched locally. WTM Algiers is one of these communities, it aims to inspire and enable more women to join the tech industry. Our community, located at the National Higher School of Computer science, Algiers, Algeria, isn’t just driven by developers but anyone who is excited about technology, and focuses on understanding the needs of women and underrepresented groups locally by providing them with experiences and events that are going to best serve them advance in the industry.\nwtm official website :  https://www.wtmalgiers.org/')
    global save
    if(save=="where") :
         await ctx.send('The event will be fully Virtual ')
    save = "wtm_event"

@client.command()
async def wtm_events(ctx):
    await ctx.send('International Women’s Day')  
    global save
    if(save=="where") :
         await ctx.send('The event will be fully Virtual ')
    if(save=="when") :
         await ctx.send("The will will start the 20th May")
    save = "iwd_event"

@client.command()
async def more(ctx): 
    global save
    if(save=="wtm_event") :
        await ctx.send('Shaping the future of technology that will create the outlook we all want to live in by increasing visibility, community, and resources for women in the field. In view of this, Google’s Women Techmakers program has been created in 2012, in order to spread learning and build role models globally, since, more than 200 communities have been launched locally. WTM Algiers is one of these communities, it aims to inspire and enable more women to join the tech industry. Our community, located at the National Higher School of Computer science, Algiers, Algeria, isn’t just driven by developers but anyone who is excited about technology, and focuses on understanding the needs of women and underrepresented groups locally by providing them with experiences and events that are going to best serve them advance in the industry.\nwtm official website :  https://www.wtmalgiers.org/')
        save =""
    elif (save=="gdg") :
        await ctx.send("GDG Algiers official website : https://www.gdgalgiers.com/")
        save =""
    elif (save=="iwd_event") :
        await ctx.send('IWD (International Women’s Day) marked on 8th march every year. An international day celebrating women’s economic, political and social achievements. This year\'s edition intends to train and help the developers community evolve, develop their passion and grow their networks.')
        save =""
    else :
        await  ctx.send("There is nothing searched so that i give you more informations :) ")

@client.command()
async def iwd(ctx):
    await ctx.send('IWD (International Women’s Day) marked on 8th march every year. An international day celebrating women’s economic, political and social achievements. This year\'s edition intends to train and help the developers community evolve, develop their passion and grow their networks.')
    global save 
    if(save=="where") :
         await ctx.send("The will take place in GDG local")
    if(save=="when") :
         await ctx.send("The will will start the 22th May")
    save = "iwd_event"

@client.command()
async def helpme(ctx):  
    await ctx.send('hello I am brainy’s wife :wave: , I’m a bot made by humans \n'
 +'and I’m here to help you discover the server and answer your questions  :hugging: \n '
+'I can answer if you type one of these commands: \n'
+'** +hello,+hi ** :  to welcome you :smile: \n'
+'**+About_GDG_ALGIERS**: to know more about this beautiful supportive community  :gdg: \n'
+'**+when**: to ask about when the event will take place \n'
+'**+where [event] || +win ** ://need to correct this: to ask about where the event will take place \n'
+'**+thanks || +saha or +merci** :  :pray: \n'
+'**+wtm**: introducing women techmakers  :wtm: \n '
+'**+about_wtm**: giving more details about wtm  :wtm: \n'
+'**+wtm_events**: women techmakers events  :wtm: \n'
+'**+about_iwd**:  giving more details about international women’s day \n'
+'make sure to type commands correctly \n'
+'give it a try, let’s chat  :blue_heart: \n'
)

configJson = loads(open("config.json","r").read())

DTOKEN = configJson["TOKEN"]
client.run(DTOKEN) #brainy's wife