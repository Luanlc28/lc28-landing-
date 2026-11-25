# Integração LC28

Importe o CSS no início da folha de estilos e use as variáveis prefixadas por `--lc28-`.
O JSON usa cores base em HEX, referências semânticas e dimensões numéricas em pixels.
`icons/` usa `currentColor`. Para herdar a cor do texto, insira o SVG inline.

```css
@import url("./tokens.css");
.acao {
  background: var(--lc28-action);
  color: var(--lc28-onAction);
  font: 600 1rem var(--lc28-font-body);
  border-radius: var(--lc28-radius-small);
  padding: var(--lc28-space-sm) var(--lc28-space-md);
}
```

Use marca positiva sobre fundos claros e negativa sobre grafite. Use o monograma nos espaços compactos.
No HTML, adicione texto alternativo à marca informativa e use `alt=""` em grafismos decorativos.
Copie o favicon para a distribuição e use `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`.
As pilhas tipográficas possuem fallback local. Instale ou sirva Manrope e Inter no ambiente final.
