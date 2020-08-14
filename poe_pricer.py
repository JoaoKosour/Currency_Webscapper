from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#LINKS TO INITIATE EVALUATION
buyAlteration = 'https://www.pathofexile.com/trade/exchange/Harvest/Ny7gfR'
sellAlteration = 'https://www.pathofexile.com/trade/exchange/Harvest/AjnbtX'

buyFusing = 'https://www.pathofexile.com/trade/exchange/Harvest/AjoXSX'
sellFusing = 'https://www.pathofexile.com/trade/exchange/Harvest/AoJrFl'

buyScouring = 'https://www.pathofexile.com/trade/exchange/Harvest/rbdMHQ'
sellScouring = 'https://www.pathofexile.com/trade/exchange/Harvest/EBEzt5'

buyVaal = 'https://www.pathofexile.com/trade/exchange/Harvest/18GVuV'
sellVaal = 'https://www.pathofexile.com/trade/exchange/Harvest/EB9LC5'

buyRegret = 'https://www.pathofexile.com/trade/exchange/Harvest/zbJai4'
sellRegret = 'https://www.pathofexile.com/trade/exchange/Harvest/9z6ztK'

buyChiesel = 'https://www.pathofexile.com/trade/exchange/Harvest/zbVRF4'
sellChiesel = 'https://www.pathofexile.com/trade/exchange/Harvest/4my8I9'

buyAlchemy = 'https://www.pathofexile.com/trade/exchange/Harvest/yYYOiR'
sellAlchemy = 'https://www.pathofexile.com/trade/exchange/Harvest/rPe7CQ'

buyJeweller = 'https://www.pathofexile.com/trade/exchange/Harvest/2n56EO0ck'
sellJeweller = 'https://www.pathofexile.com/trade/exchange/Harvest/akeX753he'


def find_price_buy(driver, link):
    #importing the desired link
    driver.get(link)
    driver.implicitly_wait(10)

    #selecting the div containing all the price listing information
    prices = driver.find_elements_by_css_selector('.results .row .details .price .per-have')
    precos = [preco.text for preco in prices]
    s = precos[len(precos) - 7]
    s = s.replace(' ×  is worth', '')
    s = s.replace('×', '')
    a,b = s.split(' ', 1)
    return float(b)


def find_price_sell(driver, link):
    #importing the desired link
    driver.get(link)
    driver.implicitly_wait(4)

    #selecting the div containing all the price listing information
    prices = driver.find_elements_by_css_selector('.results .row .details .price .per-want')
    precos = [preco.text for preco in prices]
    s = precos[len(precos) - 7]
    s = s.replace(' ×  is worth', '')
    s = s.replace('×', '')
    a,b = s.split(' ', 1)
    return float(b)


def evaluate_trade(driver, name, buy, sell):
    print(name)
    buy_price = find_price_buy(driver, buy)
    sell_price = find_price_sell(driver, sell)
    profit_percentage = (((sell_price - buy_price)/sell_price) * 100)
    profit = "{:.2f}".format(profit_percentage)
    sell_for = "{:.2f}".format(1/sell_price)
    print('Buy for '+str(buy_price)+' Sell for '+str(sell_price)+' ('+sell_for+'c)'+' | '+profit+'% profit per orb.\n')


def setup_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    return driver


def main():
    webdriver = setup_webdriver()
    evaluate_trade(webdriver, 'Alteration', buyAlteration, sellAlteration)
    evaluate_trade(webdriver, 'Fusing', buyFusing, sellFusing)
    evaluate_trade(webdriver, 'Scouring', buyScouring, sellScouring)
    evaluate_trade(webdriver, 'Vaal', buyVaal, sellVaal)
    evaluate_trade(webdriver, 'Regret', buyRegret, sellRegret)
    evaluate_trade(webdriver, 'Chiesel', buyChiesel, sellChiesel)
    evaluate_trade(webdriver, 'Alchemy', buyAlchemy, sellAlchemy)
    evaluate_trade(webdriver, 'Jeweller', buyJeweller, sellJeweller)
    webdriver.close()
    

if __name__=='__main__':
    main()






























































    