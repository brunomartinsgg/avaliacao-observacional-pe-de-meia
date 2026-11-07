import time
from playwright.sync_api import sync_playwright

URL = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Carregando {URL}...", flush=True)
        page.goto(URL, wait_until="domcontentloaded", timeout=30000)
        time.sleep(3)

        # Clicar em todas as abas e botões para expandir anos
        buttons = page.query_selector_all("button, a, div[role='button']")
        for btn in buttons:
            try:
                txt = btn.text_content().strip()
                if any(yr in txt for yr in ["2022", "2023", "2024", "2025", "2021", "2020"]):
                    btn.click()
                    time.sleep(0.5)
            except:
                pass

        links = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a[href]')).map(a => a.href);
        }""")

        inep_links = [l for l in links if "download.inep.gov.br" in l]
        print(f"\nEncontrados {len(inep_links)} links para download.inep.gov.br:")
        for l in sorted(list(set(inep_links))):
            print(l, flush=True)

        browser.close()

if __name__ == "__main__":
    main()
