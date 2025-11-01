import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    """
    Función básica para extraer precios
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # BUSCAR PRECIO - intenta diferentes patrones
        price_selectors = [
            {'class': 'a-price-whole'},  # Amazon
            {'class': 'price'},           # General
            {'class': 'precio'},          # Español
            {'itemprop': 'price'},        # Schema.org
        ]
        
        for selector in price_selectors:
            price_element = soup.find('span', selector)
            if price_element:
                price_text = price_element.text.strip()
                # Limpiar el precio (quitar símbolos, espacios)
                price_clean = ''.join(c for c in price_text if c.isdigit() or c == '.')
                if price_clean:
                    return float(price_clean)
        
        return None
        
    except Exception as e:
        print(f"Error extrayendo precio: {e}")
        return None

def get_product_name(url):
    """
    Función básica para extraer nombres
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # BUSCAR NOMBRE - intenta diferentes patrones
        name_selectors = [
            {'id': 'productTitle'},       # Amazon
            {'class': 'product-title'},   # General
            {'class': 'nombre-producto'}, # Español
            {'itemprop': 'name'},         # Schema.org
            'h1',                         # Cualquier h1
        ]
        
        for selector in name_selectors:
            if isinstance(selector, str):
                name_element = soup.find(selector)
            else:
                name_element = soup.find('span', selector)
            
            if name_element and name_element.text.strip():
                return name_element.text.strip()[:100]  # Limitar longitud
        
        return "Producto sin nombre"
        
    except Exception as e:
        print(f"Error extrayendo nombre: {e}")
        return "Producto desconocido"
