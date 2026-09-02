# Hermes Agent Quotidien #38

Cette édition revient sur le programme de parrainage lancé par Nous Research pour le Nous Portal, sur l'arrivée de Claude Fable 5.1 dans Hermes Agent à prix réduit, sur le preflight des tâches cron présenté dans le soixante-et-unième numéro des Wingtips, et sur un retour d'usage qui montre un Hermes Agent opérationnel en moins d'une soirée.

## Programme de parrainage du Nous Portal

Nous Research a lancé le 2 septembre un programme de parrainage pour le Nous Portal. Chaque utilisateur du Portal dispose désormais d'un code unique qui donne 15 dollars de réduction sur un plan Plus aux nouveaux utilisateurs, et chaque parrainage réussi ajoute 10 dollars de crédit au compte du parrain.

Le plan Plus, à 20 dollars par mois, inclut 22 dollars de crédits mensuels, plus de 200 modèles, l'usage des outils hébergés et des limites de débit élevées. Le programme s'inscrit dans la logique du Portal, présenté comme le compte unique qui alimente Hermes Agent : modèles, outils et hébergement cloud.

> Sources : [@NousResearch, Introducing the Nous Portal referral program, 2 septembre 2026](https://x.com/NousResearch/status/2095144300405219654) et [Nous Portal, page de présentation](https://portal.nousresearch.com/referrals)

## Claude Fable 5.1 et Mythos 5.1 dans Hermes Agent

Anthropic a présenté le 1er septembre Claude Fable 5.1 et Claude Mythos 5.1, présentés comme les modèles les plus avancés pour le codage et le travail de connaissance. Fable 5.1 est disponible dans Hermes Agent via le Nous Portal à 20 % de réduction sur le prix de l'API, et sur OpenRouter.

Le modèle excelle sur les tâches longues et complexes, et ses capacités de recherche offrent un aperçu de la contribution des modèles au progrès scientifique. Sur les benchmarks, il marque 52,6 % sur Terminal-Bench-Science 0.1, plus du double de Fable 5, et 55,8 % sur Terminal-Bench 4.0 contre 42,0 % pour Fable 5. Les lectures de cache coûtent 75 % de moins que celles de Fable 5, ce qui réduit le coût réel du modèle d'environ 25 % sur les charges typiques et jusqu'à 45 % sur les charges très agentiques. Mythos 5.1, destiné aux cyberdéfenseurs et aux scientifiques du vivant, est disponible via des programmes d'accès de confiance.

> Sources : [@claudeai, We're introducing Claude Fable 5.1 and Claude Mythos 5.1, 1er septembre 2026](https://x.com/claudeai/status/2094848572143407483), [@Teknium, Fable 5.1 is now available in Hermes Agent, 1er septembre 2026](https://x.com/Teknium/status/2094856608002310543) et [@NousResearch, Try Fable 5.1 in Hermes Agent today, 1er septembre 2026](https://x.com/NousResearch/status/2094856799061155948)

## Wingtips #61 : le preflight des tâches cron

Le soixante-et-unième numéro de la série de witcheer porte sur le preflight des tâches cron. Avant de construire l'agent pour une exécution planifiée, le planificateur valide que la configuration peut produire une exécution réussie : la clé du fournisseur se résout, les skills attachés sont prêts, et les cibles de livraison sont connues avec des identifiants de passerelle configurés.

La documentation précise le mécanisme. La vérification de la clé fournisseur est sautée quand une chaîne de secours est configurée, puisque le chemin de repli peut sauver une clé principale manquante. Les skills sont contrôlés pour l'absence de variable d'environnement, de commande ou de fichier d'identifiants requis. Les cibles locales et d'origine ne sont jamais vérifiées. En cas d'échec, le statut de la tâche devient `blocked_config`, une seule alerte est délivrée (elle n'est pas répétée à chaque tick), et aucun appel de modèle n'est fait : une tâche mal configurée ne dépense jamais de jetons. La validation se désactive avec `cron.preflight false` ou `hermes config set cron.preflight false`.

> Sources : [@witcheer, Hermes Wingtips #61 : cron preflight, 2 septembre 2026](https://x.com/witcheer/status/2095028256332271691) et [Scheduled Tasks (Cron), documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)

## Un Hermes Agent opérationnel en moins d'une soirée

witcheer relate qu'un membre de la communauté a installé Hermes Agent sur un VPS de rechange après le dîner, et qu'avant le week-end il suivait ses livraisons de nourriture et construisait de petites applications web pour sa maison. Il en conclut qu'il faut moins d'une soirée de vendredi pour obtenir un Hermes Agent réellement opérationnel.

> Source : [@witcheer, how long does it take to get a real Hermes Agent working for you, 2 septembre 2026](https://x.com/witcheer/status/2095103919726764196)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
