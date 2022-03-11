# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://rqm01.corp.draeger.global:9443/qm/web/console/IACS%20-%20Cockpit%20%2B%20M540/_yCoMiURCEemDwtfvf4kQTw#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewDashboard&team=IACS%20VG8.0%20Verification&tab=_1")
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").click()
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").clear()
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").send_keys("gulevski")
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_password").click()
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_password").clear()
        driver.find_element_by_id("jazz_app_internal_LoginWidget_0_password").send_keys("theSofa69!")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("jazz_ui_MenuPopup_8").click()
        driver.find_element_by_id("jazz_ui_menu_MenuItem_7_text").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").clear()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").send_keys("Test suite for M540_ATC_13291 Diastolic high alarm limit Adult mmHg")
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_RelatedInfo_0']/div").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_0").click()
        Select(driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_0")).select_by_visible_text("M540")
        driver.find_element_by_xpath("//option[@value='_kHqUbqn7EeujZOWsYimMzg']").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_2").click()
        Select(driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_2")).select_by_visible_text("System Verification Test")
        driver.find_element_by_xpath("//option[@value='_38sZEbHSEeujZOWsYimMzg']").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()
        driver.find_element_by_xpath("//li[@id='com_ibm_asq_common_web_ui_internal_widgets_DirectoryPane_0.com.ibm.rqm.execution.editor.section.testcases']/a").click()
        driver.find_element_by_id("dijit_form_RadioButton_0").click()
        driver.find_element_by_xpath("//span[@id='com_ibm_asq_common_web_ui_internal_widgets_Button_69']/a/img").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").clear()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").send_keys("32133")
        driver.find_element_by_name("run").click()
        driver.find_element_by_id("TableViewer_SimpleCheckBox_10-input").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_0']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()
        driver.find_element_by_xpath("//img[@alt='Create Test Case']").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_ConfirmationDialog_0']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").clear()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").send_keys("M540_ATC_13291 Diastolic high alarm limit Adult mmHg")
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_1']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()
        driver.find_element_by_xpath("//a[@id='com_ibm_asq_common_web_ui_internal_widgets_tableViewer_ResourceLink_91']/div").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_PopupListChooser_39']/span[3]").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_PopupListChooserItem_272").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7").click()
        Select(driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7")).select_by_visible_text("Unassigned")
        driver.find_element_by_xpath("//select[@id='com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7']/option[11]").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_5']/div[3]/div/table/tbody/tr[4]/td/div").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_2']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_8").click()
        Select(driver.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_8")).select_by_visible_text("Automation System Verification Test")
        driver.find_element_by_xpath("//option[@value='_5Rz6sYcXEemyVdksGh6BTw']").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_1']/div/div/div[3]/div[2]/div/div/button[2]").click()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_DurationWidget_1']/div/input").clear()
        driver.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_DurationWidget_1']/div/input").send_keys("9")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
