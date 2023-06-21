from locators.locators import AuthPageLocators



class TestAuth:
    def test_menu_autorization_must_be(self, auth_page):
        menu_autorization = auth_page.find_element(AuthPageLocators.PAGE_RIGHT)
        result = menu_autorization.text.split("\n")[0]
        assert result == "Авторизация"


    def test_tab_click_telefon_must_be(self,auth_page):
        tab = auth_page.find_element(AuthPageLocators.TAB_PHONE)
        tab.click()
        result = tab.text
        assert result == "Телефон"


    def test_tab_click_mail_must_be(self, auth_page):
        tab = auth_page.find_element(AuthPageLocators.TAB_MAIL)
        tab.click()
        result = tab.text
        assert result == "Почта"

    def test_tab_click_login_must_be(self, auth_page):
        tab = auth_page.find_element(AuthPageLocators.TAB_LOGIN)
        tab.click()
        result = tab.text
        assert result == "Логин"

    def test_tab_click_ls_must_be(self, auth_page):
        tab = auth_page.find_element(AuthPageLocators.TAB_LS)
        tab.click()
        result = tab.text
        assert result == "Лицевой счёт"


    def test_mobile_number_field_must_be_correctness(self, auth_page):
        input_phone = auth_page.find_element(AuthPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys(+71111111111)

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Qwerty123!")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"


    def test_field_must_be_correctness_phone_and_password(self, auth_page):
        input_phone = auth_page.find_element(AuthPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-996-616-45-81")

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("1111")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"


    def test_must_be_correctness_number(self, auth_page):
        input_phone = auth_page.find_element(AuthPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7996616  ")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_CN).text
        assert result == "Неверный формат телефона"


    def test_must_be_autorization_by_phone_a_registraited_user(self, auth_page):
        input_phone = auth_page.find_element(AuthPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-996-616-45-81")

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Qwerty123!")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.get_url()
        assert result == 'https://b2c.passport.rt.ru/account_b2c/page?state=924dba8c-fd63-4430-bdad-2cfc910629f8&client_id=account_b2c#/'



    def test_mail_field_must_be_correctness(self, auth_page):
        input_mail = auth_page.find_element(AuthPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('rost@mail.ru')

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Qwerty123!")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"


    def test_must_be_autorization_by_mail_a_unregistraited_user(self, auth_page):
        input_mail = auth_page.find_element(AuthPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys("rostelecom_tester@mail.ru")

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("0000")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"


    def test_login_field_must_be_correctness(self, auth_page):
        input_login = auth_page.find_element(AuthPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('Логин')

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Qwerty123!")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"

    def test_must_be_login_field(self, auth_page):
        input_login = auth_page.find_element(AuthPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys(" ")

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_CN).text
        assert result == "Укажите логин, указанный при регистрации"

    def test_field_login_and_password_must_be_correctness(self, auth_page):
        auth_page.open()

        input_login = auth_page.find_element(AuthPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('rtkid_1685707787304')

        input_password = auth_page.find_element(AuthPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("1235gdfgs")

        button_to_come_in = auth_page.find_element(AuthPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_ID).text
        assert result == "Неверный логин или пароль"

    def test_personal_account_field_must_be_correctness(self, auth_page):
        input_ls = auth_page.find_element(AuthPageLocators.INPUT_LS)
        input_ls.clear()
        input_ls.send_keys('5960____')

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_CN).text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"

    def test_personal_account_must_be_field(self, auth_page):
        input_ls = auth_page.find_element(AuthPageLocators.INPUT_LS)
        input_ls.clear()
        input_ls.send_keys(' ')

        result = auth_page.find_element(AuthPageLocators.ERROR_MESSAGE_CN).text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"