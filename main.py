from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


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

    # 确保页面加载完成，可以通过查找新的元素
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))

    # 获取所有h3标签的文本内容
    titles = driver.find_elements(By.TAG_NAME, 'h3')

    # 遍历所有标题并打印输出
    for title in titles:
        print(title.text)

    # 关闭浏览器
    driver.quit()


# 如果当前文件被直接执行，则调用print_hi函数
if __name__ == '__main__':
    print_hi()

