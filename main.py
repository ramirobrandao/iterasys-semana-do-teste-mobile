from appium import webdriver
import pytest

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v7.8 (271241277)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

# Acionador do script
if __name__ == '__main__':

  #  def testar_somar_dois_numeros():
        # Conexão com o Sauce Labs, aponta o datacenter, meu usuário e chave
        driver = webdriver.Remote("Link do driver aqui", caps)

        result_expected = '13'

        # Realiza a conta de soma
        btn8 = driver.find_element_by_id("com.google.android.calculator:id/digit_8")
        btn8.click()
        btnsomar = driver.find_element_by_accessibility_id("plus")
        btnsomar.click()
        btn5 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
        btn5.click()
        btnigual = driver.find_element_by_accessibility_id("equals")
        btnigual.click()
        result_final = driver.find_element_by_id("com.google.android.calculator:id/result_final")
        print(f' resultado final = {result_final.text} \n resultado esperado = {result_expected}')

        assert result_final.text == result_expected

        driver.quit()