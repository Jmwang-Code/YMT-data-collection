from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from Product import Product


# 定义一个函数用于确保元素在视口内
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)  # 等待滚动完成


# 定义一个函数用于模拟自然的鼠标移动
def move_to_element_naturally(driver, element):
    actions = ActionChains(driver)

    # 确保元素在视口内
    scroll_to_element(driver, element)

    # 获取元素的位置和大小
    x_offset = element.location['x'] + element.size['width'] / 2  # 目标元素中心X坐标
    y_offset = element.location['y'] + element.size['height'] / 2  # 目标元素中心Y坐标

    # 移动到目标元素
    actions.move_to_element(element).perform()  # 直接移动到元素

    time.sleep(random.uniform(0.1, 0.3))  # 等待随机时间
    actions.click().perform()  # 点击元素


# 定义一个print_hi函数
def print_hi():
    print('Hello, World!')

    # 设置ChromeDriver的路径
    driver_path = r'C:\Users\79283\PycharmProjects\pythonProject\chromedriver.exe'  # 请替换为你的chromedriver路径

    # 创建Service对象，并指定ChromeDriver的路径
    service = Service(driver_path)

    # 创建Chrome浏览器对象，并将Service对象传递给它
    driver = webdriver.Chrome(service=service)

    # 打开指定的URL网页
    driver.get('https://www.ymt.com/')

    # 等待页面加载
    time.sleep(2)

    # 找到指定的元素
    element = driver.find_element(By.XPATH, '//a[@href="/hangqing"]')

    # 模拟自然鼠标移动并点击
    move_to_element_naturally(driver, element)

    # 等待页面跳转
    time.sleep(3)

    # 找到指定的元素
    element = driver.find_element(By.XPATH, '//input[@placeholder="搜索农产品"]')

    # 输入搜索内容
    element.send_keys("砂仁")

    # Find the "搜索" button element
    button = driver.find_element(By.XPATH, '//button[contains(text(), "搜索")]')

    # 单击按钮
    button.click()

    sleep(2)

    # 单击链接 寻找阳春砂仁
    link = driver.find_element(By.XPATH, '//a[@href="/hangqing/juhe-306886?breed_id=42788"]')
    link.click()

    sleep(2)

    # 确保页面加载完成，可以通过查找新的元素
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-v-529211f5]')))
    #
    # # 获取所有span元素的文本内容
    # spans = driver.find_elements(By.CSS_SELECTOR, 'div.horizontal.margin span')
    #
    # # 遍历所有span元素并打印输出
    # for span in spans:
    #     print(span.text)

    # 确保页面加载完成，可以通过查找新的元素
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div.horizontal.margin')))

    # 获取所有span元素的文本内容
    spans = driver.find_elements(By.CSS_SELECTOR,
                                 '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div.horizontal.margin span')

    # 遍历所有span元素并打印输出
    for span in spans: (
        print(span.text))

    # 获取所有span元素的文本内容
    # spans = driver.find_elements(By.CSS_SELECTOR,
    #                              '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) span')

    # # 将文本内容存储在一个列表中
    # data = [span.text for span in spans]

    # # 打印输出列表中的数据
    # for d in data:
    #     print(d)

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

        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > div:nth-child(2) > span.text_product_name.text_align_left'
        )
        categories = driver.find_elements(By.CSS_SELECTOR, selector)

        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > span'
        )
        prices = driver.find_elements(By.CSS_SELECTOR, selector)

        selector = (
            '#chandi_trend_price > div.bg.chandi_hangqing_detail_list > div:nth-child(5) '
            f'> a:nth-child({i}) > div > span'
        )
        changes = driver.find_elements(By.CSS_SELECTOR, selector)

        areas_list.append(areas)
        categories_list.append(categories)
        prices_list.append(prices)
        changes_list.append(changes)

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


# 如果当前文件被直接执行，则调用print_hi函数
if __name__ == '__main__':
    print_hi()
