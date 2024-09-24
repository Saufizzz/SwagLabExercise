from PageObjectModel.AdvancedPage import AdvancedPage
from PageObjectModel.MainPage import MainPage
from Utilities.BaseClass import BaseClass


class TestEbay(BaseClass):

    def test_e2e(self):
        mainpage = MainPage(self.driver)
        advancepage = AdvancedPage(self.driver)
        mainpage.clickAdvanced()
        self.WaitElementClickable(advancepage.KeywordField)
        advancepage.InputKeywordField("Malaysia")
        self.selectByText(advancepage.SelCategory(), "Home & Garden")
        self.ScrollAndLoadAllProducts()
        advancepage.clickCompleteddItem()
        advancepage.clickSoldItem()
        advancepage.clickLocatedIn()
        self.selectByText(advancepage.SelLocatedIn(), "Malaysia")
        self.selectByText(advancepage.SelSortBy(),"Distance: nearest first")
        advancepage.clickSearch()

