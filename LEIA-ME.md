# LC28 · Landing page e briefing

Arquivo único (`index.html`), sem dependências além das fontes do Google. Pode ser publicado em qualquer hospedagem estática (Vercel, Netlify, Hostinger, GitHub Pages).

## O que falta definir (bloco CONFIGURAÇÃO no topo do `<script>`)

| Pendência | Onde mexer |
|---|---|
| Número comercial do WhatsApp | `WHATSAPP_NUMBER`, só dígitos com DDI e DDD (ex.: `5511999998888`). Vazio = abre o WhatsApp sem destinatário e mostra aviso. |
| Salvar o briefing antes do WhatsApp | `onBriefingSubmit(payload)`. É chamado no clique, antes de abrir o WhatsApp. Use `navigator.sendBeacon` ou `fetch(..., {keepalive:true})` para não travar o redirecionamento. |
| Domínio | Na tag `og:image` do `<head>`, troque `img/og.jpg` pela URL completa (ex.: `https://seudominio.com.br/img/og.jpg`). Sem isso a prévia do link no WhatsApp sai sem imagem. |
| Cases autorizados | Array `CASES`: título, `image` (URL do print), objetivo, período, investimento, métrica e o que foi feito. Enquanto todos tiverem `ilustrativo: true`, a seção Resultados e os links do menu ficam escondidos. |

## Como o briefing decide as perguntas

- Perguntas por serviço ficam em `serviceQuestions()`. `core` são as iniciais e `comp` as complementares.
- Um serviço: aparecem todas. Vários serviços: as duas primeiras de cada frente e só as complementares com dependência (`dep`), por exemplo destino do anúncio só quando não há site ou landing page.
- Respostas comuns são reaproveitadas: região da empresa não é perguntada de novo no tráfego, a oferta do tráfego vale para a landing page, e "quantas pessoas vão usar" só aparece para app, sistema ou automação.
- "Preciso de ajuda para escolher" pula as perguntas de serviço e vai para contato e revisão.
- O rascunho fica salvo no navegador da pessoa (localStorage) até ela recomeçar.

## Identidade (kit oficial v9.2)

- Cores dos tokens oficiais (`tokens.css`): Grafite #0F1F2E, Azul profundo #2E5D7A, Azul névoa #8FB3C9, Cinza claro #E6EEF4, Off-white #F8FAFC. Botões de ação em azul profundo com texto off-white; azul névoa como acento sobre grafite.
- Tipografia conforme o Guia de Tipografia: Manrope 700 nos títulos, Inter no texto.
- Logos em SVG na pasta `img/`: `logo-principal-negativa.svg` (topo), `logo-horizontal-negativa.svg` (rodapé), `logo-monograma-branca.svg` (marca d'água do rodapé) e `favicon.svg`/`favicon.png`.
- Ícones da marca (diagnóstico, estratégia, tecnologia, resultados, evolução, automação) nas frentes de Soluções e nos passos de Como funciona. Aplicativo e Sistema usam ícones desenhados no mesmo traço.
- Grafismos: `padrao-continuidade.svg` nas faixas escuras e na abertura, `textura-pontos.svg` nas faixas claras, sempre na lateral e em baixa opacidade.
- O infinito 3D da abertura usa Three.js r128 e GSAP 3.12.5 (ScrollTrigger) do cdnjs. Sem internet ou WebGL a página funciona sem o 3D; com "reduzir movimento" ele fica parado.
- Publique a pasta inteira (index.html + img/).
- Arquivo único: depois de mexer no `index.html`, rode `python gerar-arquivo-unico.py` para atualizar o `LC28-landing-completa.html` (imagens embutidas, abre sem a pasta img/).

## Captação de leads (atualização)

- **Diagnóstico grátis**: é o antigo briefing, com o mesmo fluxo e a mesma lógica. Virou o CTA principal da página.
- **Demos por nicho** (`#demos`): barbearia, delivery e distribuidora, desenhadas em HTML. "Quero um assim" abre o diagnóstico com a frente marcada.
- **Investimento** (`#investimento`): preencha `MENSALIDADE_TRAFEGO` (ex.: "R$ 1.500"). Vazio mostra "Sob consulta". Confirme se "sem fidelidade" vale para a LC28.
