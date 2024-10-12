from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys
import os
import pyautogui

from typing import Dict
from Product import Product
from dbapi.MysqlConnector import MySQLConnector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 定义一个函数用于确保元素在视口内
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)  # 等待滚动完成


def move_mouse_naturally_to_element(driver, element):
    # 确保元素在视口内
    scroll_to_element(driver, element)

    # 获取元素在页面中的位置
    location = element.location_once_scrolled_into_view
    size = element.size

    # 模拟分步移动
    for _ in range(random.randint(2, 5)):
        x = location['x'] + random.uniform(-20, 20) + size['width'] / 2
        y = location['y'] + random.uniform(-20, 20) + size['height'] / 2
        pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.5))
        random_sleep(0.5, 1.5)  # 停顿，模拟悬停

    # 最终移动到目标元素中心位置
    pyautogui.moveTo(location['x'] + size['width'] / 2, location['y'] + size['height'] / 2,
                     duration=random.uniform(1, 2))
    time.sleep(random.uniform(0.5, 1.5))

    # 点击目标元素
    pyautogui.click()
    random_sleep(0.5, 1.5)  # 短暂等待，让操作更像人类行为

def random_sleep(min_time=0.5, max_time=2.0):
    time.sleep(random.uniform(min_time, max_time))


# 定义一个print_hi函数
def print_hi():
    print('Hello, World!')

    # 获取当前脚本的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 将dbapi路径添加到模块搜索路径中
    sys.path.append(os.path.join(script_dir, 'dbapi'))

    # 设置ChromeDriver的路径
    driver_path = r'C:\Users\79283\PycharmProjects\pythonProject\chromedriver.exe'  # 请替换为你的chromedriver路径

    # 创建ChromeOptions对象，并设置选项
    options = webdriver.ChromeOptions()
    options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # 创建Service对象，并指定ChromeDriver的路径
    service = Service(driver_path)

    # 创建Chrome浏览器对象，并将Service对象传递给它
    driver = webdriver.Chrome(service=service, options=options)

    # 打开指定的URL网页
    # driver.get('https://www.baidu.com/')
    driver.get('https://www.ymt.com/')

    # 等待页面加载
    time.sleep(2)

    # 找到指定的元素
    element = driver.find_element(By.XPATH, '//a[@href="/hangqing"]')
    random_sleep()
    move_mouse_naturally_to_element(driver, element)
    random_sleep()

    # 等待页面跳转
    time.sleep(3)

    # 找到指定的元素
    element = driver.find_element(By.XPATH, '//input[@placeholder="搜索农产品"]')
    random_sleep()
    move_mouse_naturally_to_element(driver, element)
    random_sleep()

    # 输入搜索内容
    element.send_keys("砂仁")

    # Find the "搜索" button element
    button = driver.find_element(By.XPATH, '//button[contains(text(), "搜索")]')

    random_sleep()
    move_mouse_naturally_to_element(driver, button)
    random_sleep()

    # # 单击按钮
    # button.click()

    sleep(2)

    # 单击链接 寻找阳春砂仁
    link = driver.find_element(By.XPATH, '//a[@href="/hangqing/juhe-306886?breed_id=42788"]')
    random_sleep()
    move_mouse_naturally_to_element(driver, link)
    random_sleep()
    # link.click()

    sleep(2)

    # 确保页面加载完成，可以通过查找新的元素
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div.horizontal.margin')))

    # 获取所有span元素的文本内容
    spans = driver.find_elements(By.CSS_SELECTOR,
                                 '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div.horizontal.margin span')

    # # 遍历所有span元素并打印输出
    # for span in spans: (
    #     print(span.text)
    # )

    # 获取指定元素下所有href属性的个数
    href_elements = driver.find_elements(By.CSS_SELECTOR,
                                         '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) a[href]')
    href_count = len(href_elements)

    # result_dict = {'areas_list': [], 'categories_list': [], 'prices_list': [], 'changes_list': []}
    areas_list = []
    categories_list = []
    prices_list = []
    changes_list = []

    for i in range(1, href_count + 1):
        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > div:nth-child(1) > span.text_product_name.text_align_left'
        )
        areas = driver.find_elements(By.CSS_SELECTOR, selector)
        area_values = [area.text for area in areas]

        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > div:nth-child(2) > span.text_product_name.text_align_left'
        )
        categories = driver.find_elements(By.CSS_SELECTOR, selector)
        category_values = [category.text for category in categories]
        # chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) > a:nth-child(2) > div > span
        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > span'
        )
        prices = driver.find_elements(By.CSS_SELECTOR, selector)
        prices_values = [price.text for price in prices]
        # chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) > a:nth-child(1) > div > div.div_sales.flex_1.horizontal.align_x_right.center_y > div > span
        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > div.div_sales.flex_1.horizontal.align_x_right.center_y > div > span'
        )
        changes = driver.find_elements(By.CSS_SELECTOR, selector)
        changes_values = [change.text for change in changes]

        # Convert price and change values to float
        prices_values = [float(price.split('元/斤')[0]) for price in prices_values]
        changes_values = [float(change.split('元/斤')[0]) for change in changes_values]

        areas_list.append(area_values)
        categories_list.append(category_values)
        prices_list.append(prices_values)
        changes_list.append(changes_values)

    dict1 = dict()

    # 打印输出获取到的信息
    # 封装成对象 product = Product("地区A", "品类1", 10.0, "+0.5")
    for i in range(href_count):
        area = areas_list[i]
        category = categories_list[i]
        price = prices_list[i]
        change = changes_list[i]
        dict1[i] = Product(area, category, price, change)

        print(dict1[i])
        print(f"地区: {area}\n品类: {category}\n价格(元/斤): {price}\n涨跌: {change}\n")

    # 确保页面加载完成，可以通过查找新的元素
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))

    # 获取所有h3标签的文本内容
    # titles = driver.find_elements(By.TAG_NAME, 'h3')

    # 遍历所有标题并打印输出
    # for title in titles:
    #     print(title.text)

    # 关闭浏览器
    driver.quit()

    return dict1


# 如果当前文件被直接执行，则调用print_hi函数
def test_db(dict1: Dict[int, Product]):
    connector = MySQLConnector('123.249.36.184','agricultural_products','123456','agricultural_products')
    connector.test_connection()
    conn_string = "mysql+pymysql://agricultural_products:123456@123.249.36.184/agricultural_products"
    engine = create_engine(conn_string)
    Session = sessionmaker(bind=engine)
    # Create a session using the Session class
    session = Session()

    for key, value in dict1.items():
        # 添加Product对象到会话
        session.add(dict1[key])

    session.commit()
    session.close()

if __name__ == '__main__':
    dict1 = print_hi()
    test_db(dict1)
