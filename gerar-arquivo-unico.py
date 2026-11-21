# Gera LC28-landing-completa.html: o index.html com as imagens de img/ embutidas (um arquivo só).
# Uso: python gerar-arquivo-unico.py
import base64, re, pathlib

raiz = pathlib.Path(__file__).parent
html = (raiz / "index.html").read_text(encoding="utf-8")
tipos = {".webp": "image/webp", ".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg"}

def embutir(m):
    arq = raiz / m.group(0)
    assert arq.exists(), f"imagem não encontrada: {arq}"
    return f"data:{tipos[arq.suffix]};base64," + base64.b64encode(arq.read_bytes()).decode()

# (?<!/) pula URLs completas, como a og:image (https://lc28.com.br/img/og.jpg), que precisam continuar como link.
REF = r"(?<!/)img/[\w.-]+\.(?:webp|png|svg|jpg)"
saida, n = re.subn(REF, embutir, html)
assert not re.search(REF, saida), "sobrou referência a img/"
(raiz / "LC28-landing-completa.html").write_text(saida, encoding="utf-8")
print(f"{n} imagens embutidas, {len(saida) / 1e6:.1f} MB")
