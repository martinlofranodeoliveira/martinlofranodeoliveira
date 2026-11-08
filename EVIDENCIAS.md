# Evidências técnicas dos projetos abertos

Este registro reúne o código público original produzido pela [Lofrano Tecnologia](https://lofranotecnologia.com.br), com documentação, testes e exemplos locais. As versões e os estados de desenvolvimento variam por projeto. Consulte a finalidade, a versão e os limites de cada um no [catálogo](PROJETOS-ABERTOS.md).

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
