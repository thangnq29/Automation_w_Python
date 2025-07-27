import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(getattr(item, "cls", None), "driver", None)
        print(f"[DEBUG] driver: {driver}")
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"[Allure] Failed to attach screenshot: {e}")
        else:
            print("[DEBUG] No driver found to take screenshot")