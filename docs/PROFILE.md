# Perfil LOFRANO TECNOLOGIA

## Identidade e referências

O perfil apresenta Martin Lofrano e a LOFRANO TECNOLOGIA, com foco em software sob medida, IA, automação e integrações. O site oficial é a referência para a oferta e os links: https://lofranotecnologia.com.br.

A coleção https://github.com/topics/awesome-github-profiles e os perfis `trinib/trinib`, `walidbosso/walidbosso` e `supuna97/supuna97` serviram de inspiração para a organização em banners, cards e métricas. Os textos, a composição visual, os desenhos SVG e o gerador de métricas deste perfil foram criados para a LOFRANO; os assets dos outros perfis não foram reutilizados.

## Assets

- `assets/lofrano-hero.jpg`: versão JPEG otimizada do banner original gerado com a ferramenta nativa de geração de imagens, 2172 × 724 px. A composição e as dimensões foram preservadas; o PNG original foi mantido como fonte da arte.
- `assets/focus-strip.svg`: faixa de identidade com animação decorativa discreta e suporte a redução de movimento.
- `assets/studio-card.svg` e `assets/headquarters-card.svg`: atalhos visuais para o Estúdio LOFRANO e a sede 3D.
- `assets/stack.svg`: tecnologias declaradas no perfil, sem representar notas de domínio.
- `assets/github-metrics.svg` e `assets/github-languages.svg`: imagens geradas com dados consultados no GitHub.

### Direção do banner

Banner editorial original e panorâmico, proporção 3:1, preto, branco e rosa. Tipografia grande à esquerda com os textos exatos “LOFRANO TECNOLOGIA”, “Software sob medida.”, “Inteligência aplicada.” e “MARTIN LOFRANO · FULL STACK DEVELOPER”. À direita, microarquitetura futurista abstrata de vidro e titânio, núcleo de luz rosa e trajetórias ópticas conectando módulos. Iluminação cinematográfica suave, reflexos físicos e margens generosas. Sem números, status operacionais, marcas externas ou elementos copiados.

## Atualização das métricas

O workflow `Métricas do perfil` consulta o GitHub e atualiza os dois painéis diariamente às 09:23 UTC, equivalentes a 06:23 em São Paulo. Também pode ser executado manualmente na aba Actions e roda quando seu script, testes ou configuração são alterados. A execução agendada pode começar depois do horário previsto, conforme a disponibilidade do GitHub.

O script usa Python 3.11 ou posterior, somente a biblioteca padrão e o `GITHUB_TOKEN` automático do repositório. Nenhuma credencial precisa ser adicionada ao README.

O calendário segue as contribuições visíveis retornadas pelo GitHub, inclusive contagens anônimas de atividade privada quando o usuário opta por torná-las públicas. Dias ativos e maior sequência são calculados pelas datas desse calendário. As linguagens usam bytes classificados pelo GitHub somente em repositórios próprios, públicos e sem forks. Não representam nível de domínio ou tempo de trabalho.

Consultas incompletas ou erros interrompem a atualização. O último par de imagens publicado permanece no repositório. A data da última consulta bem-sucedida aparece nos painéis.

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/update_profile_metrics.py
```

A segunda instrução exige `GITHUB_TOKEN`. Os testes usam dados sintéticos e não fazem consultas de rede. Imagens de teste não devem ser publicadas no perfil.
