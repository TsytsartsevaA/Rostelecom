from locators.locators import AuthPageLocators, RegistrationPageLocators



class TestRegistration:
    def test_must_be_register_link(self, reg_page):
        link = reg_page.find_element(AuthPageLocators.LINK_REGISTER)
        result = link.text
        assert result == "Зарегистрироваться"

    def test_field_first_name_must_be_correctness(self, reg_page):
        input_first_name = reg_page.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys('An')

        button_register = reg_page.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()

        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Необходимо заполнить поле кириллицей. От 2 до 30 символов"

    def test_field_last_name_must_be_correctness(self, reg_page):
        input_last_name = reg_page.find_element(RegistrationPageLocators.INPUT_LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys('Tsytsartseva')

        button_register = reg_page.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()

        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Необходимо заполнить поле кириллицей. От 2 до 30 символов"

    def test_field_phone_must_be_correctness(self, reg_page):
        input_address = reg_page.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("+375-29-123-  ")

        button_page_register = reg_page.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_page_register.click()

        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Сообщение введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    def test_field_email_must_be_correctness(self, reg_page):
        input_address = reg_page.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("katarinaGrinya@mailru")

        button_page_register = reg_page.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_page_register.click()

        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Сообщение введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    def test_must_be_password_field_correctness(self, reg_page):
        input_password = reg_page.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys('13579')
        input_password.click()

        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Длина пароля должна быть не менее 8 символов"

    def test_password_confirm_field_must_be_correctness(self, reg_page):
        input_password_confirm = reg_page.find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.send_keys('123456789')
        input_password_confirm.click()
        result = reg_page.find_element(RegistrationPageLocators.ERROR_MESSAGE_RP_CN).text
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"