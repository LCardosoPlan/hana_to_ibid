import io
from playwright.sync_api import sync_playwright, Page
from datetime_utils.datetime_utils import DateTimeUtils
from f_constantes.constantes import (
    OKTA_URL, INPUT_EMAIL, INPUT_PASS, LOGON, LOGON_TITLE_PAGE, SAP_TITLE_PAGE, CHECKBOX_REMEMBERME,
    AUTH_JSON_PATH
)

class login_okta:
    """
    Encapsula o login no Okta e salva seu estado de login em ./state_context/auth.json
    """
    def __init__(self, plan_email, plan_senha):
        self.plan_email = plan_email
        self.plan_senha = plan_senha
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False) # False mostra o navegador aberto executando os passos, True executa tudo em segundo plano
        self.context = self.browser.new_context()
        self.page = self.browser.new_page()
        self.date_utils = DateTimeUtils()

    def login(self):
        """
        Executa o processo de login no SAP.
        """
        self.page.set_default_timeout(60000)
        print("Logando no SAP...")
        print(self.page)
        self.page.goto(SAP_URL)
        self.page.fill(f"id={INPUT_EMAIL}", self.plan_email)
        self.page.fill(f"id={INPUT_PASS}", self.plan_senha)
        self.page.get_by_text("Mantenha-me conectado").click()
        self.page.get_by_role(LOGON).click()
        #print(self.page)
        titulo_pagina = self.page.title()
        if titulo_pagina == LOGON_TITLE_PAGE:
            self.page.get_by_role("link", name="Selecione para receber uma").click()
        
        print(self.context.storage_state())
        storage = self.context.storage_state(path=AUTH_JSON_PATH)
        print("Login realizado com sucesso.")