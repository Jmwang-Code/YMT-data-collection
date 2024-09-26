# 导入selenium模块中的webdriver子模块
from selenium import webdriver

# 导入selenium模块中的chrome子模块的Service类
from selenium.webdriver.chrome.service import Service

# 导入selenium模块中的By类
from selenium.webdriver.common.by import By

# 导入time模块，用于等待页面加载
import time

# 定义一个print_hi函数
def print_hi():
    # 打印输出 'Hello, World!'
    print('Hello, World!')

    # 设置ChromeDriver的路径
    driver_path = r'C:\Users\79283\PycharmProjects\pythonProject\chromedriver.exe'  # 请替换为你的chromedriver路径

    # 创建Service对象，并指定ChromeDriver的路径
    service = Service(driver_path)

    # 创建Chrome浏览器对象，并将Service对象传递给它
    driver = webdriver.Chrome(service=service)

    # 打开指定的URL网页
    #driver.get('https://www.baidu.com')
    driver.get('https://www.ymt.com/')

    # 等待页面加载
    time.sleep(2)

    # Click on the specified element
    element = driver.find_element(By.XPATH, '//a[@href="/hangqing"]')
    element.click()

    # 等待搜索结果加载
    time.sleep(2)

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