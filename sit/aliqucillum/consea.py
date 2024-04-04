def remove_metamask(driver):
    """
    Remove the MetaMask extension from the browser.

    Args:
        driver: The Selenium WebDriver instance.
    """

    # Navigate to the extensions page.
    driver.get("chrome://extensions/")

    # Find the MetaMask extension.
    extension = driver.find_element_by_xpath("//div[@id='extensions-container']//div[contains(@class, 'extension-card') and contains(@id, 'extension-id-')]")

    # Click the "Remove" button.
    extension.find_element_by_xpath(".//button[contains(@class, 'delete-button')]").click()

    # Confirm the removal.
    driver.find_element_by_xpath("//button[contains(@class, 'confirm-button')]").click()

    # Wait for the extension to be removed.
    time.sleep(5)
