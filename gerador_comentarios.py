import pandas as pd

# Criando o dataset
comentarios = [
    ("Shang-Chi trouxe uma ação incrível e cenas de luta muito bem coreografadas. Finalmente um herói novo que empolga!", "Positivo"),
    ("WandaVision foi uma série inovadora, cheia de simbolismos e com atuações brilhantes, especialmente da Elizabeth Olsen.", "Positivo"),
    ("Loki expandiu o multiverso de forma genial! Tom Hiddleston está impecável no papel.", "Positivo"),
    ("O Homem-Aranha: Sem Volta Para Casa foi pura nostalgia! A aparição dos três Homens-Aranha foi épica!", "Positivo"),
    ("Pantera Negra: Wakanda Para Sempre fez uma linda homenagem a Chadwick Boseman e emocionou do começo ao fim.", "Positivo"),
    ("Guardiões da Galáxia Vol. 3 trouxe um encerramento perfeito para a equipe! Humor, emoção e ação na medida certa.", "Positivo"),
    ("A introdução do Kang em Homem-Formiga e a Vespa: Quantumania foi um dos melhores momentos das novas fases!", "Positivo"),

    ("Desde Ultimato, o MCU perdeu o rumo. Muitos filmes e séries sem conexão e sem impacto real no universo.", "Negativo"),
    ("Doutor Estranho no Multiverso da Loucura prometeu muito e entregou pouco. A história ficou bagunçada e Wanda foi mal aproveitada.", "Negativo"),
    ("Thor: Amor e Trovão foi uma decepção! Exageraram no humor e o vilão do Christian Bale foi mal explorado.", "Negativo"),
    ("Cavaleiro da Lua começou bem, mas o final foi apressado e sem grandes consequências para o MCU.", "Negativo"),
    ("Invasão Secreta tinha potencial para ser uma série épica de espionagem, mas virou um desperdício de tempo.", "Negativo"),
    ("A Fase 4 da Marvel pareceu sem direção. Muitos personagens novos, mas sem uma história realmente cativante.", "Negativo"),
    ("A CGI está piorando a cada produção. Quantumania parecia um jogo de PS3 em alguns momentos!", "Negativo"),

    ("A Fase 4 da Marvel trouxe muitas séries e filmes, explorando novos personagens e expandindo o multiverso.", "Neutro"),
    ("Alguns amam o novo estilo da Marvel, outros acham que perdeu a magia. Depende muito do que você espera do MCU.", "Neutro"),
    ("Desde Ultimato, a Marvel está focando mais em séries no Disney+, o que pode ser bom para aprofundar personagens.", "Neutro"),
    ("A introdução do multiverso trouxe novas possibilidades, mas também tornou a história mais complexa e difícil de acompanhar.", "Neutro"),
    ("Muitos filmes da Fase 4 e 5 focam em diversidade e representatividade, o que agrada alguns fãs e desagrada outros.", "Neutro"),
    ("Com a chegada do Kang, a Marvel parece estar preparando um novo grande evento, mas ainda não sabemos se será tão grandioso quanto Ultimato.", "Neutro"),

    ("Homem-Aranha: Sem Volta Para Casa trouxe uma das melhores experiências de cinema dos últimos anos!", "Positivo"),
    ("Ms. Marvel foi uma surpresa agradável! Ótima representatividade e uma vibe divertida.", "Positivo"),
    ("A trilha sonora de Wakanda Para Sempre foi simplesmente espetacular!", "Positivo"),
    ("A atuação de Jonathan Majors como Kang foi incrível, ele realmente impõe presença!", "Positivo"),
    ("A conexão entre Loki e o multiverso foi muito bem feita e deixou um gostinho de quero mais.", "Positivo"),
    
    ("Thor: Amor e Trovão parecia mais uma paródia do que um filme sério do MCU.", "Negativo"),
    ("Muitos efeitos especiais da Fase 5 parecem apressados, prejudicando a imersão.", "Negativo"),
    ("A Marvel está exagerando no número de produções, o que torna difícil acompanhar tudo.", "Negativo"),
    ("Não há mais o mesmo impacto emocional nos filmes da Marvel desde Ultimato.", "Negativo"),
    ("Quantumania tentou ser grandioso, mas o roteiro foi fraco e sem emoção.", "Negativo"),
    
    ("A qualidade das séries da Marvel varia bastante, algumas são incríveis, outras decepcionam.", "Neutro"),
    ("O futuro do MCU parece incerto, mas a Saga do Multiverso pode surpreender.", "Neutro"),
    ("Alguns personagens novos são interessantes, mas falta um foco maior na narrativa geral.", "Neutro"),
    ("As séries no Disney+ trouxeram um novo formato para o MCU, mas nem todas foram bem aproveitadas.", "Neutro"),
    ("O CGI em alguns filmes é ótimo, mas em outros deixa a desejar, dependendo do orçamento.", "Neutro"),

    ("Gavião Arqueiro trouxe uma história leve e divertida, e a introdução da Kate Bishop foi ótima!", "Positivo"),
    ("Eu amei a série do Cavaleiro da Lua! Oscar Isaac entregou uma performance incrível!", "Positivo"),
    ("Doutor Estranho no Multiverso da Loucura teve uma direção fantástica de Sam Raimi, cheia de identidade!", "Positivo"),
    ("A química entre Tom Holland e Zendaya faz toda a diferença nos filmes do Homem-Aranha.", "Positivo"),
    ("What If? explorou histórias alternativas muito criativas e expandiu o conceito do multiverso.", "Positivo"),
    
    ("A Marvel está apostando demais em humor exagerado, o que torna alguns filmes cansativos.", "Negativo"),
    ("A morte do T’Challa deixou um vazio na história do MCU que não foi bem resolvido.", "Negativo"),
    ("Secret Invasion poderia ter sido um thriller político épico, mas foi muito mal executado.", "Negativo"),
    ("She-Hulk tentou inovar, mas a quebra de quarta parede ficou forçada e sem graça.", "Negativo"),
    ("Eternos trouxe muitos personagens novos de uma vez, dificultando a conexão com o público.", "Negativo"),
    
    ("As produções do MCU estão mais diversificadas, o que pode ser positivo ou negativo, dependendo do público.", "Neutro"),
    ("O conceito de variantes foi bem introduzido, mas às vezes confunde o espectador casual.", "Neutro"),
    ("As séries têm explorado personagens secundários de maneira interessante.", "Neutro"),
    ("Com tantas produções, fica difícil saber quais são realmente essenciais para a trama geral do MCU.", "Neutro"),
    ("O hype em torno dos filmes da Marvel diminuiu, mas ainda há expectativa para os próximos lançamentos.", "Neutro"),
]

# Criando DataFrame
df = pd.DataFrame(comentarios, columns=["Comentário", "Sentimento"])

# Salvando como CSV
file_path = "dataset_marvel_comentarios.csv"
df.to_csv(file_path, index=False, encoding="utf-8")

file_path