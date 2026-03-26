import asyncio
from playwright.async_api import async_playwright
import pandas as pd
from datetime import datetime

async def coletar_precos():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # Exemplo GBarbosa Aracaju
        itens = ["arroz", "feijao", "leite", "cafe", "oleo"]
        resultados = []
        
        for item in itens:
            url = f"https://www.gbarbosa.com.br/{item}?_q={item}&map=ft"
            try:
                await page.goto(url, wait_until="networkidle", timeout=60000)
                # Seletores reais da plataforma VTEX (GBarbosa)
                nomes = await page.locator(".vtex-product-summary-2-x-brandName").all_inner_texts()
                precos = await page.locator(".vtex-product-price-1-x-currencyInteger").all_inner_texts()
                
                for n, p_val in zip(nomes[:5], precos[:5]):
                    resultados.append({
                        "loja": "GBarbosa",
                        "produto": n,
                        "preco": float(p_val.replace(".", "").replace(",", ".")),
                        "data": datetime.now().strftime("%d/%m/%Y")
                    })
            except:
                continue
        
        await browser.close()
        pd.DataFrame(resultados).to_csv("dados_precos.csv", index=False)

if __name__ == "__main__":
    asyncio.run(coletar_precos())
