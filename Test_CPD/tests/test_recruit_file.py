import pytest

from Utilities.BaseClass import BaseClass
from Utilities.login_helper import login


class Test_Recruit(BaseClass):
    def test_login(self,consultant_maker_credentials):
        login(self.driver,
              consultant_maker_credentials['username'],
              consultant_maker_credentials['password'],
              2)

