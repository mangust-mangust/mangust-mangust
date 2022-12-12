from ast import alias
import asyncio
from cgitb import text
from distutils.sysconfig import PREFIX
from pydoc import describe
from turtle import title
from urllib import request
import discord
from discord.ext import commands
import random
import aiohttp

channelIDS= 847202767772188713
channelIDS2= 847212309494366278
TOKEN= ' '
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '+', intents=intents)
bot.remove_command( 'help' )
title_hello=['Доброго времени суток',"Здраствуй)","Нихрена..Кто же заглянул в эту глушь..","Приветик~","А вот и он..","Приветствую тебя"]
hello=['https://image.myanimelist.net/ui/gDEE1QGHMmMAOJRb4Q-ehqF7ckhcVAUyzogC6VP5vLR4ILIAHotU84aGAV_ihyEjUE7hToGq7Qf4W4nsPugrgp-44K87QbbXDRU6qzb7SDw1u8zz8srGrKBe5Yk39GZH','https://pa1.narvii.com/7506/779525507f8fa48b3e5b31096df2564cd4052230r1-540-304_hq.gif','https://i.gifer.com/embedded/download/VW9t.gif','https://avatars.mds.yandex.net/i?id=6e74ed1fbda2883b93989d62cdfd00d6-4119126-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=41b07c68e4ea335bfa6ac3c35eb3abb4-5219071-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=7ddd3835d24ed7eb3fb16b5af6e23407-5241671-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=8607d37ad2cbf0861d7fe8777aee3019-5147303-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=e62c3bf40ffa1ae93f6ae5adaf856f7b-5723597-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=8e162d47812b0c4068b2458369f8fe46-4466230-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=2a0000017a12d3ba2f00a554096194b305a6-4513470-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=39ee6bf3772cf1f6bca22116835bb895-3674804-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=ca28e257d4ecd50f7a822ab5f738be91-5268868-images-thumbs&n=13&exp=1','https://avatars.mds.yandex.net/i?id=892570e23ede50b4d3306d7d061e6eea-5427440-images-thumbs&n=13&exp=1'," https://pa1.narvii.com/7217/6712e821f2505f8377a9803c7c491c33d12df527r1-538-302_hq.gif","https://avatars.mds.yandex.net/i?id=25c510330142c55659b72d3965d2ae75-5232263-images-thumbs&n=13&exp=1","https://yandex-images.clstorage.net/5WKUz1169/4c13b5lh7p/mT-_mgQhREei-EpV_tjVuDqKf57NwagwAk86CEUT4bEDd0vXeK4DANqgZI-nCIGqm24j2MnKkcfUur02PYABvNtr-dYfPwtNo_hJWPfD3L8xgnCWydWvMloYIQ8bVLmyH2ZO1xOVJCetxx6423up0oQ8fo-d0NyNkdfbO1zDet-VLLi6PysDWrTgM2bT5NKfIOV_rsmYpWwAaEYvB2_ujS9kN6otqCMTp-wUudZMkMulH2mbk8yxrIjr52FF0l3EqS2HnjM5OUSR2StlztnhsQPyc7jRo7VbJ2RxBCdv0aEgdTWUCpwQHqr2JoXbWIbLuxZXjLLslLmS8PdIaMtm7JsTr4M1Kw9liNgxXsns2o4E4km5_YaHdxpYYggbYM20DkE-gyqFDDeA1CWd2l2W5oUuRqKc_5umj-zSdVrKaNuoOr-YLBMzbKnpB2TL4vyeNcJyuduBrlUsQXAdOUDamRFUBrcFsBUcneA6jedEkfinFX2hj-maqrfPwmt44EX4qRacvzoeOke15AVOztTdlyPgXbn0vq9oKUlPJCVy67wyQDmkBKUDCYXvBaboTYfNsBZqrr3dtrSjyfVJSvte5a0ZnqggMxBusu8jVcrvwrox3Wa4ybalewlmbwEyZsiALXEirCC-FxWt2gO6wGWKzpY-dayA8ZuIo_j9VU31VuSeFKyyGQgiX7ToFnTz5uWSMcJ7rNOhm0w7akwlL03wgSp3ObY8shATjukimNl6qf2rNUimk_2XvpLSxmxo8VDFpC28kAYqJk2s4Q5-0czjiRTPfLDupa9mIkdFLyxDzLwQXgmOAbgADrbrAZP6Wo_EtylCr7PbvrOc_MlWQcl32Ywbuq4ANwdAqeIDQevx54wR7Fayy6u4fxJIYhslYsORA1ckkSO6EgOd0AKL9HW35ZgOao2P-LOevMLtSmrrdd6DMp2ZBDAzWLT4E1XxwNyVKdx_jcGEkGghZGUMMUY"]
while1=[' https://ic.pics.livejournal.com/egor_23/73280836/3981877/3981877_original.gif',"https://avatars.mds.yandex.net/i?id=51fd1a679e1493cf9bb9b12bdeca0978-5309200-images-thumbs&n=13&exp=1","https://avatars.mds.yandex.net/i?id=2a00000179f5f1440850817a2f76e1396784-3675407-images-thumbs&n=13&exp=1","https://pa1.narvii.com/8201/e1a36c13da3077ec1cd0fa2165042d834f472ba3r1-500-217_hq.gif","https://steamuserimages-a.akamaihd.net/ugc/943966739338620791/A927F99947AF8EE57C6CE783D0E7FB322A8816EB/?imw=512&amp;imh=288&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true","   https://avatars.mds.yandex.net/i?id=288e79cdbf25a2156400066f5f2d77dc-4628606-images-thumbs&n=13&exp=1","https://avatars.mds.yandex.net/i?id=8b4a0cd4e9dc8868c5822ad838fbe2e0-5094289-images-thumbs&n=13&exp=1","https://yandex-images.clstorage.net/5WKUz1169/4c13b5lh7p/mT-_mgQhREei-EpV_tjVuDqKf57NwagwAk86WBcQ5-AGJxLRePJRV9v9ZYujWtKrnzgijc-ZxpvUsLE2Oo4JsNtt89YfPwtNo_hJWPfD3L8xgnCWydWvMloYIQ8bVLmyH2ZO1xOVJCetxx6423up0oQ8fo-d0NyNkdfbO1zDet-VLLi6PysDWrTgM2bT5NKfIOV_rsmYpWwAaEYvB2_ujS9kN6otqCMTp-wUudZMkMulH2mbk8yxrIjr52FF0l3EqS2HnjM5OUSR2StlztnhsQPyc7jRo7VbJ2RxBCdv0aEgdTWUCpwQHqr2JoXbWIbLuxZXjLLslLmS8PdIaMtm7JsTr4M1Kw9liNgxXsns2o4E4km5_YaHdxpYYggbYM20DkE-gyqFDDeA1CWd2l2W5oUuRqKc_5umj-zSdVrKaNuoOr-YLBMzbKnpB2TL4vyeNcJyuduBrlUsQXAdOUDamRFUBrcFsBUcneA6jedEkfinFX2hj-maqrfPwmt44EX4qRacvzoeOke15AVOztTdlyPgXbn0vq9oKUlPJCVy67wyQDmkBKUDCYXvBaboTYfNsBZqrr3dtrSjyfVJSvte5a0ZnqggMxBusu8jVcrvwrox3Wa4ybalewlmbwEyZsiALXEirCC-FxWt2gO6wGWKzpY-dayA8ZuIo_j9VU31VuSeFKyyGQgiX7ToFnTz5uWSMcJ7rNOhm0w7akwlL03wgSp3ObY8shATjukimNl6qf2rNUimk_2XvpLSxmxo8VDFpC28kAYqJk2s4Q5-0czjiRTPfLDupa9mIkdFLyxDzLwQXgmOAbgADrbrAZP6Wo_EtylCr7PbvrOc_MlWQcl32Ywbuq4ANwdAqeIDQevx54wR7Fayy6u4fxJIYhslYsORA1ckkSO6EgOd0AKL9HW35ZgOao2P-LOevMLtSmrrdd6DMp2ZBDAzWLT4E1XxwNyVKdx_jcGEkGghZGUMMUY"]
title_while=['Было приятно с тобой общаться'," Земля тебе пухом","До скоых встречь","Пока","Встретитмся в новой жизни...","...Досвинания мой господин~",'Ты был прекрасным человеком..возможно)'," Эх..а ты мне так нравился, возможно :-)"," Наеюсь мы ещё уввидемся","Акоп!","Пора в путь.", "Бай-бай, батерфляй."]
wersteam='https://cdn.discordapp.com/attachments/904685423639552001/1019264028184424448/42_20220913181107.png'
img_hug = ["https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif", "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif", "https://c.tenor.com/4n3T2I239q8AAAAC/anime-cute.gif", "https://c.tenor.com/ztEJgrjFe54AAAAC/hug-anime.gif", "https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif", "https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif", "https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif", "https://c.tenor.com/SXk-WqF6PpQAAAAC/anime-hug.gif", "https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif", "https://c.tenor.com/SPs0Rpt7HAcAAAAC/chiya-urara.gif", "https://c.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif", "https://c.tenor.com/jQ0FcfbsXqIAAAAC/hug-anime.gif", "https://c.tenor.com/z2QaiBZCLCQAAAAC/hug-anime.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", "https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif", "https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif", "https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif", "https://c.tenor.com/WpbZhwwj6zAAAAAC/happy-hug.gif", "https://c.tenor.com/EnfEuWDXthkAAAAC/hug-couple.gif"]
memes_text=['Лови мемас','Внимание аникдот',"МЕМ","пиздец..."]
memes_art=['https://otvet.imgsmail.ru/download/220649632_160ae985d8e6a7527fc6a65a2cb45efc_800.jpg', "https://shutok.ru/uploads/posts/2020-10/1602152847_14800732.jpg",'https://i.pinimg.com/736x/f7/e2/47/f7e2478a6c3528be014393deb3f548b2.jpg','http://risovach.ru/upload/2019/06/mem/etot-moment-kogda_210745044_orig_.jpg','https://sun9-82.userapi.com/impf/JL9zBQVW-gfaasPlz8ZyzGj3txwxLcG2uUPagA/e_xE24j9c_A.jpg?size=593x374&quality=96&sign=9f138608994f90b299a156f6744d48ae&type=album','http://risovach.ru/upload/2016/10/mem/voenkom-polkovnik_126109616_orig_.jpg','https://sun9-80.userapi.com/impg/1WXyoJIuTjc_z5L_pNV9EISKrLGTWEwNqcA40w/oHaJXZQW1VA.jpg?size=604x453&quality=96&sign=b959b8968278fdbbcef9286830de76b8&type=album','http://risovach.ru/upload/2013/10/mem/gost_32871899_orig_.jpg','image.png','http://risovach.ru/upload/2013/07/mem/nu-pochemu_23944241_orig_.jpg','https://otvet.imgsmail.ru/download/179676993_f07626b89abe87f5dc9080af85691051_800.jpg','https://pm1.narvii.com/6778/0e8239f57e4b2606d9431a01eecc9216a9f0098fv2_hq.jpg','http://risovach.ru/upload/2015/10/mem/or-fray-v-panike_95287759_orig_.jpg','http://img.1001mem.ru/posts/3822000/3821737.jpg','https://i.ucrazy.ru/files/pics/2018.08/242018-8-23-14_50_24.jpg','https://www.meme-arsenal.com/memes/aebaa63423c7ff26c720bcb4ca7a7a78.jpg','https://sun9-53.userapi.com/impg/c858532/v858532751/7b164/nYEVDlPu2ms.jpg?size=604x483&quality=96&sign=c32d6903a8d2139cce4cd6266cb58155&type=album','https://sun9-77.userapi.com/impf/c850132/v850132078/e18dc/j03xQMSp9aA.jpg?size=409x604&quality=96&sign=b915ded9933356b06cff8a1da649e9f4&type=album','http://memesmix.net/media/created/dyv4t5.jpg','https://sun9-32.userapi.com/impg/dPo0D6P9k9-LNoZ2hVzcBC-e1PWKwAm_z6VG4A/CNUij44JI08.jpg?size=604x453&quality=96&sign=70e085e4352e9982f1b2b81df5d87ce5&type=album','https://static.diary.ru/userdir/2/6/5/5/2655009/73507994.jpg','https://theslide.ru/img/thumbs/9a44f70b276bd3d9c98af4369ffbd0f5-800x.jpg','http://risovach.ru/thumb/upload/200s400/2016/06/mem/xzibit_117605997_orig_.jpg?c7zff','http://risovach.ru/upload/2014/07/mem/roma-mehanik_54897812_orig_.jpeg']
kick_in_the_ass=['https://i.gifer.com/ApIn.gif','https://i.gifer.com/Vx5G.gif','http://img10.reactor.cc/pics/comment/ToAru-Anime-ББПЕ-Anime-Гифки-1237956.gif','https://i.gifer.com/VCCJ.gif','https://i.pinimg.com/originals/37/a6/04/37a6048880172e7220a32f561e63ba5c.gif','https://media.moddb.com/images/groups/1/25/24269/t3_56xx0a.gif','https://safebooru.org/images/1882/605143df221803e99f3b5423f1df4c8b76bd8ae9.gif?1964756','http://img10.reactor.cc/pics/comment/ToAru-Anime-ББПЕ-Anime-Гифки-1237952.gif','https://giffiles.alphacoders.com/200/200650.gif']
kick_in_the_ass_text=['брат...ты попал...','могу только посачуствовать)','Быстрые ноги пизды не боятся','ИДИ РАБОТАЙ!','Пошёл нахуй.','Будь нежен со мной','Ручки видишь, а ботинок вот он']

