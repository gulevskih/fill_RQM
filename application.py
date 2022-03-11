from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def create_and_fill_case(self, case_title):
        wd = self.wd
        # create Case
        wd.find_element_by_xpath("//img[@alt='Create Test Case']").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_ConfirmationDialog_0']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").clear()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_5").send_keys(case_title)
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_1']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()
        wd.find_element_by_xpath("//a[@id='com_ibm_asq_common_web_ui_internal_widgets_tableViewer_ResourceLink_91']/div").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_PopupListChooser_39']/span[3]").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_PopupListChooserItem_272").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7").click()
        Select(wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7")).select_by_visible_text("Unassigned")
        wd.find_element_by_xpath("//select[@id='com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_7']/option[11]").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_5']/div[3]/div/table/tbody/tr[4]/td/div").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_2']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_8").click()
        Select(wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_8")).select_by_visible_text("Automation System Verification Test")
        wd.find_element_by_xpath("//option[@value='_5Rz6sYcXEemyVdksGh6BTw']").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_1']/div/div/div[3]/div[2]/div/div/button[2]").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_DurationWidget_1']/div/input").clear()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_DurationWidget_1']/div/input").send_keys("9")


    def fill_suite_firm(self, suite_title):
        wd = self.wd
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").clear()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_TitleTextAreaEditor_0").send_keys(suite_title)
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_common_RelatedInfo_0']/div").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_0").click()
        Select(wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_0")).select_by_visible_text("M540")
        wd.find_element_by_xpath("//option[@value='_kHqUbqn7EeujZOWsYimMzg']").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_2").click()
        Select(wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_selector_TruncatedSelect_2")).select_by_visible_text("System Verification Test")
        wd.find_element_by_xpath("//option[@value='_38sZEbHSEeujZOWsYimMzg']").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()
        wd.find_element_by_xpath("//li[@id='com_ibm_asq_common_web_ui_internal_widgets_DirectoryPane_0.com.ibm.rqm.execution.editor.section.testcases']/a").click()
        wd.find_element_by_id("dijit_form_RadioButton_0").click()
        wd.find_element_by_xpath("//span[@id='com_ibm_asq_common_web_ui_internal_widgets_Button_69']/a/img").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").click()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").clear()
        wd.find_element_by_id("com_ibm_asq_common_web_ui_internal_widgets_layout_ASQValidateTextBox_1").send_keys("32133")
        wd.find_element_by_name("run").click()
        wd.find_element_by_id("TableViewer_SimpleCheckBox_10-input").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_widgets_SelectionDialog_0']/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/button").click()
        wd.find_element_by_xpath("//div[@id='com_ibm_asq_common_web_ui_internal_view_layout_ViewHeaderLayout_0']/div/div/div[3]/div[2]/div/div/button[2]").click()


    def create_suite(self):
        wd = self.wd
        wd.find_element_by_id("jazz_ui_MenuPopup_8").click()
        wd.find_element_by_id("jazz_ui_menu_MenuItem_7_text").click()


    def login(self):
        wd = self.wd
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").click()
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").clear()
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_userId").send_keys("gulevski")
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_password").click()
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_password").clear()
        wd.find_element_by_id("jazz_app_internal_LoginWidget_0_password").send_keys("theSofa69!")
        wd.find_element_by_xpath("//button[@type='submit']").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("https://rqm01.corp.draeger.global:9443/qm/web/console/IACS%20-%20Cockpit%20%2B%20M540/_yCoMiURCEemDwtfvf4kQTw#action=com.ibm.rqm.planning.home.actionDispatcher&subAction=viewDashboard&team=IACS%20VG8.0%20Verification&tab=_1")

    def destroy(self):
        self.wd.quit()