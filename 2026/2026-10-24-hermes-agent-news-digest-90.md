# Hermes Agent Quotidien #90

Cette édition revient sur les 122 pull requests fusionnées le 23 octobre, dont le passage de l'automatisation du navigateur sur browser_exec, sur le Curator qui entretient les skills de l'agent, sur Hermes Watch pour la montre Amazfit Active 2, sur l'arrivée de Kimi K3.1 Pro sur le Nous Portal, sur le plugin communautaire draft-cards et sur le conseil Wingtips consacré à la recherche de plugins.

## 122 pull requests fusionnées le 23 octobre

iamlukethedev a fait le compte le 24 octobre : Hermes a fusionné 122 pull requests le 23 octobre. Les changements à retenir :

- L'automatisation du navigateur ne passe plus que par browser_exec : agent-browser et les outils navigateur intégrés disparaissent, et Camofox part vers un plugin.
- Les invites de confiance MCP mémorisent enfin les choix : « Allow for this session » et « Always » sont retenus par outil, et une invite qui ne vaut que pour un seul appel ne propose plus que Once et Deny.

Le changelog du 23 octobre relève aussi le mode YOLO et la désactivation d'approvals.mode, qui ne demandent plus rien pour les appels d'écriture MCP non fiables sauf quand ils dépassent la limite de dépense ; les cartes de plugins qui répondent dans leur propre conversation ; les plugins Desktop qui disposent de leur propre dossier et de dossiers accordés par l'utilisateur ; et une installation refusée qui nomme désormais l'application manquante.

> Sources : [@iamlukethedev, Hermes merged 122 PRs on October 23, 24 octobre 2026](https://x.com/iamlukethedev/status/2113855789941039237) et [Hermes Bible, changelog du 23 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-23)

## Le Curator entretient les skills de l'agent

NetworkChuck a mis en avant le 23 octobre la fonction Curator de Hermes, qui affine et améliore les skills, retire ceux qui ne marchent pas et en crée de nouveaux automatiquement. La documentation en précise le fonctionnement : c'est une passe d'entretien en arrière-plan pour les skills créés par l'agent. Elle suit la fréquence de consultation, d'usage et de modification de chaque skill, et fait passer les skills longtemps inutilisés par les états actif, périmé puis archivé. Une passe de consolidation par un modèle auxiliaire, facultative et désactivée par défaut, peut proposer de fusionner les skills qui se recouvrent ou de corriger les dérives.

Le Curator ne supprime jamais de lui-même : le pire cas est l'archivage dans ~/.hermes/skills/.archive/, récupérable. Il ne gère par défaut que les skills créés par l'agent, épargne les skills épinglés et ceux référencés par une tâche cron, et se déclenche sur une inactivité d'au moins deux heures après un intervalle de sept jours.

> Sources : [@NetworkChuck, That's exactly what the Curator feature in Hermes does, 23 octobre 2026](https://x.com/NetworkChuck/status/2113753045028773982) et [Curator, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator/)

## Hermes Watch sur Amazfit Active 2

witcheer a présenté le 23 octobre Hermes Watch, un build communautaire open source pour la montre Amazfit Active 2. On touche TALK, on pose sa question, et Hermes Agent répond sur la montre, en texte et à voix haute. La voix entre, la réponse arrive au poignet, sans téléphone en main.

> Source : [@witcheer, your Hermes Agent, on your wrist, 23 octobre 2026](https://x.com/witcheer/status/2113684377527840794)

## Kimi K3.1 Pro sur le Nous Portal

witcheer a signalé le 24 octobre que Kimi K3.1 Pro est déjà sur le Nous Portal, à une commande `hermes model` dans Hermes Agent. Il cite Artificial Analysis, qui place le modèle en quatrième position de son Intelligence Index avec un score de 55, et relève de nets gains en performance agentique. Le modèle de raisonnement de Kimi Moonshot gagne 11 points sur Kimi K3 et sera le modèle open weights en tête une fois ses poids publiés.

> Sources : [@witcheer, Kimi K3.1 Pro is already on Nous Portal, 24 octobre 2026](https://x.com/witcheer/status/2113865988693508269) et [@ArtificialAnlys, Kimi K3.1 Pro launches at 4th on the Artificial Analysis Intelligence Index, 23 octobre 2026](https://x.com/ArtificialAnlys/status/2113688083145314416)

## draft-cards, des brouillons en cartes

tonbistudio a recommandé le 23 octobre draft-cards, un plugin communautaire qui transforme les brouillons de mail ou de message en cartes modifiables plutôt qu'en bloc de texte. Le dépôt précise le fonctionnement : demander un mail à Hermes affiche une carte avec destinataires, objet et corps, prêts à relire. Une demande de changement ouvre une nouvelle carte qui surligne exactement les mots modifiés. On peut éditer directement dans la carte, et rien ne part avant d'appuyer sur Envoyer. Le plugin fonctionne sans aucune configuration mail, n'appelle aucun service réseau et ne lit aucun jeton ni compte. Installation : `hermes plugins install arsiktech/hermes-draft-cards --enable`, à partir de Hermes 0.22.2.

> Sources : [@tonbistudio, draft-cards lets you draft emails or any kind of message as an editable card, 23 octobre 2026](https://x.com/tonbistudio/status/2113733357683261472) et [Draft Cards for Hermes, dépôt arsiktech/hermes-draft-cards](https://github.com/arsiktech/hermes-draft-cards)

## Wingtips #109, chercher des plugins

witcheer a publié le 24 octobre le conseil Wingtips #109. Le catalogue de plugins de Hermes est une liste relue de plugins installables par leur nom, et on peut la chercher depuis le terminal avec `hermes plugins search <terme>`. On tape un mot comme weather, rss ou telegram, et Hermes le rapproche des noms de plugins.

> Source : [@witcheer, Hermes Wingtips #109: hermes plugins search, 24 octobre 2026](https://x.com/witcheer/status/2113910871046947127)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
