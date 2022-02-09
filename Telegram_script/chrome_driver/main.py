import time
from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import list_groups

# user_agent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless = True
# options.add_argument('--disable-gpu')
print('Starting ...')
driver = webdriver.Chrome(options=options)
driver.set_window_size(1440, 900)

url = 'https://web.telegram.org/z/'
print('Loading page ...')
def xpath_exists(xpath):
    try:
        driver.find_element(By.CSS_SELECTOR, xpath)
        exist = True
    except Exception as ex:
        exist = False
    return exist


# def main():

try:
    driver.get(url)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'button.Button.default.primary.text').click()
    time.sleep(6)
    input_number = driver.find_element(By.CSS_SELECTOR, 'input#sign-in-phone-number.form-control')
    input_number.clear()
    tg_phone = input("Write your full number: ")
    time.sleep(1)
    input_number.send_keys(tg_phone)
    input_number.send_keys(Keys.ENTER)
    code = input('Check your phone and send your key: ')
    time.sleep(1)
    input_code = driver.find_element(By.CSS_SELECTOR, 'input#sign-in-code.form-control')
    input_code.send_keys(code)
    input_code.send_keys(Keys.ENTER)
    time.sleep(9)

    #joined groups
    count = 0
    timer = 0

    print('GO')
    for group in list_groups:
        if timer == 5:
            time.sleep(320)
            timer = 0
        else:
            search = driver.find_element(By.CSS_SELECTOR, 'input#telegram-search-input.form-control')
            search.clear()
            time.sleep(2)
            search.send_keys(group)
            time.sleep(3)
            search.send_keys(Keys.ENTER)
            time.sleep(4)


            try:
                if xpath_exists('button.Button.default.primary.text'):
                    driver.find_element(By.CSS_SELECTOR, 'button.Button.default.primary.text').click()
                    time.sleep(5)

                driver.find_element(By.CSS_SELECTOR, 'button.Button.tiny.primary.fluid.has-ripple').click()
                count += 1
                timer += 1
                print(f'Nice {count} --> {group}')
                time.sleep(3)

            except Exception as exc:
                print(f'######### Private #########-->{group}')
                search.clear()
                time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# if __name__=='__main__':
#     main()