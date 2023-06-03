import os
import aqt
from bs4 import BeautifulSoup
from aqt.forms import main, browser, addcards

###
soups = {}
with open(os.path.join(os.path.dirname(main.__file__), 'main.ui'), 'r') as fh:
    soups['main'] = BeautifulSoup(fh.read(), 'xml')
with open(os.path.join(os.path.dirname(browser.__file__), 'browser.ui'), 'r') as fh:
    soups['browser'] = BeautifulSoup(fh.read(), 'xml')
with open(os.path.join(os.path.dirname(addcards.__file__), 'addcards.ui'), 'r') as fh:
    soups['addcards'] = BeautifulSoup(fh.read(), 'xml')

for title, soup_ in soups.items():
    soup: BeautifulSoup = soup_
    for action_ in soup.select('action'):
        if sc_ := action_.select_one('property[name="shortcut"] > string'):
            sc = sc_.string
        else:
            sc = None
        

forms = [('browser', )]        
###

def parse_browser(browser: aqt.browser.Browser):
    
    for action in dir(browser.form):
        if not action.startswith('action'):
            continue
        print(f"action: {action}, type: {type(browser.form[action])}")

aqt.gui_hooks.browser_will_show.append(parse_browser)