import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

#PATH = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1400x1000")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


class Build(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def build(self, ctx, champion, role=None):
        driver.get('https://u.gg/')
        driver.maximize_window()

        driver.implicitly_wait(10)

        search = driver.find_element_by_name('query')
        search.send_keys(champion)
        search.send_keys(Keys.RETURN)

        


        if (role == 'top'):
            top = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[4]/div/div/div[3]/div[1]')
            top.click()
        elif (role == 'jg' or role == 'jungle'):
            jg = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[4]/div/div/div[3]/div[2]')
            jg.click()
        elif (role == 'mid'):
            mid = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[4]/div/div/div[3]/div[3]')
            mid.click()
        elif (role == 'support' or role == 'sup'):
            sup = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[4]/div/div/div[3]/div[4]')
            sup.click()
        elif (role == 'adc' or role == 'ad'):
            adc = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[4]/div/div/div[3]/div[5]')
            adc.click()

        
        driver.implicitly_wait(10)

        runes = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[5]/div/div[2]/div[1]')
        time.sleep(0.5)
        runes.screenshot("runes.png")
        print(runes)

        driver.execute_script('window.scrollBy(0,200)')

        skill_path = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[5]/div/div[4]')
        time.sleep(0.5)
        skill_path.screenshot('skill_path.png')
        '''
        try: 
            close_ad = driver.find_element_by_xpath('//*[@id="desktop-anchor-close"]')
            close_ad.click()
        except:
            print('no ad found')
        '''

        items = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[5]/div/div[7]')
        time.sleep(0.5)
        items.screenshot('items.png')


        await ctx.send(file=discord.File('runes.png'))
        await ctx.send(file=discord.File('skill_path.png'))
        await ctx.send(file=discord.File('items.png'))

        

    @commands.command()
    async def counters(self, ctx, champion):
        driver.get('https://u.gg/')
        driver.maximize_window()

        driver.implicitly_wait(10)

        search = driver.find_element_by_name('query')
        search.send_keys(champion + ' counters')
        search.send_keys(Keys.RETURN)

        driver.implicitly_wait(10)

        counters = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[5]')
        time.sleep(0.5)
        driver.execute_script('window.scrollBy(0,1500)')
        time.sleep(0.5)
        counters.screenshot('counters.png')

        await ctx.send(file=discord.File('counters.png'))

        



def setup(bot):
    bot.add_cog(Build(bot))




        

        




