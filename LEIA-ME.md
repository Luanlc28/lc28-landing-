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

## Identidade (Manual da Marca V11)

- Manual, briefing de marca, tokens e todos os arquivos oficiais ficam em `brand/` (V11: novo 8 e espaço ajustado entre C e 2).
- Cores (`brand/tokens.css`): Grafite #0F1F2E, Azul profundo #2E5D7A, Azul névoa #8FB3C9, Cinza claro #E6EEF4, Off-white #F8FAFC. Botões de ação em azul profundo com texto off-white; azul névoa como acento sobre grafite.
- Tipografia: Manrope 700 nos títulos, Inter no texto.
- Marca no topo: assinatura principal negativa a partir de 600 px de largura de tela (44 px de altura, acima do mínimo de 120 px de largura do manual) e monograma negativo em telas estreitas. Rodapé com a principal negativa; bloco de comparação com a principal positiva.
- Favicon: `favicon.ico` na raiz, `img/favicon.svg` e `img/apple-touch-icon.png` (do ícone de app V11). `img/og.jpg` usa a assinatura V11.
- Grafismos: `padrao-continuidade.svg` nas faixas escuras, `textura-pontos.svg` nas claras, sempre na lateral e em baixa opacidade.
- O infinito 3D da abertura usa Three.js r128 e GSAP 3.12.5 do cdnjs. Sem WebGL a página funciona sem o 3D.

## Blocos novos (recriados em HTML/CSS, sem React)

- **Soluções em carrossel** (`#solucoes`, base Gallery4): um card por tipo de negócio com a solução que a LC28 monta (substitui a antiga grade de seis frentes). Edite o array `SEGS` no script. Clicar abre o diagnóstico com a frente marcada.
- **LC28 x jeito comum** (`#diferencas`, base comparison-2): só compromissos que já estão na oferta (sem fidelidade, contas no nome do cliente, preço fechado etc.).
- **Chamada com lista** (`.cta4`, base cta-4): fecha a seção Investimento.
- **Celular dos modelos**: moldura com botões laterais e reflexo (base mobile mockup).
- **Nuvem de logos**: fora até existirem logos de clientes autorizados.
- Publique a pasta inteira (index.html + img/ + favicon.ico).
- Arquivo único: depois de mexer no `index.html`, rode `python gerar-arquivo-unico.py`.

## Captação de leads (atualização)

- **Diagnóstico grátis**: é o antigo briefing, com o mesmo fluxo e a mesma lógica. Virou o CTA principal da página.
- **Demos por nicho** (`#demos`): barbearia, delivery e distribuidora, desenhadas em HTML. "Quero um assim" abre o diagnóstico com a frente marcada.
- **Investimento** (`#investimento`): preencha `MENSALIDADE_TRAFEGO` (ex.: "R$ 1.500"). Vazio mostra "Sob consulta". Confirme se "sem fidelidade" vale para a LC28.