@bot.event
async def on_ready():
    print("Я запущен!")

    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Genshin Impact') )

@bot.command(aliases=['очисть'])
async def clear(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send('Мои усилия только для вас мой господин~')

@bot.command(aliases=['мем'])
async def mem(ctx):
    author = ctx.message.author
    embed = discord.Embed(
    title=F'{random.choice(memes_text)}',
    color = 0xe100ff,)
    embed.set_image(url=f'{random.choice(memes_art)}')
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=['обн'])
async def hug(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел объять.\nПопробуй так: `+hug @человек`")
    author = ctx.author
    embed = discord.Embed(
        color = 0xe100ff,
        description = f"{author.mention} обнял {member.mention}")
    embed.set_image(url=f'{random.choice(img_hug)}')
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=['пинок_под_зад'])
async def kick(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)
    if member == None:
        await ctx.send("Быстрее, пинай пока не сбежал.\nПопробуй так: `+kick @человек`")
    author = ctx.author
    embed = discord.Embed(
        title=F'{random.choice(kick_in_the_ass_text)}',
        color = 0xe100ff,
        description = f"{author.mention} пнул {member.mention}")
    embed.set_image(url=f'{random.choice(kick_in_the_ass)}')
    author = ctx.message.author
    embed.set_footer(text=f"Тебя пнул {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)    

@bot.command(aliases=['помощь'])
async def help(ctx):
    emb=discord.Embed(title='всё что я пока что умею:(')
    emb.add_field(name='+очисть'.format(PREFIX), value='очистит столько сообщений сколько укажешь')
    emb.add_field(name='+пинок_под_зад'.format(PREFIX), value='пнёт под зад твоего друга')
    emb.add_field(name='+мем'.format(PREFIX), value='пришлёт тебе мемасик')
    emb.add_field(name='+обн'.format(PREFIX), value='он может тебя обнять от лица автора, а вообще эта команда реагирует не только на +обн, но так же на +обними, +обнять, +обнимашки и т.п')
    emb.add_field(name='++"город"'.format(PREFIX), value='он сыграет с тобой в города, команда ещё не доделанна но уже рабочая')
    await ctx.send(embed=emb)

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel=bot.get_channel(channelIDS)
    embed=discord.Embed(title=f'{random.choice(title_hello)}', description=f"Мы ждали тебя, {member.mention} Для начала настоятельно рекомендую прочитать #╔правила📃 , перед началом общения в #╔чат . А если ты пришел работать, то заполни #╠анкета")
    embed.set_image(url=f'{random.choice(hello)}')
    embed.set_footer(text=f"Мы очень рады вас видеть!")
    await channel.send(embed= embed)

@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel=bot.get_channel(channelIDS2)
    embed=discord.Embed(title=f'{random.choice(title_while)}', description=f"эх...{member.mention} было приятно пообщаться")
    embed.set_image(url=f'{random.choice(while1)}')
    embed.set_footer(text=f"кидалова!")
    await channel.send(embed= embed)

bot.run(TOKEN)


