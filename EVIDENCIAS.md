# Evidências técnicas dos projetos abertos

Este registro reúne o código público original produzido pela [Lofrano Tecnologia](https://lofranotecnologia.com.br), com documentação, testes e exemplos locais. Os projetos estão em desenvolvimento 0.1.0. Consulte a finalidade e os limites de cada um no [catálogo](PROJETOS-ABERTOS.md).

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

As demos web publicadas tiveram os arquivos e tipos HTTP conferidos contra o código revisado. A revisão visual e de acessibilidade em navegador permanece pendente, conforme os arquivos DESIGN.md dos projetos. Presença de licença, README ou política de segurança registra existência, sem certificar seu conteúdo.
