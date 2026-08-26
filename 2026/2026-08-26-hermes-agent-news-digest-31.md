# Hermes Agent Quotidien #31

Cette édition revient sur l'élargissement du catalogue de connecteurs MCP de Hermes, sur le chaînage des tâches cron expliqué par witcheer dans le cinquante-cinquième numéro de sa série, sur le critère décisif pour choisir un modèle local, et sur la disponibilité de GLM-5.3 Flash dans Nous Portal après la fin de la gratuité d'Ox Alpha.

## Le catalogue de connecteurs MCP gagne 44 nouvelles connexions

Nous Research a annoncé l'extension du catalogue de connecteurs MCP intégré à Hermes, qui propose désormais 44 nouvelles connexions à des applications courantes, installables en un clic depuis l'application de bureau. L'annonce met en avant l'accès à Cloudflare, Datadog, Metabase, GitLab, Railway et DeepWiki, ainsi qu'à d'autres services et sources de données.

La documentation d'Hermes décrit ce catalogue comme un ensemble de serveurs MCP revus et fusionnés par l'équipe de Nous, désactivés par défaut : on n'installe que ce dont on a besoin. Au moment de l'installation, Hermes interroge le serveur pour lister les outils exposés et présente une liste à cocher. Depuis le terminal, les commandes `hermes mcp` (sélecteur interactif), `hermes mcp catalog` (liste en texte) et `hermes mcp install <nom>` gèrent l'installation. Les entrées sont stockées dans le répertoire `optional-mcps/` du dépôt hermes-agent, leur présence valant approbation de Nous ; il n'existe pas de palier de soumission communautaire, les entrées s'ajoutant par fusion de pull request.

> Sources : [@NousResearch, 44 nouvelles connexions dans le catalogue, 25 août 2026](https://x.com/NousResearch/status/2092326815193055681), [@NousResearch, les services désormais accessibles, 25 août 2026](https://x.com/NousResearch/status/2092321384085299665) et [Hermes Agent, page MCP de la documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)

## Wingtips #55 : chaîner les tâches cron

Le cinquante-cinquième numéro de la série de witcheer porte sur le chaînage des tâches cron. Chaque tâche cron démarre dans une session neuve, si bien qu'un pipeline en deux étapes, par exemple collecter puis résumer, ne peut pas voir par défaut ce que la première étape a produit. La connexion se fait avec `context_from` : en créant la deuxième tâche, on la pointe vers l'identifiant de la première, qui lui transmet alors sa sortie.

> Source : [@witcheer, Hermes Wingtips #55, chaîner les tâches cron, 26 août 2026](https://x.com/witcheer/status/2092527968140632114)

## Choisir un modèle local : la capacité d'appel d'outils avant tout

witcheer rappelle le critère qui compte le plus dans la fiche technique d'un modèle local destiné à Hermes : la ligne qui importe est de savoir si le modèle a été entraîné à appeler les outils. En dessous de ce seuil, on obtient un modèle qui narre : il écrit en toutes lettres l'appel d'outil qu'il ferait, sous forme de texte, et rien ne s'exécute ensuite.

> Source : [@witcheer, choisir un modèle local pour Hermes, 26 août 2026](https://x.com/witcheer/status/2092589072480919837)

## GLM-5.3 Flash prend le relais dans Nous Portal

Teknium indique que la période gratuite d'Ox Alpha via Nous Portal est terminée, et que GLM-5.3 Flash est désormais disponible pour qui souhaite poursuivre l'usage.

> Source : [@Teknium, fin de la gratuité d'Ox Alpha et arrivée de GLM-5.3 Flash, 26 août 2026](https://x.com/Teknium/status/2092626520678465760)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
