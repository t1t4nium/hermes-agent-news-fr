# Hermes Agent Quotidien #39

Cette édition revient sur l'arrivée de Gemini 3.8 Flash sur le Nous Portal pour Hermes Agent, sur les connexions multi-passerelles persistantes du bureau apportées par v0.21.0, sur un usage qui a nettoyé le dépôt Hermes Agent de 375 000 lignes avec un seul /goal, et sur la collecte des questions pour la deuxième édition de la FAQ.

## Gemini 3.8 Flash disponible sur le Nous Portal

Google DeepMind a présenté le 2 septembre Gemini 3.8 Flash et Gemini 3.8 Flash Cyber, deux variantes d'un même modèle présenté comme le meilleur modèle de raisonnement et de codage de Google, à la même vitesse et au même coût que 3.7 Flash. C'est la troisième release Flash en six semaines. Gemini 3.8 Flash est disponible dès le 2 septembre sur le Nous Portal pour Hermes Agent, au prix de 0,60 dollar par million de jetons en entrée et 3,00 dollars en sortie, identique à 3.7 Flash.

Le modèle est conçu pour les tâches agentiques longues : sur DeepSWE v1.1, il résout de bout en bout des problèmes d'ingénierie complexes en dépassant la plupart des modèles frontaliers plus grands, à une fraction du coût. Il marque 54,9 % sur HLE-Verified et devance 3.7 Flash sur les benchmarks Vals Finance Agent v2 et Harvey's Legal Agent Benchmark. Son gain vient d'un choix de conception : il travaille plus, en exécutant des étapes de raisonnement supplémentaires et en appelant les outils de façon itérative, ce qui peut consommer plus de jetons aux niveaux d'effort élevés. Gemini 3.8 Flash Cyber, destiné aux défenseurs de confiance, est accessible via le programme Fairwind et se concentre sur la découverte de vulnérabilités et le correctif automatique.

> Sources : [@GoogleDeepMind, Two new Gemini models are here, 2 septembre 2026](https://x.com/GoogleDeepMind/status/2095175498967949359), [@Teknium, Gemini 3.8 Flash is now available on Nous Portal for Hermes Agent, 2 septembre 2026](https://x.com/Teknium/status/2095191596698595793), [@witcheer, Gemini 3.8 Flash is on Nous Portal, 2 septembre 2026](https://x.com/witcheer/status/2095195241250734555), [Introducing Gemini 3.8 Flash and 3.8 Flash Cyber, blog Google, 2 septembre 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) et [Nous Portal, catalogue de modèles](https://portal.nousresearch.com/)

## Connexions multi-passerelles persistantes dans le bureau

Nous Research a mis en avant le 2 septembre une fonctionnalité de v0.21.0 : le bureau peut désormais se connecter à plusieurs passerelles à la fois, de façon persistante. On branche n'importe quelle combinaison de passerelles distantes, qu'il s'agisse d'instances Hermes Cloud ou d'agents locaux, et on voit tous les bots et toutes les conversations de l'ensemble dans une même interface.

Teknium précise que cette demande revenait souvent : relier des instances distantes à l'agent local, ou plusieurs instances distantes entre elles, dans l'application de bureau. witcheer décrit le branchement : ouvrir les réglages puis la section Gateways, ou cliquer sur le bouton de connexion de la barre de profil, puis ajouter une connexion et choisir son type. Son bureau, qui tournait déjà contre une instance Hermes Cloud, peut maintenant tenir celle-ci plus toutes ses autres machines en même temps.

> Sources : [@NousResearch, New in Hermes Agent v0.21.0 : Persistent Multi-Gateway Connections for Desktop, 2 septembre 2026](https://x.com/NousResearch/status/2095199772336341480), [@Teknium, connect your remote instances and your local agent, 2 septembre 2026](https://x.com/Teknium/status/2095200455781728672) et [@witcheer, my Desktop already runs against a Hermes Cloud instance, 2 septembre 2026](https://x.com/witcheer/status/2095206552760193096)

## Un /goal qui nettoie le dépôt Hermes Agent

Teknium a raconté le 3 septembre avoir mis Hermes Agent à l'épreuve sur son propre dépôt : un seul /goal, lancé pour nettoyer en profondeur le code, tourne depuis environ quinze heures et a simplifié, unifié, optimisé ou retiré assez de code pour faire tomber 375 000 lignes. Il ajoute que cette exécution mène déjà à d'importantes optimisations pour la montée en charge des sous-agents concurrents dans Hermes Agent.

> Sources : [@Teknium, putting Hermes Agent to the ultimate test of cleaning up the repo, 3 septembre 2026](https://x.com/Teknium/status/2095412050751332838) et [@Teknium, optimizations for scalability of concurrent subagents, 3 septembre 2026](https://x.com/Teknium/status/2095445009642504336)

## La FAQ Hermes Agent et la collecte des questions pour la v2

witcheer a indiqué le 3 septembre que la FAQ de Hermes Agent a été mise en favori plus de 800 fois. L'équipe collecte déjà les questions pour la prochaine édition : elle invite à poser en commentaire ce qui n'a pas encore de réponse claire, en répondant sur place à ce qui est possible et en reportant le reste dans la v2. La FAQ actuelle, dans la documentation, couvre notamment les fournisseurs compatibles, la confidentialité des données, le coût, l'usage hors ligne et la différence entre mémoire et skills.

> Sources : [@witcheer, the Hermes Agent FAQ has been bookmarked over 800 times, 3 septembre 2026](https://x.com/witcheer/status/2095500274508955964) et [FAQ & Troubleshooting, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/faq)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
