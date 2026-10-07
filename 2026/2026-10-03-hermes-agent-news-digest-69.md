# Hermes Agent Quotidien #69

Cette édition revient sur la commande `/blueprint` présentée dans les Wingtips, sur les 175 pull requests fusionnées le 2 octobre, sur les améliorations récentes de Hermes Desktop, et sur l'installation d'un serveur MCP en un clic depuis le catalogue de connecteurs.

## Wingtips #90 : /blueprint

witcheer a consacré le numéro 90 des Wingtips à la commande `/blueprint`. Elle met en place une automatisation prête à l'emploi : Hermes pose ses questions une par une, puis planifie le tout comme une tâche cron, sans écrire la moindre syntaxe cron. L'exemple donné dans le message, une courte leçon chaque matin de semaine sur un sujet choisi, correspond au blueprint Daily learning drip du catalogue.

La documentation précise la mécanique. La forme complète est `/blueprint [name] [slot=value ...]`, avec l'alias `/bp`. Appelée sans argument, elle liste le catalogue ; avec un nom, elle démarre un remplissage guidé des champs au tour suivant ; avec des valeurs passées en ligne, comme `/blueprint morning-brief time=08:00`, elle crée la tâche directement. Un blueprint ne planifie jamais en silence : la création est toujours confirmée, et les tâches se gèrent ensuite avec `/cron`. Techniquement, un blueprint n'est qu'une skill qui déclare un bloc `metadata.hermes.blueprint` dans son en-tête `SKILL.md`.

> Sources : [@witcheer, Hermes Wingtips #90: /blueprint, 3 octobre 2026](https://x.com/witcheer/status/2106275419557126419), [Slash Commands Reference, /blueprint, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) et [Automation Blueprints Catalog, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)

## 175 pull requests fusionnées le 2 octobre

iamlukethedev a fait le compte le 3 octobre : Hermes a fusionné 175 pull requests le 2 octobre. Deux entrées figurent dans le texte du message, le reste de la liste étant détaillé dans la capture jointe :

- Des dizaines de nouveaux plugins ont rejoint le catalogue, des fournisseurs de mémoire à Gmail, WhatsApp, Health et Agent Builder.
- Les fournisseurs de mémoire se migrent depuis Desktop, la passerelle et les mises à jour scriptées, sans ouvrir de terminal.

> Source : [@iamlukethedev, Hermes merged 175 PRs on October 2, 3 octobre 2026](https://x.com/iamlukethedev/status/2106190123100746023)

## Une semaine d'améliorations de Hermes Desktop

tonbistudio a publié le 2 octobre une vidéo récapitulative des petites améliorations apportées à Hermes Desktop au cours de la semaine, reprise par witcheer le soir même. Les nouveautés listées dans le message : glisser-déposer des sessions entre projets, de nouveaux thèmes, une taille de texte de discussion réglable indépendamment de celle de l'interface, et un volet de revue qui affiche les changements non commités et la branche. Le sélecteur de modèles avec favoris, déjà couvert dans l'édition #67, figure aussi dans la liste. witcheer met justement ce point en avant : épingler les deux ou trois modèles entre lesquels on bascule les place en haut de liste.

> Sources : [@tonbistudio, The last week had several small improvements to the Hermes Desktop app, 2 octobre 2026](https://x.com/tonbistudio/status/2106119254785634400) et [@witcheer, a week of Hermes Desktop updates in under 5 min, 2 octobre 2026](https://x.com/witcheer/status/2106121038106972394)

## Installer un serveur MCP en un clic depuis Desktop

witcheer a montré le 2 octobre comment ajouter un serveur MCP à Hermes Agent en un clic depuis Hermes Desktop. Le parcours se déroule dans la page Capabilities puis l'onglet Connectors : on cherche le catalogue, ici DeepWiki qui répond sur n'importe quel dépôt GitHub public, on clique sur Install, et la carte liste les outils apportés. La quatrième étape, coupée par la limite de caractères, se poursuit dans la vidéo jointe.

La documentation des intégrations rappelle le rôle de MCP : relier Hermes à des serveurs d'outils externes via le protocole Model Context Protocol, avec prise en charge des transports stdio et SSE, du filtrage des outils par serveur et de l'enregistrement de ressources et d'invites.

> Sources : [@witcheer, how to add an MCP server to Hermes Agent in one click, 2 octobre 2026](https://x.com/witcheer/status/2106036133666619806) et [Integrations, MCP Servers, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
