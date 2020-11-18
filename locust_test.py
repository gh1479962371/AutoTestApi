'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
1. 为要模拟的用户定义一个类，从HttpUser继承 
'''
class CarRental(HttpUser):
    # between是User类中定义的一个方法
    # wait_time是User类定义的一个属性，表示等待时间
    wait_time = between(3, 8)  # 任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def loadAllRent(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")

# 阶梯式加压的模型
class StepLoadShape(LoadTestShape):
    """
    A step load shape


    Keyword arguments:

        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds

    """

    step_time = 30    # 两个阶梯时间的时间
    step_load = 10    # 每个阶梯增加的用户数
    spawn_rate = 10   # 用户上线的速率
    time_limit = 600  # 测试的时长

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
# -f 要执行文件
# --host 被测系统
# --web-host Locust web 页面的访问地址
# --web-port Locust web 页面的访问端口
# locust -f locust_test.py --host=http://127.0.0.1:8080 --web-host=127.0.0.1 --web-port=8089
# locust -f locust_test.py --host=http://127.0.0.1:8080
# locust -f locust_test.py --step-load