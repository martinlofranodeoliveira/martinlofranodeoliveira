# Evidências técnicas dos projetos abertos

Este registro reúne o código público original produzido pela [Lofrano Tecnologia](https://lofranotecnologia.com.br), com documentação, testes e exemplos locais. As versões e os estados de desenvolvimento variam por projeto. Consulte a finalidade, a versão e os limites de cada um no [catálogo](PROJETOS-ABERTOS.md).

<!-- EVIDENCE-QUESTIONS-2026-11-08:BEGIN -->
## Banco de Questões · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/banco-de-questoes/tree/1dcba99e29be614bbe3651011ca30e8e40265641), licença MIT, biblioteca/CLI Python 3.11+ e documentação em português. Pillow 13.0.0 é a dependência de execução; o uso funciona offline após a instalação, sem conexão ao LMS.
- 61 testes passaram em cada um dos cinco jobs de testes/distribuição da [CI desse commit](https://github.com/martinlofranodeoliveira/banco-de-questoes/actions/runs/42542138739): Python 3.11–3.14 no Linux e 3.14 no Windows, sem omissões. Todos construíram wheel/sdist, conferiram 36 arquivos públicos e dez arquivos de runtime e exercitaram o wheel instalado fora da árvore de fontes. O sexto job aprovou a integração com Moodle real e confirmou a limpeza dos recursos.
- O contrato aceita JSON v1 com campos fechados, rejeita chaves repetidas e valores inválidos e representa cinco modelos: escolha simples, escolha múltipla, verdadeiro/falso, resposta curta e numérica. Percentuais são explícitos; os pesos não são redistribuídos. Os diagnósticos usam localização lógica, sem repetir enunciados, respostas ou caminhos absolutos.
- A [evidência reproduzível](https://github.com/martinlofranodeoliveira/banco-de-questoes/blob/1dcba99e29be614bbe3651011ca30e8e40265641/tests/integration/evidence.json) registra aprovação no Moodle 4.5.15+ (Build: 20261030), commit `c0690bbc765fccacd4956452cbff3f6aacad77c5`, com PHP 8.3.36 e PostgreSQL 17.10. O consumidor real importa oito questões, carrega os modelos persistidos e corrige 30 respostas com `grade_response()` e tentativas do `question_engine`, persistidas e recarregadas. Frações são comparadas com tolerância absoluta de 0,000001 na escala 0–1.
- Foram comparados IDs, modelos, nomes, categorias, textos, notas, penalidades, tags, alternativas/padrões, frações, feedbacks, tolerâncias, caixa, embaralhamento e referência/nome/MIME/alt/bytes da imagem PNG. A exportação pelo Moodle foi reimportada num segundo curso com igualdade dos snapshots persistidos, incluindo a imagem. A tabela de 41 percentuais foi confrontada com `question_bank::fraction_options_full()`.
- Probes separados confirmaram remoção de espaços externos em nomes e padrões de resposta curta, normalização de penalidade de `0.334` para `0.3333333` e limpeza, descarte e união de tags. A resposta normalizada também foi corrigida pelo Moodle. Um contraexemplo com o parser oficial mostrou descarte de CR e conversão de CRLF para LF; por isso o validador recusa CR/CRLF em padrões de resposta curta. LF e TAB internos permaneceram aceitos e foram preservados pelo parser nos probes. Esses contraexemplos não são registrados como importações fiéis de questões com CR.
- O pacote inclui Moodle XML, cadernos HTML docente e aluno, relatórios JSON/Markdown, orientação de uso e manifesto com SHA256 e tamanho dos seis outros arquivos. XML e caderno docente incluem gabaritos por finalidade. O caderno aluno omite a seção de respostas e feedback, preservando enunciados e alternativas; HTML é estático, sem scripts, formulários ou rede. Não há gerador próprio de PDF.
- A integração usa dados fictícios, fonte e imagens fixadas por hash, rede Docker interna e nenhuma porta publicada. A evidência registra limpeza dos recursos ao fim da execução, com limites totais de 2 GiB e 2 CPUs. O Moodle é baixado separadamente e não integra o pacote MIT. A conferência tem o escopo da versão fixada e dos casos documentados; não certifica todas as versões, plugins, bancos possíveis ou configurações de avaliação.
- Os cadernos de exemplo foram carregados em navegador nas larguras de 1280 px (docente) e 390 px (aluno), com as oito questões e a imagem, sem overflow horizontal ou erros de console observados. A impressão/PDF depende das opções do navegador e não integrou essa verificação.
- [Release e checksums](https://github.com/martinlofranodeoliveira/banco-de-questoes/releases/tag/v1.0.0): os seis assets públicos — wheel, sdist, `banco-exemplo.zip`, `docente-exemplo.html`, `aluno-exemplo.html` e `SHA256SUMS` — foram baixados novamente. Os cinco arquivos listados em `SHA256SUMS` tiveram seus hashes conferidos e corresponderam byte a byte aos artefatos preparados; o manifesto interno do ZIP também foi validado.

<!-- EVIDENCE-QUESTIONS-2026-11-08:END -->

## Roteiro de Vídeo · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/roteiro-de-video/tree/2c87c5d103d5fc0070ae8ae26364e9fb6faa8e96), licença MIT e documentação em português. Planejador estático HTML/CSS/JavaScript para até 40 cenas, sem conta nem salvamento automático.
- 56 testes passaram em cada job Node.js 22/24 da [CI desse commit](https://github.com/martinlofranodeoliveira/roteiro-de-video/actions/runs/42538258436).
- A narrativa preserva os números das cenas quando a ordem de gravação é agrupada por local e setup. Durações usam milissegundos inteiros e distinguem o tempo informado das cenas pendentes.
- O projeto JSON inclui as imagens normalizadas. Há exportação Markdown e CSV e impressão pelo diálogo nativo do navegador; os dados de edição permanecem locais.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/roteiro-de-video/actions/runs/42538258548) aprovado no mesmo código; os 20 arquivos públicos conferidos por HTTP corresponderam byte a byte à distribuição estática de 21 arquivos. O marcador `.nojekyll` foi conferido apenas dentro do ZIP estático.
- Na [demonstração pública](https://martinlofranodeoliveira.github.io/roteiro-de-video/), um projeto com seis imagens normalizadas foi carregado e exportado como JSON com bytes idênticos ao exemplo validado. A ordem de gravação ficou em 1, 3, 4, 2, 5 e 6, preservando os números narrativos. Não foram observados erros de console nem overflow horizontal na largura exercitada.
- [Release e checksums](https://github.com/martinlofranodeoliveira/roteiro-de-video/releases/tag/v1.0.0): os ZIPs de fontes e distribuição estática e o arquivo SHA256SUMS foram baixados da publicação. Os hashes dos dois ZIPs foram validados; os 45 arquivos de fontes corresponderam ao commit indicado e os 21 arquivos estáticos à distribuição preparada. A [CI da tag](https://github.com/martinlofranodeoliveira/roteiro-de-video/actions/runs/42538461370) também passou no mesmo código.

## Extrato OFX · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/extrato-ofx/tree/11e803c78d15fa821f653902ecf031f200d3a2d2), licença MIT, biblioteca/CLI e documentação em português. O perfil bancário/cartão interpreta OFX1 SGML e OFX2 XML, sem conexão bancária, reconciliação ou aplicação de correções.
- 104 testes na suíte da [CI desse commit](https://github.com/martinlofranodeoliveira/extrato-ofx/actions/runs/42531636608), com Python 3.11–3.14 no Linux e 3.14 no Windows. No Windows, somente o teste de broken pipe é omitido. Todos os cinco jobs constroem a distribuição e exercitam o wheel instalado em um ambiente novo fora dos fontes.
- A comparação opcional com ofxtools 1.1.1 confronta 22 variantes de extratos fictícios com projeções de campos e expectativas escritas à mão. Três diferenças conhecidas ficam separadas: rejeição de offset 5.5 pelo oráculo, interpretação divergente de 5.50 e rejeição de VERSION 221. Não se declara conformidade integral com OFX.
- Valores e somas usam coeficientes inteiros e escalas, com testes por Fraction e independência do contexto Decimal. Datas preservam precisão e usam horas decimais para o offset. Duplicatas permanecem no relatório, agrupadas por conta; diferenças de moeda ou conteúdo interpretado geram conflito.
- A revisão independente exercitou 10.000 mutações determinísticas de entradas SGML/XML e reproduziu problemas em relatórios alterados pelo chamador. As regressões corrigem tipos inválidos de status, fórmulas em colunas numéricas e conteúdo de Markdown. Os pontos revisados foram revalidados sem pendências.
- Um arquivo sintético com 10.000 transações e 2.180.909 bytes foi interpretado e exportado nos três formatos, mantendo a soma exata de -899000. Isso verifica esse caso local; não constitui medição universal de desempenho ou memória.
- [Release e checksums](https://github.com/martinlofranodeoliveira/extrato-ofx/releases/tag/v1.0.0): wheel instalável, sdist e ZIP com 40 arquivos rastreados foram baixados da publicação e conferidos por SHA-256 contra o manifesto. Os fontes do ZIP e os nove módulos do wheel corresponderam ao commit. A [CI da tag](https://github.com/martinlofranodeoliveira/extrato-ofx/actions/runs/42531768464) também passou nos cinco jobs. Os exemplos são inteiramente fictícios; relatórios reais continuam contendo dados financeiros privados.

## Folha de Contato · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/folha-de-contato/tree/4223c61abd91b75a42cec326b2b3303c4d009c3f), licença MIT e documentação em português, com instruções para publicar e adaptar um fork. A organização Mesa de edição e a implementação estática foram confirmadas pelo usuário.
- 62 testes passaram em cada job Node.js 22/24 da [CI desse commit](https://github.com/martinlofranodeoliveira/folha-de-contato/actions/runs/42527098441), sem omissões. Incluem modelo imutável, limites UTF-8/bytes/pixels, preços com centavos inteiros, 120 combinações de formato/orientação/grade e matrizes de enquadramento nas quatro rotações. O SVG é confrontado com o parser XML independente ElementTree.
- A revisão funcional reproduziu e corrigiu caracteres Unicode que invalidavam o SVG, nomes cortados sem elipse, reentrada de callbacks e leituras antigas substituindo edições recentes. Três regressões do controlador usam o app real com DOM mínimo: preço em edição preservado quando o exemplo falha, texto visível igual ao arquivo salvo e confirmação somente quando há conteúdo a substituir.
- No navegador, um backup com seis produtos foi restaurado e reexportado preservando os 3.675.012 bytes, inclusive após remover e desfazer a remoção de um item. Foram conferidos preço zero e preço ausente, mudança de ordem, rotação e paginação. Projeto com PNG corrompido e lote de fotos com um arquivo inválido preservaram o catálogo aberto.
- PNG e SVG baixados foram verificados com Pillow e ElementTree; o SVG correspondeu exatamente ao renderizador. A orientação EXIF 6 de uma imagem JPEG sintética produziu um PNG de 96 × 128 px, com os pixels orientados esperados. O PNG de demonstração contém os seis produtos e seus centros foram comparados às imagens normalizadas.
- Revisão visual independente de desktop e celular apontou que a sequência ficava fora da primeira tela em 1280 × 720. Após corrigir o espaço vertical, o revisor pontuou esse ajuste como resolvido: folha, campos principais e os seis produtos ficaram visíveis juntos. Capturas móveis de retrato e de folha em paisagem também foram conferidas. O detector operou com parsers indisponíveis; não certificou contraste calculado.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/folha-de-contato/actions/runs/42527098370) aprovado no mesmo código; 18 arquivos HTTP, incluindo manifesto, módulos, estilos, fontes e imagens, corresponderam byte a byte à distribuição. O JSON do exemplo baixado do site público preservou os 3.675.002 bytes da cópia local correspondente. O marcador `.nojekyll` foi conferido dentro do ZIP estático.
- [Release e checksums](https://github.com/martinlofranodeoliveira/folha-de-contato/releases/tag/v1.0.0): ZIP com 44 arquivos de fontes, ZIP estático com 19 arquivos e PNG de exemplo foram baixados da release pública e verificados por SHA-256. A [CI da tag](https://github.com/martinlofranodeoliveira/folha-de-contato/actions/runs/42527513952) também passou nos dois jobs com o mesmo commit.

## Recorrência Civil · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/recorrencia-civil/tree/26a224fb69be7f9b444ec1c5144bafcebf6c8acc), licença MIT, biblioteca/CLI e documentação em português. O contrato declara um perfil DATE da RFC 5545, sem conformidade integral iCalendar ou execução de agendas.
- 75 testes passaram em cada um dos cinco jobs da [CI desse commit](https://github.com/martinlofranodeoliveira/recorrencia-civil/actions/runs/42520927671): Python 3.11–3.14 no Ubuntu e 3.14 no Windows, sem omissões da suíte. Cada job construiu o pacote e instalou o wheel em um ambiente novo fora da árvore de fontes, sem dependências de runtime.
- A comparação independente com `python-dateutil==4.0.0` coincidiu em 289 cenários, com 8.109 ocorrências comparadas e 72 partições de janelas inclusivas. Uma divergência na seleção `BYSETPOS` da primeira semana foi reproduzida separadamente, com discussão e proposta upstream documentadas; ela não é contabilizada como comparação aprovada. O [resumo reproduzível](https://github.com/martinlofranodeoliveira/recorrencia-civil/blob/26a224fb69be7f9b444ec1c5144bafcebf6c8acc/examples/oraculos.json) registra entradas e resultados.
- Os testes cobrem sincronização de DTSTART, contagem antes de exclusões e janela, RDATE independente de COUNT/UNTIL, períodos completos antes de BYSETPOS, anos 0001 e 9999, orçamentos zero, prefixos comprovados e limites exatos de entrada. A revisão independente confrontou ainda 42 casos de consultas parciais com suas expansões completas, sem encontrar novas divergências nesses casos.
- A primeira execução no Windows revelou tradução das quebras de linha de stdout. A correção emite UTF-8 pelo buffer binário; uma regressão reproduz o wrapper com CRLF também no Linux. A instalação verificada compara os três formatos byte a byte com a API instalada e analisa CSV de stdout e arquivo com parser independente. Destinos existentes e criados durante a publicação são preservados.
- [Release e checksums](https://github.com/martinlofranodeoliveira/recorrencia-civil/releases/tag/v1.0.0): wheel, sdist e ZIP de fontes foram baixados da release pública e verificados por SHA-256. Os oito módulos do wheel, os 36 arquivos rastreados incluídos no sdist e os 39 arquivos do ZIP corresponderam ao código indicado. O wheel baixado foi instalado em ambiente separado e conferido nos três formatos, com limite parcial e publicação exclusiva.

## Pauta Aberta · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/pauta-aberta/tree/45cd2d4845ba6fd0dbe5a9df60f38559d50ac51d), licença MIT, documentação em português, contrato e exemplos sintéticos.
- 103 testes passaram em cada job Node.js 22/24 da [CI desse commit](https://github.com/martinlofranodeoliveira/pauta-aberta/actions/runs/42517233074), sem omissões. Cobrem limite UTF-8 exato de 2 MiB, snapshots independentes, vínculos, datas civis, importação integral, transações IndexedDB e revisões monotônicas contra conflitos. Markdown e CSV foram confrontados com parsers independentes.
- A revisão funcional reproduziu duas corridas: notas digitadas após abrir a confirmação da ata e uma leitura antiga de arquivo substituindo uma prévia mais recente. As correções e três regressões passaram na mesma CI. Rascunhos de formulário são preservados em memória e não são apresentados como dados já salvos.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/pauta-aberta/actions/runs/42517233124) aprovado; 14 arquivos públicos, incluindo HTML, módulos, estilos, fontes e avisos de licença, foram comparados byte a byte com a distribuição preparada. O marcador `.nojekyll` foi conferido apenas dentro do ZIP estático.
- Na prévia local, um backup com 1 reunião, 3 pontos, 1 decisão, 2 ações e 2 atas foi restaurado e reexportado preservando os 7.413 bytes. O Markdown histórico e o CSV baixados corresponderam aos exportadores; a versão 1 permaneceu intacta após editar a ficha e gerar a versão 2. O caderno salvo foi recuperado após recarga. Na demonstração pública, o backup do exemplo preservou os 4.779 bytes do gerador canônico.
- Revisão visual independente de pauta, ata e encaminhamentos em desktop e celular: disposição `ship`, sem correções materiais exigidas. A largura móvel de 390 px permaneceu sem overflow; a captura pública na largura disponível de 1.010 px também foi conferida. O detector mecânico operou com parsers indisponíveis, portanto não certificou contraste ou seletores.
- [Release e checksums](https://github.com/martinlofranodeoliveira/pauta-aberta/releases/tag/v1.0.0): os ZIPs de fontes e distribuição estática foram baixados da release pública e verificados por SHA-256; seus 39 e 15 arquivos, respectivamente, corresponderam aos arquivos preparados. A [CI da tag](https://github.com/martinlofranodeoliveira/pauta-aberta/actions/runs/42517454695) também foi aprovada no mesmo código.

## EPUB Navigation Audit · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/epub-navigation-audit/tree/24e4cb5bf6a57ce6762adcccaff2d73ecf28f2fe), licença MIT, biblioteca/CLI e documentação em português.
- [CI do mesmo commit](https://github.com/martinlofranodeoliveira/epub-navigation-audit/actions/runs/42477675035) aprovada em cinco jobs de distribuição: Python 3.11–3.14 no Ubuntu e 3.14 no Windows. Cada job executou a suíte de 105 testes, construiu o pacote e exercitou o wheel instalado fora da árvore de fontes. Há uma omissão específica de FIFO no Windows.
- Os testes cobrem leitura ZIP limitada, headers e CRC contraditórios, XML sem entidades externas, limites globais, normalização Unicode, XHTML/SVG, seleção de rendição, privacidade dos relatórios e saída sem sobrescrita. A CI revelou diferenças de Windows no gerador de um ZIP com barra invertida e na classificação de diretórios; ambas foram corrigidas antes da release.
- O sexto job confrontou os [12 EPUBs sintéticos originais](https://github.com/martinlofranodeoliveira/epub-navigation-audit/blob/main/scripts/make_samples.py) com EPUBCheck 5.3.0, cujo arquivo oficial é verificado por SHA-256. Inclui casos válidos, falhas conhecidas e recursos legítimos fora do perfil próprio. O helper de URLs contém 18 casos, com 14 resoluções locais comparadas ao WHATWG URL do Node.js e quatro referências fora do perfil local.
- A [CI adicional da tag](https://github.com/martinlofranodeoliveira/epub-navigation-audit/actions/runs/42477787417) passou nos cinco jobs de distribuição, mas o download externo do EPUBCheck excedeu o timeout, inclusive em uma repetição apenas desse job. O confronto completo do mesmo commit permanece comprovado na CI principal acima; a execução adicional da tag não está registrada como aprovada.
- [Relatórios de exemplo](https://github.com/martinlofranodeoliveira/epub-navigation-audit/tree/main/examples) registram estados e cobertura separadamente. O confronto com EPUBCheck corrigiu um falso diagnóstico de caminhos Unicode equivalentes. Um livro consistente neste perfil não é certificado como integralmente conforme ou seguro para execução.
- [Release e checksums](https://github.com/martinlofranodeoliveira/epub-navigation-audit/releases/tag/v1.0.0): wheel, sdist e ZIP de fontes foram baixados da release pública e verificados por SHA-256. Os dez módulos do wheel e os 36 arquivos do ZIP correspondem ao código indicado; o wheel baixado foi instalado em ambiente separado e conferiu os doze casos, a seleção explícita e a interrupção por limite.

## Decisões Abertas · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/decisoes-abertas/tree/b8daa0b35a5c4d5d3d501395c950a7f4836f3b2d), licença MIT, documentação em português e exemplos sintéticos.
- 93 testes passaram em cada job Node.js 22/24 da [CI desse commit](https://github.com/martinlofranodeoliveira/decisoes-abertas/actions/runs/42473656383), sem omissões. Cobrem cálculo inteiro, notas ausentes e zero, pesos inativos, empates, snapshots, importação integral, geração de prévias e concorrência de salvamento com controle de revisão.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/decisoes-abertas/actions/runs/42473656386) aprovado; nove assets públicos e dois avisos de licença foram comparados byte a byte com o código e os recursos locais. A demonstração pública exibiu os resultados fictícios 80,0%, 81,0% e 79,0%.
- Fluxo real no navegador: nota ausente removeu o ranking, nota zero foi contabilizada e peso zero desativou o critério. Uma escolha diferente da primeira colocada foi salva, registrada em histórico e reaberta após recarga com o salvamento opcional.
- Um backup com 1 comparação, 3 alternativas, 4 critérios e 2 registros foi restaurado e reexportado sem alterar bytes. CSV e Markdown histórico baixados também corresponderam às exportações esperadas; o relatório histórico manteve uma escolha diferente da matriz corrente.
- Revisão desktop/celular identificou três correções materiais: largura com oito alternativas, contexto dos critérios no celular e continuidade do foco. A revisão das recapturas pontuou os três itens como resolvidos. A medição de oito alternativas encontrou 32 seletores sem sobreposição, com rolagem apenas dentro da tabela; a versão móvel permaneceu sem overflow horizontal.
- [Release e checksums](https://github.com/martinlofranodeoliveira/decisoes-abertas/releases/tag/v1.0.0): os ZIPs de código-fonte e versão estática foram baixados da release pública e verificados por SHA-256. Os 40 arquivos do ZIP de fontes e 14 da distribuição estática corresponderam aos arquivos preparados, incluindo os avisos MIT e OFL.

## SQLite Catalog Report · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/tree/2becdce860ccf25ff6699bea592d65ce6aaca47b), licença MIT, API/CLI e documentação em português.
- [CI do mesmo commit](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/actions/runs/42470742835) aprovada em cinco jobs: Python 3.11, 3.12, 3.13 e 3.14 no Ubuntu; Python 3.14 no Windows. Cada job executou 81 testes, sem omissões, construiu a distribuição e instalou o wheel fora da árvore de fontes.
- Os testes cobrem snapshot WAL com alteração concorrente de esquema, leitura somente de metadados, limites globais, relações compostas, ciclos longos, escaping e publicação de relatórios sem sobrescrita. Valores canários dos registros sintéticos permanecem ausentes dos três formatos.
- A revisão independente identificou e resolveu classificação incompleta de shadows, índices ainda não detalhados marcados como completos e falha de pipe no encerramento da CLI. A CI também revelou duas incompatibilidades de Windows no gerador e no nome de arquivo do teste, corrigidas antes da release.
- [Exemplos](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/tree/main/examples) incluem esquema sintético e saídas JSON/Markdown/Mermaid. A apresentação foi conferida adicionalmente com os parsers Mermaid 12.3.0 e Markdown-it 14.1.0 usando nomes e SQL com caracteres de formatação, sem injeção de nós, links ou elementos HTML.
- [Release e checksums](https://github.com/martinlofranodeoliveira/sqlite-catalog-report/releases/tag/v1.0.0): wheel, sdist e ZIP de fontes foram baixados da release pública e conferidos por SHA-256. Os oito módulos no wheel e os 29 arquivos do ZIP correspondem ao código indicado; o wheel baixado foi instalado e exercitado em ambiente temporário separado.

## Wheel Record Audit · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/wheel-record-audit/tree/f7a87e3068ab97a140931c02a5d568eaeb50e568), licença MIT, API/CLI e documentação em português.
- [CI do mesmo commit](https://github.com/martinlofranodeoliveira/wheel-record-audit/actions/runs/42468166025) aprovada em cinco jobs: Python 3.11, 3.12, 3.13 e 3.14 no Ubuntu; Python 3.14 no Windows. Cada job executa a suíte de 133 testes; no Windows há uma omissão específica de FIFO, recurso indisponível nesse ambiente.
- Todos os jobs constroem a distribuição, instalam o wheel em um ambiente virtual temporário fora do código-fonte e exercitam a CLI, o caso sintético válido, o adulterado e a auditoria do próprio wheel.
- A revisão independente reproduziu três grupos de falhas estruturais em 11 arquivos sintéticos. A revalidação confirmou a recusa dos cabeçalhos/descritores/diretórios contraditórios e o bloqueio de EOCD ambíguo antes de criar objetos ZipInfo.
- [Relatórios de exemplo](https://github.com/martinlofranodeoliveira/wheel-record-audit/tree/main/examples) registram conteúdos fictícios. O perfil, os limites e as distinções entre `consistent`, `invalid` e `incomplete` estão documentados.
- [Release e checksums](https://github.com/martinlofranodeoliveira/wheel-record-audit/releases/tag/v1.0.0): wheel instalável, sdist, ZIP dos fontes e relatório da auditoria do próprio wheel, com 12 arquivos e seus tamanhos/hashes confirmados.

## Caderno de Revisões · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/caderno-revisoes/tree/5ab7d570d5c99486b018ee21359031c6f2757e75), licença MIT e documentação em português, com arquivos de exemplo para importar.
- 80 testes passaram no [workflow Node.js 22/24](https://github.com/martinlofranodeoliveira/caderno-revisoes/actions/runs/42465613140), no mesmo commit. Incluem regras de intervalo, datas, versões, limites, importação atômica, conflitos IndexedDB e regressões de interface.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/caderno-revisoes/actions/runs/42465613119) concluído; os quatro módulos JavaScript e o CSS públicos foram conferidos por SHA256 contra esse código.
- [Demonstração](https://martinlofranodeoliveira.github.io/caderno-revisoes/) exercitada no navegador: restauração e reexportação de backup fictício (2 baralhos, 6 cartões, 5 avaliações) preservaram todos os bytes. Depois de importar dois cartões CSV e registrar uma avaliação, o backup resultante válido contém 8 cartões e 6 avaliações; a revisão foi agendada para 09/11/2026 conforme a regra.
- Revisão visual em desktop (viewport 1280 × 720) e celular (390 × 844), cobrindo fila com prática inline, biblioteca, histórico e backup. Os ajustes de barra de rolagem e sua adaptação móvel foram pontuados como resolvidos. Salvamento e recuperação após recarga também foram exercitados na prévia local.
- [Download da versão e checksum](https://github.com/martinlofranodeoliveira/caderno-revisoes/releases/tag/v1.0.0).

## Garantia Aberta · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/garantia-aberta/tree/117e6261ac596e0e5d99dd09feaa70c11e7be90d), licença MIT e documentação em português.
- 75 testes passaram no [workflow Node.js 22/24](https://github.com/martinlofranodeoliveira/garantia-aberta/actions/runs/42461183329), no mesmo commit. Incluem limites do backup, integridade dos anexos, concorrência entre conexões IndexedDB e regressões de interface.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/garantia-aberta/actions/runs/42461183339) concluído; os cinco módulos JavaScript e o CSS públicos foram conferidos por SHA256 contra esse código.
- [Demonstração](https://martinlofranodeoliveira.github.io/garantia-aberta/) exercitada no navegador com backup fictício: 3 bens e 1 PDF. Restauração e reexportação preservaram o livro completo; o PDF baixado preservou os 693 bytes do arquivo original.
- Revisão visual em desktop (viewport 1280 × 720) e celular (390 × 844), incluindo inventário vazio, fichas, documentos, agenda, backup e cadastro. Salvamento e recuperação entre visitas também exercitados na prévia local.
- [Download da versão e checksum](https://github.com/martinlofranodeoliveira/garantia-aberta/releases/tag/v1.0.0).

## Orçamento Aberto · 8 de novembro de 2026

- [Código da versão 1.0.0](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/tree/5ac25f885ede16fff75e52a339f2d1d2e8817c5d), licença MIT e documentação em português.
- 47 testes passaram no [workflow Node.js 22/24](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/actions/runs/42457496754), no mesmo commit.
- [Deploy do GitHub Pages](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/actions/runs/42457496792) concluído; JavaScript principal e CSS públicos conferidos por SHA256 contra o código dessa versão.
- [Demonstração](https://martinlofranodeoliveira.github.io/lofrano-orcamentos-open/) conferida no navegador: cálculo fracionado, desconto e adicional totalizando R$ 15,52; exemplo fictício totalizando R$ 2.700,00.
- Revisão visual em desktop (viewport 1055 × 900) e celular (390 × 844). Salvamento opcional, recuperação do rascunho e download JSON também exercitados na prévia local.
- [Download da versão e checksum](https://github.com/martinlofranodeoliveira/lofrano-orcamentos-open/releases/tag/v1.0.0).

## Consultar uma versão

O [snapshot JSON](evidencias/portfolio-snapshot.json) registra a identidade de cada repositório, seu commit, horário da consulta, presença de arquivos de documentação, inventário de workflows e execuções de GitHub Actions daquele commit. Os dados foram consultados na API pública do GitHub. A data `evaluated_at_utc` identifica esta coleta; ela não se atualiza quando o arquivo é aberto.

Para conferir uma implementação:

1. Abra o repositório pelo catálogo e consulte o commit indicado em `source_sha`.
2. Leia o README e o contrato nessa versão; siga os comandos de preparação, testes e demo documentados.
3. Compare o SHA da execução em Actions com o commit examinado. Execuções antigas ou de outro commit não comprovam o estado da versão atual.
4. Examine também as limitações, os casos negativos e as dependências declaradas.

## Inspecionar no painel

Baixe o JSON e abra o [GitHub Evidence Board](https://martinlofranodeoliveira.github.io/github-evidence-board/). Use **Open local UTF-8 JSON** e **Apply snapshot**.

O arquivo é identificado como evidência importada: o painel mostra `unverified_offline` até uma consulta explícita à API. No detalhe de um repositório, **Refresh this repository from GitHub** consulta os dados públicos atuais sem pedir credenciais. Exportar e importar o resultado novamente não preserva a autenticação da sessão. A consulta pode ser limitada pelo GitHub.

O snapshot utiliza TTL de 24 horas em relação ao horário de avaliação informado. O núcleo offline usa tempo explícito; para avaliar uma coleta antiga no horário atual, informe esse horário ou atualize os dados pela API. `complete: false` identifica uma enumeração incompleta e impede concluir que todos os workflows passaram.

## Alcance desta evidência

O material demonstra implementações, documentação e verificações públicas. Contratos com clientes, atestados de execução comercial e habilitação em licitações precisam de seus próprios documentos; este catálogo não os declara.

Os registros de cada entrega indicam o alcance da conferência HTTP, da revisão visual e dos testes de interação. O snapshot geral e os arquivos DESIGN.md devem ser lidos com sua data e escopo próprios. Presença de licença, README ou política de segurança registra existência, sem certificar seu conteúdo.
