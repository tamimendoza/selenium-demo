import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def get_element(navegador, referencia, tipo):
    return WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((tipo, referencia))
    )

def main():
    navegador = webdriver.Firefox()
    navegador.set_window_size(1920, 1080)

    try:
        navegador.get("https://www.selenium.dev/selenium/web/web-form.html")

        txt_input = get_element(navegador, "my-text-id", By.ID)
        txt_input.send_keys("Texto de prueba input")

        txt_password = get_element(navegador, "my-password", By.NAME)
        txt_password.send_keys("123456")

        txt_area = get_element(navegador, "my-textarea", By.NAME)
        txt_area.send_keys("Texto de prueba area")

        cb_select = Select(get_element(navegador, "my-select", By.NAME))
        cb_select.select_by_value("2")

        txt_datalist = get_element(navegador, "my-datalist", By.NAME)
        txt_datalist.send_keys("New")
        time.sleep(1)
        txt_datalist.send_keys(Keys.ARROW_DOWN)
        txt_datalist.send_keys(Keys.ENTER)

        txt_file = get_element(navegador, "my-file", By.NAME)
        txt_file.send_keys("/home/tmendoza/Escritorio/selenium-demo/demotxt")

        txt_checkbox = get_element(navegador, "my-check-1", By.ID)
        txt_checkbox.click()

        txt_color = get_element(navegador, "my-colors", By.NAME)
        new_color = "#FF0000"
        navegador.execute_script("arguments[0].value = arguments[1];", txt_color, new_color)

        # 06/06/2023
        txt_date = get_element(navegador, "my-date", By.NAME)
        txt_date.send_keys("06/06/2023" + Keys.TAB)

        txt_rango = get_element(navegador, "/html/body/main/div/form/div/div[3]/label[3]/input", By.XPATH)
        navegador.execute_script("arguments[0].value = arguments[1];", txt_rango, "1")

        navegador.save_screenshot("screenshot.png")

        btn_submit = get_element(navegador, "/html/body/main/div/form/div/div[2]/button", By.XPATH)
        btn_submit.click()

        parrafo = get_element(navegador, "message", By.ID)
        parrafo_text = parrafo.text

        if parrafo_text == "Received!":
            print("Test OK")

        time.sleep(5)
    except Exception as e:
        print("Error: ", e)
    
    if navegador:
        navegador.close()
        navegador.quit()

if __name__ == "__main__":
    main()