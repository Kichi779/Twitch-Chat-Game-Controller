import time
import os
from twitchio.ext import commands
import keyboard
import mouse
from pystyle import Center, Colors, Colorate
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system('title Kichi779 - Twitch Chat Game Controller v1')

print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter("""
           
                             ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                             ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                             ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                            ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                           ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                             ███▐██▄   ███   ███    █▄    ███    ███   ███  
                             ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                             ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                             ▀                                             
                         Edit the code, but please don't remove my name. 
                               Discord https://discord.gg/aVk4JUFukk       
                               Github  https://github.com/kichi779          
                       
                      
                      """)))


class Bot(commands.Bot):

    def __init__(self):
        # Enter the ACCESS TOKEN in the Token section (If you don't know how to get it, read my github page). initial_channels=['xxx']) Enter the name of your channel here.
        super().__init__(token='xxx', prefix='!', initial_channels=['xxxx'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print(Fore.GREEN + "The bot has started working on your channel !help" + Fore.RESET)
        print(Fore.YELLOW +"This code is open source and free, please don't forget to leave stars on github." + Fore.RESET)

    @commands.command()
    async def help(self, ctx: commands.Context):
      await ctx.send(f'Command List = !w !a !s !d !jump !longjump !rjump !ljump !rljump !lljump !looku !lookd !euse {ctx.author.name}!')


    @commands.command()
    async def w(self, ctx: commands.Context):
        keyboard.press('w')
        time.sleep(0.4)
        keyboard.release('w')

    @commands.command()
    async def a(self, ctx: commands.Context):
        keyboard.press('a')
        time.sleep(0.5)
        keyboard.release('a')

    @commands.command()
    async def s(self, ctx: commands.Context):
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')

    @commands.command()
    async def d(self, ctx: commands.Context):
        keyboard.press('d')
        time.sleep(0.5)
        keyboard.release('d')

    @commands.command()
    async def jump(self, ctx: commands.Context):
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')

    @commands.command()
    async def rjump(self, ctx: commands.Context):
        keyboard.press('d')
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        keyboard.release('d')

    @commands.command()
    async def ljump(self, ctx: commands.Context):
        keyboard.press('a')
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        keyboard.release('a')

    @commands.command()
    async def longjump(self, ctx: commands.Context):
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('space')

    @commands.command()
    async def rljump(self, ctx: commands.Context):
        keyboard.press('d')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('d')
        keyboard.release('space')

    @commands.command()
    async def lljump(self, ctx: commands.Context):
        keyboard.press('a')
        keyboard.press('space')
        time.sleep(2)
        keyboard.release('a')
        keyboard.release('space')

    @commands.command() 
    async def lookr(self, ctx: commands.Context):
       mouse.move(500, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def lookl(self, ctx: commands.Context):
       mouse.move(500, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def lookd(self, ctx: commands.Context):
       mouse.move(0, 500, absolute=False, duration=0.2)

    @commands.command() 
    async def looku(self, ctx: commands.Context):
       mouse.move(0, -500, absolute=False, duration=0.2)



bot = Bot()
bot.run()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
