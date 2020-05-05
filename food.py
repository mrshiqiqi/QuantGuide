# 一个使用例子
class food:
    """
    食物类，用来存储食物名称
    """
    
    # 设置食物名称
    def set_name(self, name):
        """
        设置食物名称
        :name, 食物名称参数
        """
        self.name = name # self.name 是该类的属性，用来存储数据
        
    # 获取食物名称
    def get_name(self):
        """
        获取食物名称 
        """
        return self.name
