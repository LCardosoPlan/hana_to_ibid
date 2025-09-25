import io
import json
import constantes
import pandas as pd
from playwright.sync_api import sync_playwright, Page
from constantes import (
    SAP_URL, INPUT_EMAIL, INPUT_PASS, LOGON, LOGON_TITLE_PAGE, SAP_TITLE_PAGE, CHECKBOX_REMEMBERME,
    AUTH_JSON_PATH
)
from datetime_utils.datetime_utils import DateTimeUtils

class SapAutomation:
    """
    Gere toda a automação no SAP.
    Encapsula a execução de transações e a extração dos relatórios.
    """
    def __init__(self, sap_username, sap_password):
        self.sap_username = sap_username
        self.sap_password = sap_password
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False) # False mostra o navegador aberto executando os passos, True executa tudo em segundo plano
        self.context = self.browser.new_context()
        self.page = self.browser.new_page()
        self.date_utils = DateTimeUtils()
        
    def close(self):
        """
        Fecha o navegador e libera os recursos do Playwright.
        """
        print("Fechando o navegador.")
        self.browser.close()
        self.playwright.stop()
