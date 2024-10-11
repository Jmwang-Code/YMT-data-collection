from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import DateTime

Base = declarative_base()

class Product(Base):
    '''
    从Python 3.5开始，你可以使用类型提示来指定变量、参数和函数的类型。
    类型提示是一种在变量、参数和函数中添加类型信息的注释语法。
    虽然这些类型提示不会强制执行类型，但它们可以提供更好的可读性和代码提示，并允许静态类型检查工具对代码进行类型检查。
    '''
    __tablename__ = 'ymt_products'  # 数据库表名

    def __init__(self, area: str, category: str, price: float, change: float):
        self.area = area
        self.category = category
        self.price = price
        self.change = change
        self.create_time = datetime.now()

    id = Column(Integer, primary_key=True)
    area = Column(String)
    category = Column(String)
    price = Column(Float)
    change = Column(String)
    create_time = Column(DateTime, default=datetime.now)  # Add create_time field

    # def __init__(self, area: str, category: str, price: float, change: str):
    #     # 地区
    #     self.area = area
    #     # 品类
    #     self.category = category
    #     # 价格
    #     self.price = price
    #     # 涨跌
    #     self.change = change
    #     # 时间
    #     self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self) -> str:
        return f"Product(area={self.area}, category={self.category}, price={self.price}, change={self.change}, create_time={self.create_time})"