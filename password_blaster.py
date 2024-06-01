#密码最长度 max_length
#密码最短度 min_length
#起始密码 start_position
#生成策略 暴力生成 mod

import time  
import logging
import logging.config  
import re 
import sqlite3
#正则式无法匹配的字符串实现
def has_no_consecutive_chars(s, min_length=3):  
    # 使用正则表达式找到所有重复的字符序列  
    matches = re.findall(r'(.)\1+', s)  
    # 检查是否有任何匹配的长度大于或等于min_length  
    return not any(len(m[0]) >= min_length for m in matches)  
    
class PasswordGenerator:
    def __init__(self , max_length=20 , min_length=8 , start_position =1):
        self.min_length = min_length  
        self.max_length = max_length  
        self.start_position = start_position 
        self.passwork_key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.passwork_key_num = 62
        self.patterns = [               # 多个正则表达式字符串
            #r'^(?!.*(.)\1\1)[\w\s]*$'   # 不包含3个连续的字符
            r'[A-Z].*',                 # 至少有一个大写字母  
            r'[a-z].*',                 # 至少有一个小写字母  
            r'[0-9].*',                 # 至少有一个数字 
            
        ] 
    def generator_pass(self):
        #生成一次密码
        password = ""
        var3 = self.start_position
        while True:
            var1 = var3 % self.passwork_key_num
            var2 = var3 // self.passwork_key_num
            password += self.passwork_key[var1]
            if var2 < self.passwork_key_num:
                password = password.zfill(self.min_length)
                self.start_position +=1
                return password , self.start_position
            else:
                var3 = var2
    def verify_pass(self,password):
        #对字符串进行多个正则匹配,不匹配立刻返回False，否则返回True
        for pattern in self.patterns:  
            if not re.search(pattern, password):  
                return False  
        #if not has_no_consecutive_chars(password, 3):  
        #    return False  
        # 如果所有条件都满足，则返回True  
        return True  
    def generator(self):
        #生成一次有效的密码
        while True:
            password , start_position =self.generator_pass()
            if self.verify_pass(password):
                return password , start_position
            else:
                password=self.generator_pass()
    def generator_with_position_pass(self,position):
        password = ""
        var3 = position
        while True:
            var1 = var3 % self.passwork_key_num
            var2 = var3 // self.passwork_key_num
            password += self.passwork_key[var1]
            if var2 < self.passwork_key_num:
                password = password.zfill(self.min_length)
                position +=1
                return password , position
            else:
                var3 = var2
        pass
    def generator_with_position(self,position):
        while True:
            password , position =self.generator_with_position_pass(position)
            if self.verify_pass(password):
                return password , position
            else:
                password = self.generator_with_position_pass(position)

# conn = sqlite3.connect('passwords.db')
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    password TEXT,
#                    position INTEGER)''')
# conn.commit()

# generator = PasswordGenerator(max_length=8, min_length=5, start_position=0)


# generator = PasswordGenerator(max_length=8, min_length=5, start_position=0)
# batch_size = 100000  # 每10000条记录提交一次
# passwords_count = 0  # 计数器，跟踪已生成的密码数量

# for _ in range(1000000):
#     password, position = generator.generator()
#     cursor.execute("INSERT INTO passwords (password, position) VALUES (?, ?)", (password, position))
#     passwords_count += 1
#     if passwords_count % batch_size == 0:
#         print(f"已生成并暂存{passwords_count}个密码，准备提交...")
#         conn.commit()
#         print("提交完成。")

# # 处理剩余不足10000个的情况
# if passwords_count % batch_size != 0:
#     print(f"最后一批，已生成{passwords_count}个密码，准备提交...")
#     conn.commit()
#     print("所有密码生成并提交完成。")

# # 关闭数据库连接
# cursor.close()
# conn.close()
generator = PasswordGenerator(max_length=20, min_length=8, start_position=108273487493467203472823460901)

LOGGING = {  
    'version': 1,  
    'disable_existing_loggers': False,  
    'formatters': {  
        'verbose': {  
            'format': '%(asctime)s - %(message)s',  
            'datefmt': '%Y-%m-%d %H:%M:%S'  
        },  
    },  
    'handlers': {  
        'file': {  
            'level': 'INFO',  
            'class': 'logging.FileHandler',  
            'filename': 'app.log',  
            'formatter': 'verbose'  
        },  
        'console': {  
            'level': 'INFO',  
            'class': 'logging.StreamHandler',  
            'formatter': 'verbose'  
        },  
    },  
    'loggers': {  
        'my_logger': {  
            'handlers': ['file', 'console'],  
            'level': 'INFO',  
            'propagate': True,  
        },  
    },  
    'root': {  
        'handlers': ['console'],  
        'level': 'INFO',  
    },  
}  
  
# 使用字典配置日志  
logging.config.dictConfig(LOGGING)  
# 获取或创建logger  
logger = logging.getLogger('my_logger')  
# 构建自定义的日志消息  


Mypassword= "password"
# 记录日志  
import pyautogui    
def simulate_keyboard_input(input_string):  
    for char in input_string:  
        if char.isupper():  
            pyautogui.press(char)  
        else:  
            pyautogui.press(char)  
def onePass(password):
    simulate_keyboard_input(password)
    pyautogui.press('tab')
    simulate_keyboard_input(Mypassword)
    pyautogui.press('tab')
    simulate_keyboard_input(Mypassword)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter') 
    time.sleep(0.3)
    pyautogui.press('enter') 
    pyautogui.press('tab')


pyautogui.PAUSE = 0.025

time.sleep(3) 
password= input()
while 1:
    password,position=generator.generator()
    onePass(password)
    message = f"{password} {position}"  
    logger.info(message)
    
    