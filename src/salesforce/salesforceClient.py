from src.commonClient import CommonClient


class SalesforceClient(CommonClient):
    def __init__(self, with_login=False, default_wait_time=10):
        super().__init__("salesforce", default_wait_time)
        if with_login:
            self.__login__()

    def __login__(self):
        self.driver.get(self.mainUrl)

    def dispose(self):
        self.driver.quit()
