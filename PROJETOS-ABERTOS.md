# Projetos abertos da LOFRANO TECNOLOGIA

[← Voltar ao perfil](README.md) · [Conheça a LOFRANO TECNOLOGIA](https://lofranotecnologia.com.br)

Código, ferramentas e exemplos públicos. Consulte o README de cada repositório para conhecer sua finalidade, instalação e licença.

[Commits e evidências técnicas dos novos projetos](EVIDENCIAS.md).

<!-- PUBLIC-PROJECTS:BEGIN -->
## Repositórios públicos · atualização automática

**254 repositórios públicos próprios**, incluindo forks e arquivados quando existirem. Metadados consultados no GitHub em **09/11/2026 às 10:08 UTC**.

Os oito repositórios criados mais recentemente, com o último commit da branch padrão. As coleções abaixo têm curadoria manual; as validações técnicas estão em [EVIDENCIAS.md](EVIDENCIAS.md).

[Inventário público completo em JSON](evidencias/public-projects.json).

| Projeto | Descrição pública | Último commit da branch padrão (UTC) |
| --- | --- | --- |
| [zonas\-geojson](https://github.com/martinlofranodeoliveira/zonas-geojson) | Cruze pontos com áreas GeoJSON: furos, ilhas, fronteiras e sobreposições com predicados exatos\. CLI/API Python local, português e MIT — LOFRANO TECNOLOGIA\. | [09/11/2026 09:34 · 0c3196e](https://github.com/martinlofranodeoliveira/zonas-geojson/commit/0c3196e2771954dff2e6b56233933ed67649b1d6) |
| [rateio\-claro](https://github.com/martinlofranodeoliveira/rateio-claro) | Divida despesas por pesos, confira cada centavo e registre acertos\. Aplicativo local em português, HTML/CSS/JavaScript, MIT — LOFRANO TECNOLOGIA\. | [09/11/2026 08:32 · 8ac126b](https://github.com/martinlofranodeoliveira/rateio-claro/commit/8ac126b4ec37b33cbd9209a8422e1cc799d4b837) |
| [materiais\-em\-lote](https://github.com/martinlofranodeoliveira/materiais-em-lote) | Planejamento de materiais por listas técnicas multinível: estoque, lotes, embalagens e memória de cálculo exata\. CLI/API Python, português e MIT\. | [09/11/2026 07:11 · e991b21](https://github.com/martinlofranodeoliveira/materiais-em-lote/commit/e991b213e634f8eff35d8617abd1c7204728a09c) |
| [cruzadas\-de\-papel](https://github.com/martinlofranodeoliveira/cruzadas-de-papel) | Construtor de palavras cruzadas em português: grade interativa, pistas, atividade e gabarito em SVG/IPUZ\. Local, sem conta, código MIT\. | [09/11/2026 06:16 · 2029364](https://github.com/martinlofranodeoliveira/cruzadas-de-papel/commit/202936452e03d11cb6704fb329691d4d784fa892) |
| [portaria\-local](https://github.com/martinlofranodeoliveira/portaria-local) | Recepção e controle local de presença por busca, código e QR, com correções no histórico, arquivos portáteis e interface em português\. MIT\. | [09/11/2026 04:53 · b34cf4c](https://github.com/martinlofranodeoliveira/portaria-local/commit/b34cf4c2e21a78ad4b5b2baae1f90bd0b025b79d) |
| [mapa\-de\-mesas](https://github.com/martinlofranodeoliveira/mapa-de-mesas) | Organize convidados e grupos por mesas: capacidades, atribuições manuais, backup JSON, CSV e listas para impressão\. Local, português e MIT\. | [09/11/2026 04:04 · db3b68f](https://github.com/martinlofranodeoliveira/mapa-de-mesas/commit/db3b68f968083f2b59f6724e0d7dec6b5769b63a) |
| [biblioteca\-de\-emprestimos](https://github.com/martinlofranodeoliveira/biblioteca-de-emprestimos) | Controle local de empréstimos de livros e ferramentas, devoluções parciais e atrasos\. Python sem dependências\. | [09/11/2026 03:38 · 1c60541](https://github.com/martinlofranodeoliveira/biblioteca-de-emprestimos/commit/1c605412a2e63d321415a7c4aecf4e834ad9ad94) |
| [mapa\-midi](https://github.com/martinlofranodeoliveira/mapa-midi) | Inspeção local de arquivos MIDI: tempo racional exato, intervalos de notas, diagnósticos e rolo de piano SVG/PNG\. Python, MIT e documentação em português\. | [09/11/2026 03:13 · 71b832f](https://github.com/martinlofranodeoliveira/mapa-midi/commit/71b832f0eafab4c6d9645dfa6401584ca0519672) |

<!-- PUBLIC-PROJECTS:END -->

<!-- DELIVERY-ZONAS-2026-11-09:BEGIN -->
## Zonas GeoJSON · pontos, áreas e fronteiras

Cruze pontos já geocodificados com áreas de atendimento. A junção distingue interior, fronteira, exterior e sobreposição, respeita furos e ilhas e conserva todas as correspondências, sem escolher uma zona vencedora silenciosamente.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Zonas GeoJSON](https://github.com/martinlofranodeoliveira/zonas-geojson) · CLI/API Python · MIT · português · LOFRANO TECNOLOGIA | [Baixar exemplo completo](https://github.com/martinlofranodeoliveira/zonas-geojson/releases/download/v1.0.0/exemplo-zonas.zip) · [Ver figura](https://github.com/martinlofranodeoliveira/zonas-geojson/blob/0c3196e2771954dff2e6b56233933ed67649b1d6/docs/exemplo.png) | [v1.0.0](https://github.com/martinlofranodeoliveira/zonas-geojson/releases/tag/v1.0.0) · 65 testes locais · [CI Linux/Windows e GIS](https://github.com/martinlofranodeoliveira/zonas-geojson/actions/runs/42594417559) |

Até 10.000 pontos, 100 zonas e 5.000 posições de polígonos, com orçamento lógico explícito. A análise usa racionais exatos sobre os decimais fornecidos; o ZIP reúne fontes originais, JSON, CSV, GeoJSON anotado, SVG, orientação e manifesto. O exemplo tem treze pontos e quatro zonas fictícias. Execução local sem dependências externas de runtime; o recorte é cartesiano em graus, sem geocodificação, áreas geodésicas ou certificação territorial.

<!-- DELIVERY-ZONAS-2026-11-09:END -->

<!-- DELIVERY-RATEIO-2026-11-09:BEGIN -->
## Rateio Claro · cada centavo tem destino

Divida despesas de um grupo por pesos, confira o arredondamento de cada parcela e registre os acertos declarados. O recibo explica os centavos adicionais; as sugestões permanecem separadas até a confirmação explícita de um acerto.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/rateio-claro/) | [Rateio Claro](https://github.com/martinlofranodeoliveira/rateio-claro) · HTML/CSS/JavaScript · MIT · português · LOFRANO TECNOLOGIA | [v1.0.0](https://github.com/martinlofranodeoliveira/rateio-claro/releases/tag/v1.0.0) · 48 testes Node + 23 Python · [CI com LibreOffice](https://github.com/martinlofranodeoliveira/rateio-claro/actions/runs/42586661350) |

Até 100 pessoas, 500 despesas e 500 acertos; projeto JSON UTF-8 de até 2 MiB. O núcleo usa centavos inteiros e BigInt; desempates seguem o ID em cada despesa. Acertos não aumentam o custo e podem inverter saldos. JSON guarda o estado aplicado; memória JSON, CSV e Markdown permitem conferir a conta. Sugestões determinísticas não prometem o menor número de transferências. Sem conta, banco ou autosave: guarde o JSON para continuar depois.

<!-- DELIVERY-RATEIO-2026-11-09:END -->

<!-- DELIVERY-MATERIAIS-2026-11-09:BEGIN -->
## Materiais em Lote · do pedido aos componentes

Calcule necessidades de fabricação e compra por listas técnicas multinível. Demandas de pais diferentes são reunidas antes de usar o estoque uma vez; apenas os lotes fabricados consomem componentes. Embalagens e lotes explicam as sobras, com quantidades racionais exatas e memória de cada origem.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Materiais em Lote](https://github.com/martinlofranodeoliveira/materiais-em-lote) · CLI/API Python · MIT · português · LOFRANO TECNOLOGIA | [Baixar exemplo completo](https://github.com/martinlofranodeoliveira/materiais-em-lote/releases/download/v1.0.0/exemplo.zip) | [v1.0.0](https://github.com/martinlofranodeoliveira/materiais-em-lote/releases/tag/v1.0.0) · 59 testes locais · [CI Linux/Windows e LibreOffice](https://github.com/martinlofranodeoliveira/materiais-em-lote/actions/runs/42577747832) |

Até 250 itens, 2.000 relações e 250 demandas; JSON UTF-8 de até 1 MiB. O ZIP reúne entrada, plano JSON/CSV/Markdown/XLSX, orientação e manifesto SHA-256. XLSX é relatório estático; JSON conserva o cenário para recalcular. O LibreOffice importou 414 células corretamente, mas alterou dois padrões literais ao regravar XLSX: essa limitação está documentada. Não há conversão de unidades, preços, calendário, reserva de estoque ou compra real.

<!-- DELIVERY-MATERIAIS-2026-11-09:END -->

<!-- DELIVERY-CRUZADAS-2026-11-09:BEGIN -->
## Cruzadas de Papel · palavras, pistas e cruzamentos

Monte palavras cruzadas autorais no navegador, confira as letras compartilhadas e prepare atividade e gabarito. A edição mostra a resposta original e sua preparação em A–Z; a numeração acompanha as posições, inclusive quando duas palavras começam na mesma célula.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/cruzadas-de-papel/) | [Cruzadas de Papel](https://github.com/martinlofranodeoliveira/cruzadas-de-papel) · HTML/CSS/JavaScript · MIT · português · LOFRANO TECNOLOGIA | [v1.0.0](https://github.com/martinlofranodeoliveira/cruzadas-de-papel/releases/tag/v1.0.0) · 25 testes Node + 18 Python · [CI Node 22/24](https://github.com/martinlofranodeoliveira/cruzadas-de-papel/actions/runs/42572011827) |

Até 40 entradas em grade de 5 a 21 células por eixo. JSON guarda a edição, inclusive rascunhos; SVG e IPUZ separam atividade e gabarito. As saídas finais exigem palavras posicionadas e conectadas, pistas e ausência de sequências acidentais. Os dois IPUZ realmente baixados foram abertos no player oficial Exolve: atividade digitável sem controles de solução e gabarito com nove respostas e 28 células conferidas. Sem conta, autosave, banco de palavras ou IA; guarde o JSON antes de fechar a aba.

<!-- DELIVERY-CRUZADAS-2026-11-09:END -->

<!-- DELIVERY-PORTARIA-2026-11-09:BEGIN -->
## Portaria Local · localizar, conferir e confirmar

Receba participantes de um pequeno encontro por busca, código copiável ou imagem QR. Confira o cadastro antes de confirmar a entrada; uma repetição conserva a presença e seu horário. Correções exigem motivo e acrescentam uma anulação ao histórico, mantendo a entrada original.

| Código e documentação | Demonstração e versão | Validação |
| --- | --- | --- |
| [Portaria Local](https://github.com/martinlofranodeoliveira/portaria-local) · HTML/CSS/JavaScript · MIT · português · LOFRANO TECNOLOGIA | [Abrir demonstração](https://martinlofranodeoliveira.github.io/portaria-local/) · [Versão 1.0.0](https://github.com/martinlofranodeoliveira/portaria-local/releases/tag/v1.0.0) | 52 testes Node + 7 Python; CI Node 22/24, interoperabilidade e Pages concluídos. |

Até 300 participantes e 5.000 registros de histórico, com arquivos JSON/CSV de entrada UTF-8 de até 2 MiB. IDs preservam homônimos; JSON guarda o projeto completo e CSV apresenta presenças e histórico. O código/QR é um localizador copiável, sem autenticação ou prova de identidade. Horários vêm do relógio do dispositivo. Sem conta ou autosave: guarde o JSON antes de fechar a aba. A demonstração usa oito pessoas fictícias, duas presentes e seis ausentes, com três entradas e uma anulação.

<!-- DELIVERY-PORTARIA-2026-11-09:END -->

<!-- DELIVERY-SEATING-2026-11-09:BEGIN -->
## Mapa de Mesas · cada convidado, um lugar

Organize pessoas e grupos por mesas, confira as vagas e prepare listas por mesa e em ordem alfabética. Uma distribuição manual com capacidade validada, IDs que preservam homônimos e movimento de grupo completo ou recusado integralmente.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/mapa-de-mesas/) | [Mapa de Mesas](https://github.com/martinlofranodeoliveira/mapa-de-mesas/tree/db3b68f968083f2b59f6724e0d7dec6b5769b63a) · HTML/CSS/JavaScript · MIT · português | [v1.0.0](https://github.com/martinlofranodeoliveira/mapa-de-mesas/releases/tag/v1.0.0) · 46 testes Node + 9 Python · [CI](https://github.com/martinlofranodeoliveira/mapa-de-mesas/actions/runs/42559744917) |

Até 300 convidados e 50 mesas, sem conta ou salvamento implícito. JSON guarda o encontro completo; CSV ajuda a importar convidados e consultar a distribuição; HTML prepara as listas para impressão. Backup reaberto no Chrome preservou os bytes, e os downloads reais foram conferidos por um leitor Python independente. Não há solver, planta em escala ou geração própria de PDF; PDF não foi validado nesta entrega. Guarde o JSON para continuar depois.

<!-- DELIVERY-SEATING-2026-11-09:END -->

<!-- DELIVERY-MIDI-2026-11-09:BEGIN -->
## Mapa MIDI · notas, eventos e andamento

Inspecione arquivos MIDI sem sintetizador ou dispositivos. A biblioteca e CLI Python mostram intervalos entre mensagens de nota, mudanças de andamento e diagnósticos; exportam JSON, CSV, Markdown e rolo de piano SVG/PNG com proveniência por trilha e evento.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Mapa MIDI](https://github.com/martinlofranodeoliveira/mapa-midi/tree/71b832f0eafab4c6d9645dfa6401584ca0519672) · Python · MIT · README em português | [MIDI original e relatórios](https://github.com/martinlofranodeoliveira/mapa-midi/releases/download/v1.0.0/exemplo-mapa-midi.zip) · [Ver rolo de piano](https://github.com/martinlofranodeoliveira/mapa-midi/blob/71b832f0eafab4c6d9645dfa6401584ca0519672/examples/rolo.png) | [v1.0.0](https://github.com/martinlofranodeoliveira/mapa-midi/releases/tag/v1.0.0) · suíte de 75 testes · [CI Linux/Windows e MIDICSV](https://github.com/martinlofranodeoliveira/mapa-midi/actions/runs/42555236493) |

Requer Python 3.11+, Mido e Matplotlib. Usa segundos racionais exatos e pareamento FIFO por trilha, porta, canal e nota. Cinco exemplos sintéticos passaram pelo consumidor C MIDICSV 1.1: 90 eventos e 22 intervalos conferidos com oráculos manuais. Pedal é registrado, sem inferir duração audível; sobreposições ficam marcadas como ambíguas e notas abertas não recebem fim inventado. O escopo aceita SMF tipos 0/1 com PPQN e está documentado no contrato.

<!-- DELIVERY-MIDI-2026-11-09:END -->

<!-- DELIVERY-XLSX-2026-11-08:BEGIN -->
## Conferência XLSX · veja o que mudou na planilha

Biblioteca e CLI Python que comparam duas entregas de uma planilha por aba e coordenada. Distinguem valores tipados, números decimais exatos, texto das fórmulas e resultados armazenados; identificam também mudanças de abas e mesclagens, sem modificar as entradas.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Conferência XLSX](https://github.com/martinlofranodeoliveira/conferencia-xlsx/tree/e8160aec8093072cbdba56e62c9ca35777b0b4d5) · Python · MIT · README em português | [Baixar exemplo completo](https://github.com/martinlofranodeoliveira/conferencia-xlsx/releases/download/v1.0.0/exemplo-conferencia.zip) · [Reproduzir ensaio](https://github.com/martinlofranodeoliveira/conferencia-xlsx/blob/e8160aec8093072cbdba56e62c9ca35777b0b4d5/docs/INTEROPERABILIDADE.md) | [v1.0.0](https://github.com/martinlofranodeoliveira/conferencia-xlsx/releases/tag/v1.0.0) · 64 testes · [CI Linux/Windows e LibreOffice](https://github.com/martinlofranodeoliveira/conferencia-xlsx/actions/runs/42551395253) |

Requer Python 3.11+, openpyxl e defusedxml. Produz JSON, Markdown, CSV e ZIP com manifesto SHA-256; o pacote comum contém relatórios, e o comando de exemplo acrescenta duas entradas sintéticas. O LibreOffice real produziu os XLSX usados em onze mudanças conhecidas, além de uma fixture derivada com uma mudança de cache ausente. Outro ensaio confrontou 14 casos de texto em 28 células. A ferramenta não calcula fórmulas: a atualidade dos resultados armazenados permanece desconhecida. Aparência e igualdade integral da pasta de trabalho ficam fora do escopo.

<!-- DELIVERY-XLSX-2026-11-08:END -->

<!-- DELIVERY-ACERVO-2026-11-08:BEGIN -->
## Acervo de Leitura · referências e tempo para ler

Importe referências CSL JSON, organize a fila por prioridade e distribua as estimativas restantes pela capacidade de cada dia da semana. O plano identifica pendências e alocações depois do prazo; o histórico registra sessões sem alterar automaticamente as estimativas ou a conclusão.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/acervo-de-leitura/) | [Acervo de Leitura](https://github.com/martinlofranodeoliveira/acervo-de-leitura) · HTML/CSS/JavaScript · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/acervo-de-leitura/releases/tag/v1.0.0) · 48 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/acervo-de-leitura/actions/runs/42546938219) |

Funciona no navegador com até 500 referências, backup JSON, metadados CSL e relatórios CSV/Markdown. Os dados permanecem locais; guarde o projeto JSON antes de fechar a aba. Três referências fictícias percorreram o Zotero Translation Server oficial: o Acervo preservou o CSL recebido, e a reimportação oficial regenerou somente os IDs nessa amostra. O backup do aplicativo inclui o planejamento e não abrange anexos ou coleções do Zotero.

<!-- DELIVERY-ACERVO-2026-11-08:END -->

<!-- DELIVERY-QUESTIONS-2026-11-08:BEGIN -->
## Banco de Questões · do banco versionado à revisão

Biblioteca e CLI Python que validam um banco JSON de esquema fechado e compilam Moodle XML com imagens e gabaritos. Representam escolha simples, escolha múltipla, verdadeiro/falso, resposta curta e numérica; produzem cadernos HTML docente/aluno, relatórios sem repetir enunciados ou respostas e ZIP com manifesto SHA256.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Banco de Questões](https://github.com/martinlofranodeoliveira/banco-de-questoes) · Python · MIT · README em português | [Banco e cadernos fictícios para download](https://github.com/martinlofranodeoliveira/banco-de-questoes/releases/tag/v1.0.0) | [v1.0.0](https://github.com/martinlofranodeoliveira/banco-de-questoes/releases/tag/v1.0.0) · 61 testes · [CI Linux/Windows e Moodle](https://github.com/martinlofranodeoliveira/banco-de-questoes/actions/runs/42542138739) |

Requer Python 3.11+ e Pillow 13.0.0; funciona offline após a instalação, sem conexão ao LMS. A importação e a correção reais foram exercitadas no Moodle 4.5.15+ fixado, com oito questões, 30 respostas corrigidas, reimportação da exportação com a imagem PNG preservada e conferência de 41 percentuais. O alcance cobre os casos documentados nessa versão. O XML e o caderno docente contêm gabaritos por finalidade; os arquivos devem ser revisados antes da distribuição.

<!-- DELIVERY-QUESTIONS-2026-11-08:END -->

<!-- DELIVERY-VIDEO-2026-11-08:BEGIN -->
## Roteiro de Vídeo · da narrativa à gravação

Planeje cenas com texto, referências visuais e duração. A narrativa mantém seus números enquanto a ordem de gravação reúne cenas por local e setup. Durações usam milissegundos inteiros; cenas sem duração continuam identificadas como pendentes.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/roteiro-de-video/) | [Roteiro de Vídeo](https://github.com/martinlofranodeoliveira/roteiro-de-video) · HTML/CSS/JavaScript · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/roteiro-de-video/releases/tag/v1.0.0) · 56 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/roteiro-de-video/actions/runs/42538258436) |

Funciona no navegador com até 40 cenas, sem conta nem salvamento automático. O projeto JSON inclui as imagens normalizadas para continuar a edição; Markdown e CSV organizam o roteiro e a gravação, e a impressão usa o diálogo do navegador. Os dados permanecem locais: guarde o JSON antes de fechar a página.

<!-- DELIVERY-VIDEO-2026-11-08:END -->

<!-- DELIVERY-OFX-2026-11-08:BEGIN -->
## Extrato OFX · extratos locais, valores exatos

Biblioteca e CLI Python para converter extratos bancários e de cartão em JSON, CSV e Markdown. Preservam valores decimais, datas com offset, saldos, correções e identificadores repetidos, com diagnósticos e cobertura explícita do perfil interpretado.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Extrato OFX](https://github.com/martinlofranodeoliveira/extrato-ofx) · Python · MIT · README em português | [Extratos e relatórios fictícios](https://github.com/martinlofranodeoliveira/extrato-ofx/tree/main/examples) | [v1.0.0](https://github.com/martinlofranodeoliveira/extrato-ofx/releases/tag/v1.0.0) · 104 testes na suíte · [CI Linux/Windows](https://github.com/martinlofranodeoliveira/extrato-ofx/actions/runs/42531636608) |

Funciona offline após a instalação e requer Python 3.11+ e defusedxml. Não conecta contas, não aplica correções nem reconcilia saldos. Uma lista ausente se distingue de uma lista vazia; campos desconhecidos tornam a cobertura incompleta e bloqueiam o CSV por padrão. Todos os exemplos são inventados.

<!-- DELIVERY-OFX-2026-11-08:END -->

<!-- DELIVERY-CONTACT-2026-11-08:BEGIN -->
## Folha de Contato · fotos que viram catálogo

Organize fotos de produtos, informe nomes, referências e preços opcionais e monte páginas A4/Carta. A mesa de edição reúne folha, formulário e sequência numerada; o projeto JSON leva as imagens normalizadas junto para continuar em outro navegador.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/folha-de-contato/) | [Folha de Contato](https://github.com/martinlofranodeoliveira/folha-de-contato) · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/folha-de-contato/releases/tag/v1.0.0) · 62 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/folha-de-contato/actions/runs/42527098441) |

Exporta PNG/SVG da página atual e JSON completo. Funciona no navegador com até 32 produtos, sem salvamento automático: guarde o projeto para continuar depois. Os preços são informados por quem edita. O exemplo usa objetos, referências e preços fictícios.

<!-- DELIVERY-CONTACT-2026-11-08:END -->

<!-- DELIVERY-CIVIL-2026-11-08:BEGIN -->
## Recorrência Civil · calcule séries de datas

Biblioteca e CLI Python para expandir regras diárias, semanais, mensais e anuais, com inclusões e exceções. Uma série mensal no dia 31 pula os meses incompatíveis; limites explícitos interrompem a consulta com um prefixo comprovado, sem apresentar a lista parcial como completa.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Recorrência Civil](https://github.com/martinlofranodeoliveira/recorrencia-civil) · Python · MIT · README em português | [Entradas e relatórios sintéticos](https://github.com/martinlofranodeoliveira/recorrencia-civil/tree/main/examples) | [v1.0.0](https://github.com/martinlofranodeoliveira/recorrencia-civil/releases/tag/v1.0.0) · 75 testes · [CI Linux/Windows](https://github.com/martinlofranodeoliveira/recorrencia-civil/actions/runs/42520927671) |

Requer Python 3.11+, funciona offline e usa somente a biblioteca padrão na execução. Exporta JSON, Markdown e CSV. Implementa um perfil de datas da RFC 5545: não importa ICS, não calcula horários ou fusos e não executa uma agenda. Uma divergência conhecida com dateutil está reproduzida na documentação.

<!-- DELIVERY-CIVIL-2026-11-08:END -->

<!-- DELIVERY-PAUTA-2026-11-08:BEGIN -->
## Pauta Aberta · da reunião aos próximos passos

Prepare a pauta, registre decisões e acompanhe encaminhamentos com responsável e prazo. A ficha continua editável; cada versão da ata preserva uma cópia independente do que foi registrado. Funciona no navegador, com backup JSON, Markdown histórico, CSV e salvamento local opcional.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/pauta-aberta/) | [Pauta Aberta](https://github.com/martinlofranodeoliveira/pauta-aberta) · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/pauta-aberta/releases/tag/v1.0.0) · 103 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/pauta-aberta/actions/runs/42517233074) |

A pauta e o registro preservado aparecem lado a lado no computador; os encaminhamentos viram fichas completas no celular. O exemplo é inteiramente fictício. Atas locais organizam o histórico informado e não equivalem a uma assinatura ou comprovação de presença.

<!-- DELIVERY-PAUTA-2026-11-08:END -->

<!-- DELIVERY-EPUB-2026-11-08:BEGIN -->
## EPUB Navigation Audit · confira a navegação de livros digitais

Biblioteca e CLI Python que conferem a rendição selecionada, o manifest, a ordem de leitura, os destinos do sumário e seus fragmentos em um EPUB local. Produzem JSON ou Markdown, sem renderizar o livro ou executar seu conteúdo, com limites explícitos e distinção entre erro comprovado e verificação incompleta.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [EPUB Navigation Audit](https://github.com/martinlofranodeoliveira/epub-navigation-audit) · Python · MIT · README em português | [Gerador e relatórios sintéticos](https://github.com/martinlofranodeoliveira/epub-navigation-audit/tree/main/examples) | [v1.0.0](https://github.com/martinlofranodeoliveira/epub-navigation-audit/releases/tag/v1.0.0) · 105 testes na suíte · [CI Linux/Windows](https://github.com/martinlofranodeoliveira/epub-navigation-audit/actions/runs/42477675035) |

Doze exemplos originais foram confrontados com EPUBCheck 5.3.0; URLs do subconjunto aceito foram comparadas ao WHATWG URL do Node.js. Requer Python 3.11+ e defusedxml. A ferramenta cobre seu perfil documentado e não substitui a validação integral de EPUB. A CI inclui instalação fora dos fontes; o teste de FIFO é omitido no Windows.

<!-- DELIVERY-EPUB-2026-11-08:END -->

<!-- DELIVERY-DECISION-2026-11-08:BEGIN -->
## Decisões Abertas · compare alternativas com contexto

Defina critérios, pesos e notas, veja o cálculo e registre sua escolha com uma justificativa. O aplicativo distingue lacunas de nota zero, mostra intervalos enquanto faltam respostas e preserva versões da matriz. Funciona no navegador com backup JSON, relatórios Markdown/CSV e salvamento local opcional.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/decisoes-abertas/) | [Decisões Abertas](https://github.com/martinlofranodeoliveira/decisoes-abertas) · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/decisoes-abertas/releases/tag/v1.0.0) · 93 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/decisoes-abertas/actions/runs/42473656383) |

A matriz se transforma em fichas no celular. Um backup fictício foi restaurado e reexportado sem alterar seus bytes; o relatório histórico preservou a escolha anterior. A pontuação organiza as informações fornecidas e a conclusão continua sendo da pessoa que usa o aplicativo.

<!-- DELIVERY-DECISION-2026-11-08:END -->

<!-- DELIVERY-SQLITE-CATALOG-2026-11-08:BEGIN -->
## SQLite Catalog Report · documentação de bancos

Biblioteca e CLI Python que documentam o esquema de um arquivo SQLite em JSON, Markdown e Mermaid, sem exportar os registros das tabelas. Incluem colunas, índices, chaves estrangeiras, ciclos e camadas de dependência, com fingerprint dos metadados e indicação explícita de capturas parciais.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [SQLite Catalog Report](https://github.com/martinlofranodeoliveira/sqlite-catalog-report) · Python · MIT · README em português | [Esquema, gerador e relatórios sintéticos](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/tree/main/examples) | [v1.0.0](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/releases/tag/v1.0.0) · 81 testes · [CI Linux/Windows](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/actions/runs/42470742835) |

Requer Python 3.11+ e SQLite 3.37+, sem dependências de execução externas à biblioteca padrão. Cada job da CI constrói o pacote e testa a distribuição instalada fora da árvore de fontes. O grafo descreve relações declaradas; não verifica os dados do banco.

<!-- DELIVERY-SQLITE-CATALOG-2026-11-08:END -->

<!-- DELIVERY-WHEEL-2026-11-08:BEGIN -->
## Wheel Record Audit · conferência de pacotes Python

Biblioteca e CLI que conferem inventário, metadados selecionados, hashes, tamanhos e CRC de um wheel local, sem instalar ou executar o pacote auditado. Relatórios JSON/Markdown distinguem divergências comprovadas de verificações incompletas por limite ou recurso fora do perfil.

| Código e documentação | Experimentar | Versão e verificação |
| --- | --- | --- |
| [Wheel Record Audit](https://github.com/martinlofranodeoliveira/wheel-record-audit) · Python · MIT · README em português | [Gerador e relatórios sintéticos](https://github.com/martinlofranodeoliveira/wheel-record-audit/tree/main/examples) | [v1.0.0](https://github.com/martinlofranodeoliveira/wheel-record-audit/releases/tag/v1.0.0) · 133 testes na suíte · [CI Linux/Windows](https://github.com/martinlofranodeoliveira/wheel-record-audit/actions/runs/42468166025) |

A CI inclui Python 3.11–3.14 no Linux e 3.14 no Windows, com instalação fora da árvore e auditoria do próprio wheel. O teste de FIFO é omitido no Windows. A ferramenta confere seu perfil documentado; hashes internos não autenticam a procedência nem comprovam a segurança do código.

<!-- DELIVERY-WHEEL-2026-11-08:END -->

<!-- DELIVERY-STUDY-2026-11-08:BEGIN -->
## Caderno de Revisões · cartões e prática de estudo

Crie baralhos e cartões, revele a resposta na própria fila e registre sua autoavaliação. Uma regra explícita calcula a próxima data; versões do conteúdo preservam o histórico anterior. Funciona no navegador, com backup JSON, importação CSV com prévia e salvamento local opcional com controle de conflitos.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/caderno-revisoes/) | [Caderno de Revisões](https://github.com/martinlofranodeoliveira/caderno-revisoes) · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/caderno-revisoes/releases/tag/v1.0.0) · 80 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/caderno-revisoes/actions/runs/42465613140) |

A demonstração restaurou e reexportou um backup fictício com 2 baralhos, 6 cartões e 5 avaliações sem alterar seus bytes. A importação de dois cartões e uma nova avaliação também foram conferidas no site publicado. Interface revisada em desktop e celular; os intervalos são uma regra de organização, sem promessa de eficácia pedagógica ou notificações em segundo plano.

<!-- DELIVERY-STUDY-2026-11-08:END -->

<!-- DELIVERY-WARRANTY-2026-11-08:BEGIN -->
## Garantia Aberta · bens, comprovantes e cuidados

Inventário pessoal no navegador com busca, categorias, documentos e agenda de manutenção. Os prazos são informados por quem usa o aplicativo. O backup JSON inclui os anexos e verifica sua integridade antes de restaurar; o salvamento em IndexedDB é opcional e controla conflitos entre revisões.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/garantia-aberta/) | [Garantia Aberta](https://github.com/martinlofranodeoliveira/garantia-aberta) · MIT · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/garantia-aberta/releases/tag/v1.0.0) · 75 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/garantia-aberta/actions/runs/42461183329) |

A demonstração publicada restaurou e reexportou um backup fictício com 3 bens e 1 anexo, preservando os dados e o PDF baixado. Interface conferida em desktop e celular. A agenda é consultada no aplicativo, sem notificações em segundo plano.

<!-- DELIVERY-WARRANTY-2026-11-08:END -->

<!-- DELIVERY-QUOTE-2026-11-08:BEGIN -->
## Orçamento Aberto · aplicação para pequenos negócios

Editor de orçamentos em BRL, com cálculo exato, quantidades fracionadas, desconto, adicional, prévia e exportação JSON, CSV e HTML. Funciona no navegador, com salvamento local opcional e licença MIT. A impressão usa o diálogo do navegador, inclusive a opção de PDF quando disponível.

| Usar | Código e documentação | Versão e verificação |
| --- | --- | --- |
| [Abrir demonstração](https://martinlofranodeoliveira.github.io/lofrano-orcamentos-open/) | [Orçamento Aberto](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open) · README em português | [v1.0.0](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/releases/tag/v1.0.0) · 47 testes · [CI Node.js 22/24](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/actions/runs/42457496754) |

A demonstração publicada foi conferida em navegador, com revisão visual em desktop e celular. Os exemplos são fictícios; o aplicativo não envia os orçamentos a um backend de negócio.

<!-- DELIVERY-QUOTE-2026-11-08:END -->

<!-- DELIVERY-2026-11-08:BEGIN -->
## Novas ferramentas · 8 de novembro de 2026

Três bibliotecas e CLIs Python com licença MIT, README em português, exemplos executáveis e releases para download. Foram conferidos 67 testes locais e os workflows públicos de cada projeto.

| Projeto | Finalidade | Verificação e download |
| --- | --- | --- |
| [HTTP Contract Diff](https://github.com/martinlofranodeoliveira/http-contract-diff) | Compara contratos HTTP JSON e aponta mudanças incompatíveis antes de uma entrega. Perfil plano explícito, sem consulta à API. | 19 testes · [CI](https://github.com/martinlofranodeoliveira/http-contract-diff/actions/runs/42455372230) · [v1.0.0](https://github.com/martinlofranodeoliveira/http-contract-diff/releases/tag/v1.0.0) |
| [Resource Booking Ledger](https://github.com/martinlofranodeoliveira/resource-booking-ledger) | Controla reservas de salas e equipamentos por pico simultâneo, com capacidade, idempotência e transações SQLite. | 20 testes · [CI](https://github.com/martinlofranodeoliveira/resource-booking-ledger/actions/runs/42455375445) · [v1.0.0](https://github.com/martinlofranodeoliveira/resource-booking-ledger/releases/tag/v1.0.0) |
| [Conventional Changelog Kit](https://github.com/martinlofranodeoliveira/conventional-changelog-kit) | Gera changelog e recomenda versão a partir de mensagens convencionais em JSON ou Git local, sem publicar releases. | 28 testes · [CI](https://github.com/martinlofranodeoliveira/conventional-changelog-kit/actions/runs/42455375260) · [v1.0.0](https://github.com/martinlofranodeoliveira/conventional-changelog-kit/releases/tag/v1.0.0) |

<!-- DELIVERY-2026-11-08:END -->

<!-- FIRST-BATCH:BEGIN -->
## Primeira leva · 10 projetos abertos

**Publicado · desenvolvimento 0.1.** Esta primeira leva reúne 10 projetos abertos com documentação bilíngue, testes e demos locais. Os links de Actions permitem conferir o status atual da CI de cada repositório.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Health Probe CLI](https://github.com/martinlofranodeoliveira/health-probe-cli) | Go | Confere um GET HTTP, status esperado, latência e limite de resposta. | [Docs](https://github.com/martinlofranodeoliveira/health-probe-cli/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/health-probe-cli/actions/workflows/ci.yml) |
| [Webhook Signature Lab](https://github.com/martinlofranodeoliveira/webhook-signature-lab) | TypeScript | Assina e verifica corpos brutos com HMAC e tempo explícito. | [Docs](https://github.com/martinlofranodeoliveira/webhook-signature-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/webhook-signature-lab/actions/workflows/ci.yml) |
| [NDJSON Redact](https://github.com/martinlofranodeoliveira/ndjson-redact) | Rust | Substitui campos de NDJSON por JSON Pointer, com limites e diagnósticos sem valores. | [Docs](https://github.com/martinlofranodeoliveira/ndjson-redact/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/ndjson-redact/actions/workflows/ci.yml) |
| [Approval Flow Core](https://github.com/martinlofranodeoliveira/approval-flow-core) | TypeScript | Organiza transições de aprovação, versão esperada e histórico reconstruível. | [Docs](https://github.com/martinlofranodeoliveira/approval-flow-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/approval-flow-core/actions/workflows/ci.yml) |
| [OpenAPI Example Check](https://github.com/martinlofranodeoliveira/openapi-example-check) | TypeScript | Confere exemplos JSON no recorte documentado de OpenAPI 3.1.1, offline. | [Docs](https://github.com/martinlofranodeoliveira/openapi-example-check/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/openapi-example-check/actions/workflows/ci.yml) |
| [Retrieval Eval Kit](https://github.com/martinlofranodeoliveira/retrieval-eval-kit) | TypeScript | Avalia rankings rotulados com Recall@K, MRR@K, fonte e abstenção. | [Docs](https://github.com/martinlofranodeoliveira/retrieval-eval-kit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/retrieval-eval-kit/actions/workflows/ci.yml) |
| [Tenant Policy Lab](https://github.com/martinlofranodeoliveira/tenant-policy-lab) | SQL · PostgreSQL | Demonstra RLS por tenant com papéis distintos, dados fictícios e testes negativos. | [Docs](https://github.com/martinlofranodeoliveira/tenant-policy-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/tenant-policy-lab/actions/workflows/ci.yml) |
| [Cursor Page Kit](https://github.com/martinlofranodeoliveira/cursor-page-kit) | PHP | Demonstra paginação por chave composta, cursor validado e snapshot SQLite. | [Docs](https://github.com/martinlofranodeoliveira/cursor-page-kit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/cursor-page-kit/actions/workflows/ci.yml) |
| [Static Link Audit](https://github.com/martinlofranodeoliveira/static-link-audit) | Ruby | Confere destinos e fragmentos de links em uma exportação HTML local. | [Docs](https://github.com/martinlofranodeoliveira/static-link-audit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/static-link-audit/actions/workflows/ci.yml) |
| [Business Day Calendar](https://github.com/martinlofranodeoliveira/business-day-calendar) | Java | Calcula datas úteis com fins de semana e fechamentos explicitamente configurados. | [Docs](https://github.com/martinlofranodeoliveira/business-day-calendar/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/business-day-calendar/actions/workflows/ci.yml) |

<!-- FIRST-BATCH:END -->

<!-- SECOND-BATCH:BEGIN -->
## Segunda leva · 8 projetos abertos

**Publicado · desenvolvimento 0.1.** Mais oito ferramentas com contratos explícitos, documentação em português e inglês, testes e demos reproduzíveis. Confira a execução atual nos links de Actions.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Trace Waterfall SVG](https://github.com/martinlofranodeoliveira/trace-waterfall-svg) | C++ | Transforma eventos de trace em SVG com faixas, tempos e prévia reproduzível. | [Docs](https://github.com/martinlofranodeoliveira/trace-waterfall-svg/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/trace-waterfall-svg/actions/workflows/ci.yml) |
| [HAR Budget Audit](https://github.com/martinlofranodeoliveira/har-budget-audit) | Dart | Audita requisições, bytes conhecidos e latência de HAR com resultado explícito quando faltam dados. | [Docs](https://github.com/martinlofranodeoliveira/har-budget-audit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/har-budget-audit/actions/workflows/ci.yml) |
| [Test Shard Plan](https://github.com/martinlofranodeoliveira/test-shard-plan) | Python | Distribui testes por duração estimada e grupos de afinidade, com plano determinístico. | [Docs](https://github.com/martinlofranodeoliveira/test-shard-plan/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/test-shard-plan/actions/workflows/ci.yml) |
| [Metric Cardinality Audit](https://github.com/martinlofranodeoliveira/metric-cardinality-audit) | Lua | Conta séries e valores de rótulos de métricas e confere orçamentos de cardinalidade. | [Docs](https://github.com/martinlofranodeoliveira/metric-cardinality-audit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/metric-cardinality-audit/actions/workflows/ci.yml) |
| [Sequence Gap Audit](https://github.com/martinlofranodeoliveira/sequence-gap-audit) | Elixir | Encontra intervalos ausentes, repetições e chegadas fora de ordem em logs sequenciais. | [Docs](https://github.com/martinlofranodeoliveira/sequence-gap-audit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/sequence-gap-audit/actions/workflows/ci.yml) |
| [HTTP Freshness Core](https://github.com/martinlofranodeoliveira/http-freshness-core) | Kotlin | Calcula frescor e decisões de cache HTTP dentro de um contrato documentado. | [Docs](https://github.com/martinlofranodeoliveira/http-freshness-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/http-freshness-core/actions/workflows/ci.yml) |
| [UTC Cron Preview](https://github.com/martinlofranodeoliveira/utc-cron-preview) | C# | Mostra próximas ocorrências de expressões cron no recorte UTC suportado. | [Docs](https://github.com/martinlofranodeoliveira/utc-cron-preview/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/utc-cron-preview/actions/workflows/ci.yml) |
| [POSIX Run Capture](https://github.com/martinlofranodeoliveira/posix-run-capture) | C | Executa um comando local com prazo, captura limitada de saída e resultado estruturado no Linux. | [Docs](https://github.com/martinlofranodeoliveira/posix-run-capture/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/posix-run-capture/actions/workflows/ci.yml) |

<!-- SECOND-BATCH:END -->

<!-- THIRD-BATCH:BEGIN -->
## Terceira leva · 14 projetos abertos

**Publicado · desenvolvimento 0.1.** Ferramentas e laboratórios com documentação bilíngue, testes e exemplos reproduzíveis. Os links de Actions mostram o estado atual do CI. As três demos web têm arquivos publicados conferidos por HTTP; a validação visual em navegador ainda está pendente.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [window-stats-stream](https://github.com/martinlofranodeoliveira/window-stats-stream) | Java | Calcula estatísticas em janelas com tempo explícito, fechamento e tratamento de eventos atrasados. | [Docs](https://github.com/martinlofranodeoliveira/window-stats-stream/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/window-stats-stream/actions/workflows/ci.yml) |
| [sse-stream-inspector](https://github.com/martinlofranodeoliveira/sse-stream-inspector) | Rust | Inspeciona eventos SSE com parsing incremental, limites e diagnósticos de UTF-8. | [Docs](https://github.com/martinlofranodeoliveira/sse-stream-inspector/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/sse-stream-inspector/actions/workflows/ci.yml) |
| [budget-hold-ledger](https://github.com/martinlofranodeoliveira/budget-hold-ledger) | Go | Modela reservas, despacho e custos incertos em cotas inteiras, com histórico verificável. | [Docs](https://github.com/martinlofranodeoliveira/budget-hold-ledger/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/budget-hold-ledger/actions/workflows/ci.yml) |
| [transactional-outbox-lab](https://github.com/martinlofranodeoliveira/transactional-outbox-lab) | Python | Demonstra outbox SQLite, leases, fencing e reentrega após perda da confirmação. | [Docs](https://github.com/martinlofranodeoliveira/transactional-outbox-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/transactional-outbox-lab/actions/workflows/ci.yml) |
| [positional-record-codec](https://github.com/martinlofranodeoliveira/positional-record-codec) | PHP | Codifica e confere registros posicionais com contrato, trailer e valores inteiros exatos. | [Docs](https://github.com/martinlofranodeoliveira/positional-record-codec/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/positional-record-codec/actions/workflows/ci.yml) |
| [rollout-rule-engine](https://github.com/martinlofranodeoliveira/rollout-rule-engine) | Ruby | Avalia regras de liberação com SemVer, dependências e distribuição determinística. | [Docs](https://github.com/martinlofranodeoliveira/rollout-rule-engine/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/rollout-rule-engine/actions/workflows/ci.yml) |
| [cidr-subnet-planner](https://github.com/martinlofranodeoliveira/cidr-subnet-planner) | Python | Planeja sub-redes IPv4/IPv6 e VLSM com limites e conservação de endereços. | [Docs](https://github.com/martinlofranodeoliveira/cidr-subnet-planner/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/cidr-subnet-planner/actions/workflows/ci.yml) |
| [freebusy-slot-studio](https://github.com/martinlofranodeoliveira/freebusy-slot-studio) | JavaScript | Encontra horários livres a partir de intervalos explícitos, com inspeção e exportação local. | [Docs](https://github.com/martinlofranodeoliveira/freebusy-slot-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/freebusy-slot-studio/actions/workflows/ci.yml) · [Demo](https://martinlofranodeoliveira.github.io/freebusy-slot-studio/) |
| [schema-form-studio](https://github.com/martinlofranodeoliveira/schema-form-studio) | JavaScript | Gera formulários de um subconjunto documentado de JSON Schema e explica erros. | [Docs](https://github.com/martinlofranodeoliveira/schema-form-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/schema-form-studio/actions/workflows/ci.yml) · [Demo](https://martinlofranodeoliveira.github.io/schema-form-studio/) |
| [github-evidence-board](https://github.com/martinlofranodeoliveira/github-evidence-board) | JavaScript | Inspeciona evidências de repositórios por commit, horário e cobertura de workflows. | [Docs](https://github.com/martinlofranodeoliveira/github-evidence-board/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/github-evidence-board/actions/workflows/ci.yml) · [Demo](https://martinlofranodeoliveira.github.io/github-evidence-board/) |
| [Config Provenance Resolver](https://github.com/martinlofranodeoliveira/config-provenance-resolver) | Rust | Resolve camadas de configuração com proveniência por caminho e redação de segredos. | [Docs](https://github.com/martinlofranodeoliveira/config-provenance-resolver/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/config-provenance-resolver/actions/workflows/ci.yml) |
| [SQLite Migration Rehearsal Lab](https://github.com/martinlofranodeoliveira/sqlite-migration-rehearsal-lab) | Python | Ensaios de migração up/down/up em cópias SQLite, conferindo esquema e dados. | [Docs](https://github.com/martinlofranodeoliveira/sqlite-migration-rehearsal-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/sqlite-migration-rehearsal-lab/actions/workflows/ci.yml) |
| [Fulfillment Reconciliation Lab](https://github.com/martinlofranodeoliveira/fulfillment-reconciliation-lab) | Go | Concilia pedidos, reservas e remessas sintéticos, destacando conflitos e evidências ausentes. | [Docs](https://github.com/martinlofranodeoliveira/fulfillment-reconciliation-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/fulfillment-reconciliation-lab/actions/workflows/ci.yml) |
| [Resumable Transfer Lab](https://github.com/martinlofranodeoliveira/resumable-transfer-lab) | C# | Demonstra retomada HTTP por Range, ETag, checkpoint e SHA-256 esperado em loopback. | [Docs](https://github.com/martinlofranodeoliveira/resumable-transfer-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/resumable-transfer-lab/actions/workflows/ci.yml) |

<!-- THIRD-BATCH:END -->

<!-- FOURTH-BATCH:BEGIN -->
## Núcleos de execução · 4 projetos abertos

**Publicado · desenvolvimento 0.1.** Bibliotecas e laboratórios com contratos de estado e recursos explícitos, testes independentes e demos locais.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Saga Compensation Lab](https://github.com/martinlofranodeoliveira/saga-compensation-lab) | Java | Demonstra compensação reversa, persistência e reconciliação de resultados incertos com serviços HTTP locais. | [Docs](https://github.com/martinlofranodeoliveira/saga-compensation-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/saga-compensation-lab/actions/workflows/ci.yml) |
| [Duplex Drain Pump](https://github.com/martinlofranodeoliveira/duplex-drain-pump) | C | Retransmite dois fluxos Linux com buffers limitados, contrapressão e half-close por direção. | [Docs](https://github.com/martinlofranodeoliveira/duplex-drain-pump/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/duplex-drain-pump/actions/workflows/ci.yml) |
| [Guillotine Cut Plan](https://github.com/martinlofranodeoliveira/guillotine-cut-plan) | C++ | Planeja cortes guilhotinados com espessura de corte e certificado geométrico verificável. | [Docs](https://github.com/martinlofranodeoliveira/guillotine-cut-plan/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/guillotine-cut-plan/actions/workflows/ci.yml) |
| [Deficit Round Queue](https://github.com/martinlofranodeoliveira/deficit-round-queue) | Lua | Escalona custos declarados por deficit round-robin, com filas limitadas e contabilidade exata. | [Docs](https://github.com/martinlofranodeoliveira/deficit-round-queue/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/deficit-round-queue/actions/workflows/ci.yml) |

<!-- FOURTH-BATCH:END -->

<!-- FIFTH-BATCH:BEGIN -->
## Concorrência e integração · 3 projetos abertos

**Publicado · desenvolvimento 0.1.** Exemplos verificáveis de estado, processamento externo e integração com processos locais.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [ETS Snapshot Bundles](https://github.com/martinlofranodeoliveira/ets-snapshot-bundles) | Elixir | Publica gerações imutáveis de dados ETS com leases por processo, limites e limpeza de pins. | [Docs](https://github.com/martinlofranodeoliveira/ets-snapshot-bundles/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/ets-snapshot-bundles/actions/workflows/ci.yml) |
| [Spill Outer Join](https://github.com/martinlofranodeoliveira/spill-outer-join) | Kotlin | Faz full outer join de JSONL com ordenação externa, multiplicidade e limites compartilhados de disco. | [Docs](https://github.com/martinlofranodeoliveira/spill-outer-join/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/spill-outer-join/actions/workflows/ci.yml) |
| [MQTT Session Recovery Lab](https://github.com/martinlofranodeoliveira/mqtt-session-recovery-lab) | Go | Exercita retained, recuperação de sessão, reinício e Last Will com um broker local próprio. | [Docs](https://github.com/martinlofranodeoliveira/mqtt-session-recovery-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/mqtt-session-recovery-lab/actions/workflows/ci.yml) |

<!-- FIFTH-BATCH:END -->

<!-- SIXTH-BATCH:BEGIN -->
## Algoritmos e laboratórios · 12 projetos abertos

**Publicado · desenvolvimento 0.1.** Ferramentas com contratos explícitos, referências, testes independentes e demos reproduzíveis.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Pairwise Fixture Plan](https://github.com/martinlofranodeoliveira/pairwise-fixture-plan) | Python | Gera fixtures que cobrem pares viáveis de opções, com restrições declarativas e verificador independente. | [Docs](https://github.com/martinlofranodeoliveira/pairwise-fixture-plan/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/pairwise-fixture-plan/actions/workflows/ci.yml) |
| [Capability Match Core](https://github.com/martinlofranodeoliveira/capability-match-core) | PHP | Maximiza atribuições compatíveis e minimiza custo inteiro, com certificados de fluxo e custo. | [Docs](https://github.com/martinlofranodeoliveira/capability-match-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/capability-match-core/actions/workflows/ci.yml) |
| [PostgreSQL Isolation Replay Lab](https://github.com/martinlofranodeoliveira/postgres-isolation-replay-lab) | Ruby | Reproduz anomalias de isolamento, rollback e retentativas com PostgreSQL próprio e barreiras. | [Docs](https://github.com/martinlofranodeoliveira/postgres-isolation-replay-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/postgres-isolation-replay-lab/actions/workflows/ci.yml) |
| [Loopback DNS Cache Lab](https://github.com/martinlofranodeoliveira/loopback-dns-cache-lab) | TypeScript | Exercita cache DNS positivo/negativo e recuperação UDP para TCP com autoridade local. | [Docs](https://github.com/martinlofranodeoliveira/loopback-dns-cache-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/loopback-dns-cache-lab/actions/workflows/ci.yml) |
| [Rollback Connectivity Timeline](https://github.com/martinlofranodeoliveira/rollback-connectivity-timeline) | Rust | Consulta conectividade ao longo de um histórico de arestas com union-find reversível. | [Docs](https://github.com/martinlofranodeoliveira/rollback-connectivity-timeline/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/rollback-connectivity-timeline/actions/workflows/ci.yml) |
| [Orthogonal Route Core](https://github.com/martinlofranodeoliveira/orthogonal-route-core) | C++ | Roteia conectores em grade inteira com obstáculos, comprimento mínimo e desempate por curvas. | [Docs](https://github.com/martinlofranodeoliveira/orthogonal-route-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/orthogonal-route-core/actions/workflows/ci.yml) |
| [Bounded Token Net](https://github.com/martinlofranodeoliveira/bounded-token-net) | Elixir | Explora modelos finitos de recursos e devolve testemunhos de deadlock e limites de exploração. | [Docs](https://github.com/martinlofranodeoliveira/bounded-token-net/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/bounded-token-net/actions/workflows/ci.yml) |
| [Revision Validity Index](https://github.com/martinlofranodeoliveira/revision-validity-index) | Kotlin | Preserva consultas históricas por revisão ao corrigir intervalos de validade em memória. | [Docs](https://github.com/martinlofranodeoliveira/revision-validity-index/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/revision-validity-index/actions/workflows/ci.yml) |
| [Fenced Weight Cache](https://github.com/martinlofranodeoliveira/fenced-weight-cache) | Dart | Combina cache LRU por peso, TTL e carregamento único com proteção contra resultados antigos. | [Docs](https://github.com/martinlofranodeoliveira/fenced-weight-cache/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/fenced-weight-cache/actions/workflows/ci.yml) |
| [Mask Region Core](https://github.com/martinlofranodeoliveira/mask-region-core) | Java | Calcula componentes, buracos e distâncias quadráticas exatas em máscaras binárias, com adaptador PNG. | [Docs](https://github.com/martinlofranodeoliveira/mask-region-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/mask-region-core/actions/workflows/ci.yml) |
| [Stripe Recovery Kit](https://github.com/martinlofranodeoliveira/stripe-recovery-kit) | Rust | Restaura arquivos a partir de fragmentos redundantes, tratando blocos ausentes ou corrompidos. | [Docs](https://github.com/martinlofranodeoliveira/stripe-recovery-kit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/stripe-recovery-kit/actions/workflows/ci.yml) |
| [Bounded Observed Set](https://github.com/martinlofranodeoliveira/bounded-observed-set) | C# | Modela conjunto replicado com remoção observada, histórico limitado e snapshots validados. | [Docs](https://github.com/martinlofranodeoliveira/bounded-observed-set/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/bounded-observed-set/actions/workflows/ci.yml) |

<!-- SIXTH-BATCH:END -->

<!-- SEVENTH-BATCH:BEGIN -->
## Sétima leva · 7 projetos abertos

**Publicado · desenvolvimento 0.1.** Sete projetos com documentação bilíngue, testes e demos locais verificáveis. Os contratos descrevem os limites de cada implementação; consulte a execução atual nos links de Actions.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Monotone Curve Core](https://github.com/martinlofranodeoliveira/monotone-curve-core) | Dart | Interpola dados crescentes com PCHIP, derivadas, integrais e intervalos inversos explícitos. | [Docs](https://github.com/martinlofranodeoliveira/monotone-curve-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/monotone-curve-core/actions/workflows/ci.yml) |
| [Selection Bitmap Core](https://github.com/martinlofranodeoliveira/selection-bitmap-core) | C# | Avalia predicados tipados em bitmaps, preservando resultados verdadeiros, falsos e desconhecidos. | [Docs](https://github.com/martinlofranodeoliveira/selection-bitmap-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/selection-bitmap-core/actions/workflows/ci.yml) |
| [Source Map Chain Replay Lab](https://github.com/martinlofranodeoliveira/source-map-chain-replay-lab) | TypeScript | Reproduz mapas encadeados de código com TypeScript, esbuild e comparação com o Node. | [Docs](https://github.com/martinlofranodeoliveira/source-map-chain-replay-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/source-map-chain-replay-lab/actions/workflows/ci.yml) |
| [Revisioned FTS Search Lab](https://github.com/martinlofranodeoliveira/revisioned-fts-search-lab) | PHP | Demonstra busca FTS5, revisões, tombstones e consultas consistentes entre HTTP e SQLite. | [Docs](https://github.com/martinlofranodeoliveira/revisioned-fts-search-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/revisioned-fts-search-lab/actions/workflows/ci.yml) |
| [SMTP MIME Capture Lab](https://github.com/martinlofranodeoliveira/smtp-mime-capture-lab) | Ruby | Captura mensagens SMTP locais e inspeciona MIME com armazenamento e recuperação demonstráveis. | [Docs](https://github.com/martinlofranodeoliveira/smtp-mime-capture-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/smtp-mime-capture-lab/actions/workflows/ci.yml) |
| [Rational Polyphase Stream](https://github.com/martinlofranodeoliveira/rational-polyphase-stream) | C++ | Reamostra sequências numéricas em blocos com filtro FIR, limites e oráculo de convolução. | [Docs](https://github.com/martinlofranodeoliveira/rational-polyphase-stream/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/rational-polyphase-stream/actions/workflows/ci.yml) |
| [Connection Handoff Reload Lab](https://github.com/martinlofranodeoliveira/connection-handoff-reload-lab) | C | Demonstra troca de gerações e transferência de conexões TCP por descritores Unix. | [Docs](https://github.com/martinlofranodeoliveira/connection-handoff-reload-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/connection-handoff-reload-lab/actions/workflows/ci.yml) |

<!-- SEVENTH-BATCH:END -->

<!-- EIGHTH-BATCH:BEGIN -->
## Oitava leva · 9 projetos abertos

**Publicado · desenvolvimento 0.1.0.** Nove projetos com documentação bilíngue, testes e demos locais. Os links de Actions permitem conferir o commit e o resultado da execução atual; os contratos registram o alcance de cada implementação.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Anchored Affine Alignment](https://github.com/martinlofranodeoliveira/anchored-affine-alignment) | Kotlin | Biblioteca de alinhamento global com custo afim de lacunas, âncoras obrigatórias, desempate determinístico e operações verificáveis. | [Docs](https://github.com/martinlofranodeoliveira/anchored-affine-alignment/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/anchored-affine-alignment/actions/workflows/ci.yml) |
| [Control Flow Dominance Core](https://github.com/martinlofranodeoliveira/control-flow-dominance-core) | Java | Biblioteca de análise de fluxo de controle com dominância, pós-dominância condicionada à saída, dependências e laços naturais verificáveis. | [Docs](https://github.com/martinlofranodeoliveira/control-flow-dominance-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/control-flow-dominance-core/actions/workflows/ci.yml) |
| [Git Bundle Merge Rehearsal](https://github.com/martinlofranodeoliveira/git-bundle-merge-rehearsal) | Ruby | Aplicação offline para ensaiar merges de bundles Git em repositório descartável, produzindo resultado verificável ou conflitos estruturados. | [Docs](https://github.com/martinlofranodeoliveira/git-bundle-merge-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/git-bundle-merge-rehearsal/actions/workflows/ci.yml) |
| [gRPC Cancellation Tree Lab](https://github.com/martinlofranodeoliveira/grpc-cancel-tree-lab) | TypeScript | Laboratório gRPC sem interface gráfica para propagação de prazos, cancelamento cooperativo e contabilização de tarefas entre processos locais. | [Docs](https://github.com/martinlofranodeoliveira/grpc-cancel-tree-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/grpc-cancel-tree-lab/actions/workflows/ci.yml) |
| [Loopback TLS Rotation Lab](https://github.com/martinlofranodeoliveira/loopback-tls-rotation-lab) | Java | Laboratório JSSE para troca atômica de contexto TLS, preservação de sessões existentes e verificação local com PKI descartável. | [Docs](https://github.com/martinlofranodeoliveira/loopback-tls-rotation-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/loopback-tls-rotation-lab/actions/workflows/ci.yml) |
| [Multipart Object Commit Lab](https://github.com/martinlofranodeoliveira/multipart-object-commit-lab) | PHP | Aplicação local de upload multipart com publicação atômica de lotes, deduplicação por conteúdo e recuperação de arquivos órfãos. | [Docs](https://github.com/martinlofranodeoliveira/multipart-object-commit-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/multipart-object-commit-lab/actions/workflows/ci.yml) |
| [OFD Lock Ownership Lab](https://github.com/martinlofranodeoliveira/ofd-lock-ownership-lab) | C | Laboratório Linux de locks por faixa de bytes, com processos concorrentes, herança de descritores e aquisição com prazo explícito. | [Docs](https://github.com/martinlofranodeoliveira/ofd-lock-ownership-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/ofd-lock-ownership-lab/actions/workflows/ci.yml) |
| [Revisioned Text Buffer](https://github.com/martinlofranodeoliveira/revisioned-text-buffer) | C++ | Biblioteca de texto UTF-8 com edições múltiplas atômicas, snapshots imutáveis, posições UTF-16 e mapas explícitos de reposicionamento. | [Docs](https://github.com/martinlofranodeoliveira/revisioned-text-buffer/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/revisioned-text-buffer/actions/workflows/ci.yml) |
| [Verified Block Delta](https://github.com/martinlofranodeoliveira/verified-block-delta) | Rust | Biblioteca de diferenças binárias com assinaturas deslizantes, operações determinísticas e aplicação verificada sem alterar o arquivo base. | [Docs](https://github.com/martinlofranodeoliveira/verified-block-delta/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/verified-block-delta/actions/workflows/ci.yml) |

<!-- EIGHTH-BATCH:END -->

<!-- NINTH-BATCH:BEGIN -->
## Nona leva · 11 projetos abertos

**Publicado · desenvolvimento 0.1.0.** Onze projetos com documentação bilíngue, testes e demonstrações. Três aplicações React incluem cenas 3D e versões acessíveis por GitHub Pages; a revisão visual em navegador permanece pendente. Consulte o contrato e o commit de cada execução em Actions.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Cabinet Assembly Studio](https://github.com/martinlofranodeoliveira/cabinet-assembly-studio) | TypeScript | Configura um gabinete em 3D, explora a montagem e exporta medidas e componentes conceituais. | [Docs](https://github.com/martinlofranodeoliveira/cabinet-assembly-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/cabinet-assembly-studio/actions/workflows/ci.yml) |
| [Frame Transform Studio](https://github.com/martinlofranodeoliveira/frame-transform-studio) | TypeScript | Explora hierarquias de coordenadas em 3D e compara poses locais e globais. | [Docs](https://github.com/martinlofranodeoliveira/frame-transform-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/frame-transform-studio/actions/workflows/ci.yml) |
| [Integer Periodic Neighbors](https://github.com/martinlofranodeoliveira/integer-periodic-neighbors) | Python | Biblioteca de vizinhança periódica com coordenadas inteiras, reconstrução conservadora e comparação exata com um oráculo de todos os pares. | [Docs](https://github.com/martinlofranodeoliveira/integer-periodic-neighbors/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/integer-periodic-neighbors/actions/workflows/ci.yml) |
| [Logical Snapshot Handoff Lab](https://github.com/martinlofranodeoliveira/logical-snapshot-handoff-lab) | Go | Laboratório PostgreSQL/SQLite para bootstrap por snapshot exportado, replicação lógica transacional e retomada após falhas. | [Docs](https://github.com/martinlofranodeoliveira/logical-snapshot-handoff-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/logical-snapshot-handoff-lab/actions/workflows/ci.yml) |
| [Modbus Register Replay Lab](https://github.com/martinlofranodeoliveira/modbus-register-replay-lab) | Rust | Laboratório Modbus TCP sintético com cliente, emulador independente e falhas controladas, sem hardware ou destinos externos. | [Docs](https://github.com/martinlofranodeoliveira/modbus-register-replay-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/modbus-register-replay-lab/actions/workflows/ci.yml) |
| [OCI Layer Effect Explorer](https://github.com/martinlofranodeoliveira/oci-layer-effect-explorer) | Go | Explica o sistema de arquivos efetivo de imagens OCI locais, incluindo whiteouts e origem por camada, sem executar a imagem. | [Docs](https://github.com/martinlofranodeoliveira/oci-layer-effect-explorer/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/oci-layer-effect-explorer/actions/workflows/ci.yml) |
| [Offline Dependency Capsule](https://github.com/martinlofranodeoliveira/offline-dependency-capsule) | Kotlin | Resolve catálogos locais de dependências com restrições explícitas, mudanças mínimas no lock e resultados inconclusivos quando o orçamento termina. | [Docs](https://github.com/martinlofranodeoliveira/offline-dependency-capsule/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/offline-dependency-capsule/actions/workflows/ci.yml) |
| [Relational Fixture Slice](https://github.com/martinlofranodeoliveira/relational-fixture-slice) | SQL | Extrai fixtures PostgreSQL limitadas, com fechamento referencial, e demonstra a restauração em outro banco vazio. | [Docs](https://github.com/martinlofranodeoliveira/relational-fixture-slice/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/relational-fixture-slice/actions/workflows/ci.yml) |
| [Revisioned Formula Cells](https://github.com/martinlofranodeoliveira/revisioned-formula-cells) | Dart | Biblioteca de fórmulas tipadas com edições atômicas, recálculo incremental e recibos de revisão, sem eval. | [Docs](https://github.com/martinlofranodeoliveira/revisioned-formula-cells/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/revisioned-formula-cells/actions/workflows/ci.yml) |
| [Scoped Congruence Explanations](https://github.com/martinlofranodeoliveira/scoped-congruence-explanations) | C# | Motor limitado de igualdades entre termos concretos, com congruência, escopos reversíveis e explicações de conflitos verificadas também pelo Z3. | [Docs](https://github.com/martinlofranodeoliveira/scoped-congruence-explanations/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/scoped-congruence-explanations/actions/workflows/ci.yml) |
| [Spatial Loading Studio](https://github.com/martinlofranodeoliveira/spatial-loading-studio) | TypeScript | Planeja a ocupação volumétrica em 3D com colisões explícitas, rotações e desfazer. | [Docs](https://github.com/martinlofranodeoliveira/spatial-loading-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/spatial-loading-studio/actions/workflows/ci.yml) |

<!-- NINTH-BATCH:END -->

<!-- TENTH-BATCH:BEGIN -->
## Décima leva · 7 projetos abertos

**Publicado · desenvolvimento 0.1.0.** Sete projetos com documentação bilíngue, testes e demonstrações locais. Os contratos explicam os limites e os links de Actions permitem conferir cada execução.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Trace Context Hop Lab](https://github.com/martinlofranodeoliveira/trace-context-hop-lab) | TypeScript | Reproduz propagação de contexto W3C entre serviços locais, com OpenTelemetry e verificações de continuidade e falhas. | [Docs](https://github.com/martinlofranodeoliveira/trace-context-hop-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/trace-context-hop-lab/actions/workflows/ci.yml) |
| [Byte Corpus Suffix Index](https://github.com/martinlofranodeoliveira/byte-corpus-suffix-index) | Lua | Indexa pequenos corpora binários com array de sufixos, busca sobreposta e contagens por documento. | [Docs](https://github.com/martinlofranodeoliveira/byte-corpus-suffix-index/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/byte-corpus-suffix-index/actions/workflows/ci.yml) |
| [Inotify Convergence Lab](https://github.com/martinlofranodeoliveira/inotify-convergence-lab) | C | Reconcilia diretórios próprios após eventos inotify, distinguindo estado atual, dados antigos e observação incompleta. | [Docs](https://github.com/martinlofranodeoliveira/inotify-convergence-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/inotify-convergence-lab/actions/workflows/ci.yml) |
| [Raster Priority Mosaic](https://github.com/martinlofranodeoliveira/raster-priority-mosaic) | Python | Produz mosaicos de rasters GeoTIFF com prioridade explícita, máscara de validade e conferência independente pelo GDAL. | [Docs](https://github.com/martinlofranodeoliveira/raster-priority-mosaic/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/raster-priority-mosaic/actions/workflows/ci.yml) |
| [LSP Rename Rehearsal](https://github.com/martinlofranodeoliveira/lsp-rename-rehearsal) | TypeScript | Ensaia renomeação semântica em cópia própria, verifica edições e compila o resultado sem alterar a origem. | [Docs](https://github.com/martinlofranodeoliveira/lsp-rename-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/lsp-rename-rehearsal/actions/workflows/ci.yml) |
| [Booklet Imposition Pack](https://github.com/martinlofranodeoliveira/booklet-imposition-pack) | PHP | Organiza páginas PDF em cadernos dobráveis, com mapa de posições e validação por estrutura, texto e rasterização. | [Docs](https://github.com/martinlofranodeoliveira/booklet-imposition-pack/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/booklet-imposition-pack/actions/workflows/ci.yml) |
| [Audio Edit Replay Lab](https://github.com/martinlofranodeoliveira/audio-edit-replay-lab) | C# | Monta cortes e silêncio de áudio PCM por índices de amostras, com mapa de saída e conferência dos valores decodificados. | [Docs](https://github.com/martinlofranodeoliveira/audio-edit-replay-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/audio-edit-replay-lab/actions/workflows/ci.yml) |

<!-- TENTH-BATCH:END -->

## Catálogo existente

| Projeto | Finalidade |
| --- | --- |
| [Gestão de igrejas — aplicação aberta](https://github.com/martinlofranodeoliveira/Gest-o-de-Igrejas-open) | Aplicação React com modo local no navegador e desktop Electron/SQLite. Começa sem cadastros, sem conta padrão e sem dados da operação anterior. |
| [Martin Guitar — portfólio artístico](https://github.com/martinlofranodeoliveira/MartinGuitarArtistViteJS) | Repositório de portfólio musical. O snapshot público contém subpastas; não foi identificado um comando de instalação na raiz. Consulte os manifests dentro da pasta da aplicação. |
| [Nexus — orquestrador de agentes de IA](https://github.com/martinlofranodeoliveira/NexusOrchestrator-open) | Servidor Node e interface React para tarefas, salas e integrações opcionais. O modo observador acompanha uma equipe externa sem executar comandos. |
| [Projeto colaborativo — exercícios de programação](https://github.com/martinlofranodeoliveira/ProjetoColaborativoDH) | Repositório de trabalho colaborativo educacional, com arquivo A.js no snapshot público. Autoria compartilhada deve ser preservada. |
| [Laboratório de agentes e simulações offline](https://github.com/martinlofranodeoliveira/ToTheMoonTokens-open) | API e dashboard para desenvolvimento local com fixtures sintéticas. Trading, carteiras, pagamentos, mainnet e provedores financeiros reais ficam fora desta avaliação. |
| [Planejador de tentativas e prazos](https://github.com/martinlofranodeoliveira/backoff-budget) | Calcula quantas tentativas e esperas cabem em um prazo, com duração explícita de cada tentativa. Não executa requisições nem dorme. |
| [Exportador de calendários ICS](https://github.com/martinlofranodeoliveira/calendar-ics-export) | Converte eventos JSON em arquivos iCalendar determinísticos, com horários UTC explícitos e exemplos fictícios. |
| [CineHouse — exercícios de JavaScript](https://github.com/martinlofranodeoliveira/cinehouse) | Repositório de estudo de JavaScript com arquivos de demonstração. O estado público é educacional e não representa uma plataforma de cinema pronta. |
| [Auditoria de contraste de cores](https://github.com/martinlofranodeoliveira/contrast-palette-audit) | Verifica pares opacos de cores sRGB, calcula contraste e relata os limiares de texto AA/AAA. Não certifica a acessibilidade completa de um site. |
| [Controle analítico — interface web](https://github.com/martinlofranodeoliveira/controleanalitico) | Interface React/TypeScript com Vite. Revise a configuração e utilize dados sintéticos na avaliação local; integrações externas não estão validadas por esta documentação. |
| [Validador de CSV por contrato](https://github.com/martinlofranodeoliveira/csv-contract-check) | Confere cabeçalhos, campos obrigatórios e tipos de um CSV conforme um contrato JSON explícito, sem inferir ou corrigir dados. |
| [Auditoria de CSV com esquema explícito](https://github.com/martinlofranodeoliveira/csv-schema-audit) | Audita CSV local com limites de recursos e diagnósticos sem ecoar valores. Mantém contrato público, testes protegidos e checagem da distribuição instalada. |
| [Importador de CSV para SQLite](https://github.com/martinlofranodeoliveira/csv-sqlite-import) | Valida e importa CSV em um banco SQLite novo, com esquema explícito opcional e publicação sem sobrescrever o destino. |
| [Validador de nomes de variáveis de ambiente](https://github.com/martinlofranodeoliveira/env-template-check) | Compara nomes esperados e encontrados em arquivos explícitos, sem imprimir seus valores. Não avalia conteúdo nem modifica o ambiente. |
| [Catálogo de filmes — exercício com Sequelize](https://github.com/martinlofranodeoliveira/exercicio-filme-sequelize) | Projeto educacional Node/Express com views EJS e acesso a banco via Sequelize. Não há implantação ou banco de demonstração provisionado. |
| [Exemplo de servidor HTTP com Express](https://github.com/martinlofranodeoliveira/express) | Exercício de servidor Express com arquivos HTML/CSS. Não confundir este repositório de estudo com o framework oficial Express. |
| [Manifestos e comparação de arquivos](https://github.com/martinlofranodeoliveira/file-manifest-check) | Inventaria conteúdos de uma pasta e compara snapshots no Linux. Não apaga, corrige, envia arquivos ou substitui um backup. |
| [GemCRM — CRM aberto para pequenos negócios](https://github.com/martinlofranodeoliveira/gemcrm-open) | CRM independente em português para contatos, empresas, oportunidades e tarefas. É auto-hospedado e mantém isolamento por conta. |
| [GemCRM — site institucional](https://github.com/martinlofranodeoliveira/gemcrm-site) | Site estático de apresentação do GemCRM. É uma interface institucional, não o servidor nem o banco do CRM. |
| [Projeto integrador — aplicação web Node](https://github.com/martinlofranodeoliveira/grupo1-pi) | Projeto educacional com Express, EJS e funcionalidades do trabalho integrador. Verifique rotas, configuração e persistência antes do uso local. |
| [Projeto integrador — API de estudo](https://github.com/martinlofranodeoliveira/grupo1-pi-backend) | Backend educacional Express/Sequelize com autenticação e componentes de e-mail. Configure somente serviços de teste próprios; não acione integrações reais na avaliação. |
| [Servidor HTTP local para testes](https://github.com/martinlofranodeoliveira/http-fixture-lab) | Servidor de fixtures restrito a loopback, com configuração explícita e limites. Serve respostas sintéticas para testes de integração. |
| [Analisador de intervalos HTTP Range](https://github.com/martinlofranodeoliveira/http-range-tools) | Interpreta cabeçalhos Range e resolve intervalos de bytes em fatias Python, totalmente offline. Não fornece um servidor HTTP. |
| [Controle de idempotência com SQLite](https://github.com/martinlofranodeoliveira/idempotency-ledger) | Registra reservas com fencing e resultados reproduzíveis, usando tempo explícito do chamador. Não executa transações financeiras ou tarefas do consumidor. |
| [Comparador de documentos JSON](https://github.com/martinlofranodeoliveira/json-pointer-diff) | Compara documentos JSON com números exatos e caminhos JSON Pointer. Opera localmente, sem sincronizar ou sobrescrever documentos. |
| [Validador de arquivos JSON Lines](https://github.com/martinlofranodeoliveira/jsonl-workbench) | Valida registros JSONL com limites de tamanho, profundidade e linhas, usando diagnósticos que não repetem o conteúdo. |
| [Resumo de relatórios de testes JUnit](https://github.com/martinlofranodeoliveira/junit-report-summary) | Lê XML JUnit e produz resumos JSON ou Markdown com totais de casos e parsing limitado. Não executa testes do projeto consumidor. |
| [Auditoria de chaves de tradução](https://github.com/martinlofranodeoliveira/locale-key-audit) | Encontra chaves ausentes e extras em catálogos JSON aninhados, sem incluir textos das traduções nos relatórios. |
| [Loft Flex — página web de estudo](https://github.com/martinlofranodeoliveira/loft) | Página HTML de apresentação. Conteúdo e referências comerciais pertencem ao contexto original do exemplo; não há serviço ou oferta provisionada por este repositório. |
| [Martin Guitar — registro de projeto](https://github.com/martinlofranodeoliveira/martinguitar) | Repositório público sem implementação no snapshot auditado. Esta documentação registra o estado para evitar a aparência de produto pronto. |
| [Medicina Consulta — interface legada de estudo](https://github.com/martinlofranodeoliveira/medicina-consulta) | Interface Ionic/React legada para estudo. Não distribua dados reais de pacientes e não trate esta interface como produto clínico certificado. |
| [Agendamento de consultas — protótipo aberto](https://github.com/martinlofranodeoliveira/medicina-consulta-open) | Servidor local de agendamentos com exemplos sintéticos e validação de conflitos. Núcleo/protótipo reutilizável, não o SaaS privado integral nem um sistema clínico certificado. |
| [Consulta médica — aplicação web legada](https://github.com/martinlofranodeoliveira/medicinaconsulta) | Aplicação educacional Express/EJS. Avalie somente com dados fictícios e configuração própria; sem garantia de operação clínica ou implantação pronta. |
| [Laboratório de análise de pacotes npm](https://github.com/martinlofranodeoliveira/opensource-rea-lab) | Auditoria offline de artefatos de software abertos e análises reproduzíveis. O pacote inspecionado é entrada não confiável; não há execução automática de scripts de instalação. |
| [Ferramentas abertas para tarefas de vídeo](https://github.com/martinlofranodeoliveira/sora2-videos-open) | Núcleo independente para filas de geração, cancelamento e inspeção local de mídia. A demonstração usa adaptadores simulados, não gera vídeo pago automaticamente. |
| [Snapshots consistentes de bancos SQLite](https://github.com/martinlofranodeoliveira/sqlite-snapshot-kit) | Cria cópias locais consistentes de SQLite, verifica integridade e publica sem sobrescrever destino. Não substitui estratégia completa de backup/recuperação. |
| [Validador de legendas SRT](https://github.com/martinlofranodeoliveira/srt-caption-check) | Valida legendas UTF-8 localmente e pode verificar sobreposição temporal. Não traduz, sincroniza áudio ou corrige legendas por conta própria. |
| [Starship 2050 — jogo de nave no navegador](https://github.com/martinlofranodeoliveira/starship-2050-open) | Jogo arcade com gráficos procedurais, pontuação local e servidor de desenvolvimento sem dependências. Os recursos privados da versão original não fazem parte desta edição. |
| [Stone Open — integração de pagamentos em PHP](https://github.com/martinlofranodeoliveira/stone-open) | Código de API/painel e esquema SQL com configuração explícita, webhook autenticado e TOTP local. Documentação e testes offline não autorizam cobranças ou operações reais. |
| [Inventário de oficina — demonstração comunitária](https://github.com/martinlofranodeoliveira/studio-69069ea233b84cc7bdbbc06053815f37) | Protótipo de catálogo, retirada e devolução de ferramentas com dados fictícios. Tudo acontece no navegador; não é um sistema pronto para produção. |
| [Planejador de tarefas com dependências](https://github.com/martinlofranodeoliveira/taskgraph-plan) | Organiza um DAG em ordem topológica, ondas de dependência e caminho crítico. Não executa as tarefas descritas. |
| [Zanvoria — RPG de criaturas no navegador](https://github.com/martinlofranodeoliveira/zanvoria-open) | Edição de código do jogo com gráficos procedurais, som do navegador e salvamento local. Imagens, vozes e outros recursos sem redistribuição estabelecida foram excluídos. |
| [ZelloLife — documentos clínicos seguros](https://github.com/martinlofranodeoliveira/zellolife-open) | Biblioteca reutilizável para renderização e validação de documentos fornecidos pelo chamador. Não inventa achados, não realiza decisão clínica e não abre o SaaS integral. |
| [Auditor de manifestos de arquivos ZIP](https://github.com/martinlofranodeoliveira/zip-manifest-audit) | Inventaria metadados do diretório central de ZIPs sem extrair nem ler os conteúdos dos membros. Relata riscos, mas não certifica a segurança do arquivo. |
| [Casa Aberta — gerador de plantas](https://github.com/martinlofranodeoliveira/gerador-plantas-casas) | Editor local de planta 2D, vista 3D e exportações em medidas métricas. |

<!-- ELEVENTH-BATCH:BEGIN -->
## Pacotes e ensaios nativos · 7 projetos abertos

**Publicado · desenvolvimento 0.1.** Bibliotecas e ferramentas com contratos explícitos, testes nativos, documentação bilíngue e consumo de pacotes conferido fora do código-fonte. Consulte os limites e as execuções de Actions de cada projeto.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Swift Actor Transition Rehearsal](https://github.com/martinlofranodeoliveira/swift-actor-transition-rehearsal) | Swift | Ensaios de transições em atores, com cancelamento, confirmação de etapas e resultados reproduzíveis. | [Docs](https://github.com/martinlofranodeoliveira/swift-actor-transition-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/swift-actor-transition-rehearsal/actions/workflows/ci.yml) |
| [SFTP Generation Publisher](https://github.com/martinlofranodeoliveira/sftp-generation-publisher) | Rust | Publica gerações por SFTP em um servidor próprio, com verificação de arquivos e pontos de confirmação explícitos. | [Docs](https://github.com/martinlofranodeoliveira/sftp-generation-publisher/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/sftp-generation-publisher/actions/workflows/ci.yml) |
| [Gettext Generation Workbench](https://github.com/martinlofranodeoliveira/gettext-generation-workbench) | Ruby | Cria gerações de traduções Gettext, confere arquivos GNU e mantém consultas vinculadas a uma versão. | [Docs](https://github.com/martinlofranodeoliveira/gettext-generation-workbench/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/gettext-generation-workbench/actions/workflows/ci.yml) |
| [Julia Bounded GK Evidence](https://github.com/martinlofranodeoliveira/julia-bounded-gk-evidence) | Julia | Resume fluxos inteiros com limites de recursos e certificados de posição conferidos contra os dados de teste. | [Docs](https://github.com/martinlofranodeoliveira/julia-bounded-gk-evidence/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/julia-bounded-gk-evidence/actions/workflows/ci.yml) |
| [Corpus Font Bundle](https://github.com/martinlofranodeoliveira/corpus-font-bundle) | Python | Produz subconjuntos TTF e WOFF2 para corpus declarado, conferindo composição de glifos e métricas com HarfBuzz. | [Docs](https://github.com/martinlofranodeoliveira/corpus-font-bundle/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/corpus-font-bundle/actions/workflows/ci.yml) |
| [OTP State Upgrade Rehearsal](https://github.com/martinlofranodeoliveira/otp-state-upgrade-rehearsal) | Elixir | Ensaios de troca de código e migração de estado OTP, com recuperação do histórico confirmado em memória. | [Docs](https://github.com/martinlofranodeoliveira/otp-state-upgrade-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/otp-state-upgrade-rehearsal/actions/workflows/ci.yml) |
| [LDAP Membership Evidence Lab](https://github.com/martinlofranodeoliveira/ldap-membership-evidence-lab) | C# | Explica caminhos de grupos LDAP sintéticos, ciclos, referências ausentes e observações incompletas. | [Docs](https://github.com/martinlofranodeoliveira/ldap-membership-evidence-lab/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/ldap-membership-evidence-lab/actions/workflows/ci.yml) |

<!-- ELEVENTH-BATCH:END -->

<!-- TWELFTH-BATCH:BEGIN -->
## Geometria, dados e execução · 6 projetos abertos

**Publicado · desenvolvimento 0.1.0.** Seis bibliotecas e ferramentas com exemplos originais, documentação bilíngue, testes e pacotes conferidos fora do código-fonte. Os contratos descrevem os limites e distinguem resultados completos de execuções inconclusivas.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [Indexed PNG Palette Pack](https://github.com/martinlofranodeoliveira/indexed-png-palette-pack) | C++ | Converte pequenos PNGs RGBA em paletas indexadas, com verificação independente dos pixels e dos limites do formato. | [Docs](https://github.com/martinlofranodeoliveira/indexed-png-palette-pack/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/indexed-png-palette-pack/actions/workflows/ci.yml) |
| [Stratified Permutation Mass](https://github.com/martinlofranodeoliveira/stratified-permutation-mass) | R | Calcula massas combinatórias exatas de somas em atribuições finitas, preservando os totais de cada estrato. | [Docs](https://github.com/martinlofranodeoliveira/stratified-permutation-mass/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/stratified-permutation-mass/actions/workflows/ci.yml) |
| [Parquet Schema Union Rewrite](https://github.com/martinlofranodeoliveira/parquet-schema-union-rewrite) | Python | Reescreve pequenos conjuntos Parquet em um esquema compatível, com proveniência por linha e conferência pelo DuckDB. | [Docs](https://github.com/martinlofranodeoliveira/parquet-schema-union-rewrite/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/parquet-schema-union-rewrite/actions/workflows/ci.yml) |
| [OCaml Regular Path Witness](https://github.com/martinlofranodeoliveira/ocaml-regular-path-witness) | OCaml | Encontra percursos de grafos aceitos por expressões regulares, com testemunhas verificadas e limites explícitos de busca. | [Docs](https://github.com/martinlofranodeoliveira/ocaml-regular-path-witness/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/ocaml-regular-path-witness/actions/workflows/ci.yml) |
| [Rational Halfspace Witnesses](https://github.com/martinlofranodeoliveira/rational-halfspace-witnesses) | Haskell | Resolve pequenos sistemas de desigualdades racionais com pontos ou certificados conferidos separadamente e resultado inconclusivo quando necessário. | [Docs](https://github.com/martinlofranodeoliveira/rational-halfspace-witnesses/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/rational-halfspace-witnesses/actions/workflows/ci.yml) |
| [Wasm Capability Replay](https://github.com/martinlofranodeoliveira/wasm-capability-replay) | Go | Reproduz chamadas de módulos WebAssembly sintéticos, conferindo o histórico e a consistência com a entrada declarada. | [Docs](https://github.com/martinlofranodeoliveira/wasm-capability-replay/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/wasm-capability-replay/actions/workflows/ci.yml) |

<!-- TWELFTH-BATCH:END -->

<!-- THIRTEENTH-BATCH:BEGIN -->
## Junção por similaridade, parsing preditivo, lógica temporal, tensores, geometria, grafos, cinemática 3D, robótica, binários ELF, empacotamento determinístico, cursores JDBC, orçamento geométrico GLB e transições iCalendar · Projetos abertos

**Publicado · desenvolvimento 0.1.0.** Ensaios de ligação JPMS, algoritmos exatos de junção por similaridade, contratos temporais trivalentes, otimização de árvores de tensores, parsing preditivo LL(1), fatiamento exato de malhas com aritmética racional, isomorfismo exato de grafos com refinamento 1-D Weisfeiler-Lehman, cinemática analítica de desdobramento de embalagens 3D em Three.js, bancada educacional de cinemática de braços articulados de 3 juntas rotativas, auditoria de binários ELF com arquivos de depuração auxiliares (.gnu_debuglink) em Zig, empacotador determinístico de releases ZIP em Rust, laboratório empírico de cursores e cancelamento JDBC PostgreSQL em Java 21, auditor de geometria e orçamento de recursos glTF 2.0 Binary (GLB) em C++20 e ensaio de recorrência e transições de fuso horário iCalendar em PHP 8.4.

| Projeto | Linguagem | Finalidade | Consulta |
| --- | --- | --- | --- |
| [JPMS Linkage Rehearsal](https://github.com/martinlofranodeoliveira/jpms-linkage-rehearsal) | Java | Ensaios de ligação JPMS, evolução binária de interfaces, encapsulamento e isolamento de processos no Linux. | [Docs](https://github.com/martinlofranodeoliveira/jpms-linkage-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/jpms-linkage-rehearsal/actions/workflows/ci.yml) |
| [Set Overlap Join](https://github.com/martinlofranodeoliveira/set-overlap-join) | Go | Junção exata em lote por similaridade de Jaccard com indexação por prefixos e verificação inteira exata. | [Docs](https://github.com/martinlofranodeoliveira/set-overlap-join/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/set-overlap-join/actions/workflows/ci.yml) |
| [Temporal Obligation Core](https://github.com/martinlofranodeoliveira/temporal-obligation-core) | PHP | Contratos temporais offline sob Strong Kleene com memoização compacta e operador Until incremental. | [Docs](https://github.com/martinlofranodeoliveira/temporal-obligation-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/temporal-obligation-core/actions/workflows/ci.yml) |
| [Tensor Order Core](https://github.com/martinlofranodeoliveira/tensor-order-core) | C++ | Otimização combinatória exata de árvores binárias de contração de tensores com DP sobre bipartições e aritmética checada em 128 bits. | [Docs](https://github.com/martinlofranodeoliveira/tensor-order-core/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/tensor-order-core/actions/workflows/ci.yml) |
| [Predictive Grammar Kit](https://github.com/martinlofranodeoliveira/predictive-grammar-kit) | Rust | Análise de gramáticas livres de contexto, derivação de FIRST/FOLLOW e parsing preditivo LL(1) bounded em arena. | [Docs](https://github.com/martinlofranodeoliveira/predictive-grammar-kit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/predictive-grammar-kit/actions/workflows/ci.yml) |
| [Mesh Section Loops](https://github.com/martinlofranodeoliveira/mesh-section-loops) | C# | Fatiamento exato de malhas fechadas 2-variedades em polígonos planares 2D com aritmética racional e simplificação colinear. | [Docs](https://github.com/martinlofranodeoliveira/mesh-section-loops/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/mesh-section-loops/actions/workflows/ci.yml) |
| [Colored Graph Witness](https://github.com/martinlofranodeoliveira/colored-graph-witness) | Kotlin | Isomorfismo exato de grafos pequenos direcionados e rotulados com refinamento 1-D Weisfeiler-Lehman e busca com retrocesso. | [Docs](https://github.com/martinlofranodeoliveira/colored-graph-witness/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/colored-graph-witness/actions/workflows/ci.yml) |
| [Carton Hinge Studio](https://github.com/martinlofranodeoliveira/carton-hinge-studio) | TypeScript | Cinemática analítica de desdobramento de embalagens retangulares em 3D (Three.js), convergência de junções e exportação de faca de corte em SVG. | [Docs](https://github.com/martinlofranodeoliveira/carton-hinge-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/carton-hinge-studio/actions/workflows/ci.yml) |
| [Reach Branch Studio](https://github.com/martinlofranodeoliveira/reach-branch-studio) | TypeScript | Cinemática analítica de braço robótico com 3 juntas rotativas (Three.js), enumeração de ramos de cotovelo, alternativas radiais e rejeição por limites articulares. | [Docs](https://github.com/martinlofranodeoliveira/reach-branch-studio/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/reach-branch-studio/actions/workflows/ci.yml) |
| [Debuglink Companion Audit](https://github.com/martinlofranodeoliveira/zig-debuglink-companion-audit) | Zig | Auditor de binários ELF e arquivos de depuração auxiliares (.gnu_debuglink) com verificação de CRC32 IEEE 802.3, interoperabilidade libelf e barreiras contra TOCTOU. | [Docs](https://github.com/martinlofranodeoliveira/zig-debuglink-companion-audit/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/zig-debuglink-companion-audit/actions/workflows/ci.yml) |
| [Reproducible ZIP Release Packer](https://github.com/martinlofranodeoliveira/rust-reproducible-zip-release) | Rust | Empacotador delimitado de releases para arquivos próprios com bytes ZIP estáveis sob compressão fixada, concessão cooperativa de fontes e publicação atômica via linkat. | [Docs](https://github.com/martinlofranodeoliveira/rust-reproducible-zip-release/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/rust-reproducible-zip-release/actions/workflows/ci.yml) |
| [JDBC Cursor & Cancellation Rehearsal](https://github.com/martinlofranodeoliveira/java-jdbc-cursor-rehearsal) | Java | Laboratório de cursores no servidor PostgreSQL, consumo delimitado, inspeção de portais em pg_cursors e cancelamento de buscas via PGConnection. | [Docs](https://github.com/martinlofranodeoliveira/java-jdbc-cursor-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/java-jdbc-cursor-rehearsal/actions/workflows/ci.yml) |
| [GLB Geometry Budget](https://github.com/martinlofranodeoliveira/cpp-glb-geometry-budget) | C++ | Auditor delimitado de geometria e orçamento de recursos para arquivos glTF 2.0 Binary (GLB) em C++20 com alocador seguro, transformações em dupla precisão e oráculo Khronos. | [Docs](https://github.com/martinlofranodeoliveira/cpp-glb-geometry-budget/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/cpp-glb-geometry-budget/actions/workflows/ci.yml) |
| [iCalendar Transition Rehearsal](https://github.com/martinlofranodeoliveira/php-ical-transition-rehearsal) | PHP | Motor de ensaio de recorrência iCalendar (RFC 5545) com Sabre VObject, resolução física de instantes UTC, políticas para lacunas e dobras e oráculo zdump. | [Docs](https://github.com/martinlofranodeoliveira/php-ical-transition-rehearsal/blob/main/README.pt-BR.md) · [Actions](https://github.com/martinlofranodeoliveira/php-ical-transition-rehearsal/actions/workflows/ci.yml) |

<!-- THIRTEENTH-BATCH:END -->
