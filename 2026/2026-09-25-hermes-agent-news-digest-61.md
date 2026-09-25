# Hermes Agent Quotidien #61

Cette édition revient sur l'arrivée de Fast Search, la recherche web de Perplexity désormais offerte à tous les abonnés Nous Portal, sur la sortie stable du Cua Driver pour Omarchy et son curseur synthétique natif, sur le modèle furtif Space Bunny Alpha rendu gratuit sur Nous Portal, sur le passage de l'interface de Hermes Desktop à neuf langues, et sur le Bot Screen accessible depuis un téléphone via Herald.

## Fast Search de Perplexity devient la recherche web par défaut de Hermes Agent

Nous Research a annoncé le 24 septembre que la recherche web dans Hermes Agent est désormais rapide et gratuite, Perplexity ayant construit Fast Search pour les agents et l'offrant à tous les paliers de l'abonnement Nous Portal. Perplexity précise le même jour que Fast Search devient le moteur de recherche par défaut dans Hermes Agent pour les abonnés Nous Portal, pensé pour les tâches agentiques, avec une latence d'appel de recherche unique de 160 ms en p50 et 230 ms en p95.

Fast Search s'appuie sur Photon, le moteur de récupération et de classement que Perplexity a écrit en Rust pour remplacer son moteur open source précédent, avec une petite équipe d'ingénieurs assistée par des agents de codage. Le préréglage rapide de l'API de recherche réduit le coût estimé modèle plus recherche par tâche de 68 % sur six bancs d'essai, à qualité d'ensemble comparable, et la latence p99 interne de récupération et de classement est tombée d'environ 800 ms à 65 ms, en consommant environ 20 % de machines de moins et en stockant 2,5 fois plus de données par document. Perplexity recommande ce préréglage rapide pour les tâches agentiques courantes, le préréglage standard restant plus robuste pour les questions ambiguës.

Côté activation, witcheer résume la marche à suivre : si la recherche web passe déjà par l'abonnement Nous Portal, elle bascule automatiquement avec la mise à jour dès la première réponse ; sinon, `hermes tools` déplace le web vers la route Nous, et il s'agit du même outil `web_search`. La documentation de Perplexity confirme que Fast Search est le moteur par défaut dans Hermes Agent et qu'il y est gratuit.

> Sources : [@NousResearch, Web search in Hermes Agent is now fast and free, 24 septembre 2026](https://x.com/NousResearch/status/2103244070407802905), [@perplexitydevs, Fast Search is now the default search in Hermes Agent for Nous Portal subscribers, 24 septembre 2026](https://x.com/perplexitydevs/status/2103241128216875283), [@witcheer, here is everything you need to know about Fast Search, 25 septembre 2026](https://x.com/witcheer/status/2103355797140918397), [Photon: Building a Retrieval and Ranking Engine From Scratch, Perplexity, 24 septembre 2026](https://www.perplexity.ai/hub/blog/photon) et [Perplexity web search in Hermes, documentation Perplexity](https://docs.perplexity.ai/docs/getting-started/integrations/hermes)

## Cua Driver stable sur Omarchy, un curseur synthétique natif

Cua a annoncé le 25 septembre la sortie stable du Cua Driver pour Omarchy, présentée comme une nouvelle fondation pour l'usage de l'ordinateur, intégrée au système d'exploitation dès sa conception. Pendant un mois, l'équipe a travaillé directement avec dhh, SpencerGBull et vaxryy pour apporter un curseur synthétique natif au compositeur Hyprland d'Omarchy, ce qui permet un usage de l'ordinateur multi-curseur au niveau du système. Le Cua Driver est open source.

La différence avec les plates-formes établies est nette. Sur macOS et Windows, l'usage de l'ordinateur en arrière-plan repose encore sur des compromis et des contournements dans leurs serveurs de fenêtres pour supporter plusieurs curseurs synthétiques. Sur Omarchy, le compositeur possède les deux curseurs, celui de l'agent et celui de l'humain, et les route vers les bonnes fenêtres : l'entrée de l'agent reste séparée au lieu de prendre la main sur le bureau. L'intégration actuelle est disponible via le canal Edge d'Omarchy, et le Cua Driver publie aussi des artefacts Linux ARM64.

witcheer relève que l'usage de l'ordinateur dans Hermes Agent tourne sur le Cua Driver, ce qui rend ce passage au natif d'autant plus notable pour l'écosystème.

> Sources : [@trycua, Today we're announcing the stable Cua Driver release for Omarchy, 25 septembre 2026](https://x.com/trycua/status/2103498682532253734), [@witcheer, computer use in Hermes Agent runs on Cua Driver, 25 septembre 2026](https://x.com/witcheer/status/2103501253477040390), [trycua/cua, dépôt GitHub](https://github.com/trycua/cua) et [Omarchy](https://omarchy.org/)

## Space Bunny Alpha, un modèle furtif gratuit sur Nous Portal

witcheer a relayé le 25 septembre les premiers retours sur Space Bunny Alpha, un modèle furtif désormais disponible sans surcoût sur Nous Portal : rapide, direct, avec un raisonnement court, ce qui compte dans un agent où chaque appel d'outil attend le modèle. Il est proposé avec un contexte d'un million de jetons et une entrée image et vidéo, à charger dans Hermes Agent par `/model stealth/space-bunny-alpha`. yeahfortommy avait annoncé le lancement le même jour, un peu plus tôt, Space Bunny Alpha étant gratuit sur Nous Portal et prêt à l'emploi dans Hermes Agent.

> Sources : [@witcheer, people first feedback about this model, 25 septembre 2026](https://x.com/witcheer/status/2103359553454940411) et [@yeahfortommy, another stealth model launch Space Bunny Alpha is now FREE on Nous Portal, 25 septembre 2026](https://x.com/yeahfortommy/status/2103302058103418906)

## Hermes Desktop passe à neuf langues

witcheer a annoncé le 25 septembre que Hermes Desktop est désormais disponible en neuf langues : anglais, chinois simplifié, chinois traditionnel, japonais, arabe et russe, auxquels s'ajoutent le français, l'allemand et l'espagnol, arrivés récemment. Le choix de la langue se fait dans Réglages, Apparence, Langue.

> Source : [@witcheer, Hermes Desktop now comes in 9 languages, 25 septembre 2026](https://x.com/witcheer/status/2103429693412425915)

## Le Bot Screen arrive sur téléphone via Herald

iamlukethedev a montré le 24 septembre le Bot Screen sur téléphone, après avoir ajouté son support à Herald. Il peut ouvrir son téléphone et regarder son bot Hermes utiliser son ordinateur en temps réel, puis, face à une étape qui demande son intervention, reprendre l'ordinateur directement depuis le téléphone, la traiter lui-même et rendre le contrôle.

> Source : [@iamlukethedev, Hermes Bot Screen is now on my phone, 24 septembre 2026](https://x.com/iamlukethedev/status/2103002905959936334)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
