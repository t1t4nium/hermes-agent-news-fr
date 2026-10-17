# Hermes Agent Quotidien #83

Cette édition revient sur le partenariat de lancement avec NVIDIA autour de RTX Spark, sur les 136 pull requests fusionnées le 16 octobre, sur The Hermes Workshop, le catalogue de matériel ouvert de Teknium, et sur l'arrivée de GPT 6.1 Sol au classement Hermes Index.

## Hermes Agent, partenaire de lancement de RTX Spark

Nous Research a annoncé le 16 octobre que Hermes Agent est partenaire de lancement de RTX Spark, la gamme de NVIDIA pour la nouvelle génération de portables. Sur ces machines, on choisit Hermes dans le flux d'installation des agents intégré à Windows, on suit le nouvel onboarding génératif, et l'agent tourne en local sur le portable ou dans le cloud.

witcheer a précisé la même journée que, sur les nouveaux portables RTX Spark, Hermes Agent est déjà présent dans l'installation des agents sous Windows. On le sélectionne, le nouvel onboarding se charge de la configuration, et il fonctionne sur la machine elle-même ou dans le cloud.

> Sources : [@NousResearch, Hermes Agent is a launch partner for nvidia's RTX Spark, 16 octobre 2026](https://x.com/NousResearch/status/2111130297907470840) et [@witcheer, RTX Spark laptops, 16 octobre 2026](https://x.com/witcheer/status/2111151153136418945)

## 136 pull requests fusionnées le 16 octobre

iamlukethedev a fait le compte le 16 octobre : Hermes a fusionné 136 pull requests le 16 octobre. Les changements mis en avant :

- L'auto-prune redevient optionnel : Hermes pose une seule question quand le disque se remplit, et cette demande ne retarde plus jamais le démarrage.
- Signal, Weixin, BlueBubbles, QQ Bot, Yuanbao et WhatsApp Cloud arrivent en plugins groupés.

Teknium est revenu le même jour sur l'auto-prune. Face aux retours sur la purge automatique des sessions au bout de 90 jours, la purge sera désactivée par défaut. Sur les nouvelles sessions, Hermes fait une vérification quasi instantanée pour détecter si la base de données va saturer le stockage, puis propose de purger ou de gérer soi-même.

> Sources : [@iamlukethedev, Hermes merged 136 PRs on October 16, 16 octobre 2026](https://x.com/iamlukethedev/status/2111235168321306881) et [@Teknium, Had some pushback on the new auto-prune, 16 octobre 2026](https://x.com/Teknium/status/2111215992882004405)

## The Hermes Workshop, un catalogue de 330 appareils

Teknium a publié le 17 octobre The Hermes Workshop, un catalogue de 330 appareils ouverts et pilotables par interface, répartis en 30 familles, avec 1 697 idées de projets rédigées. Chaque appareil expose une vraie interface locale, REST, MQTT, MCP, SCPI, série, ROS 2, ou un firmware que Hermes peut réécrire puis flasher, sans cloud constructeur dans la boucle quand on peut l'éviter.

La page détaille le rôle de Hermes : il écrit du YAML ESPHome et des macros Klipper, flashe les cartes en OTA, surveille imprimantes et réseau via des tâches cron, et mémorise les particularités de chaque appareil dans une skill. La première famille, les gadgets natifs Hermes, rassemble des cartes ESP32-S3 de Waveshare, le BOX-3 d'Espressif et le CoreS3 de M5Stack. Une fois flashées, elles s'enregistrent comme plateforme de passerelle, et un petit écran de poche hérite de la même mémoire, des mêmes approbations et des mêmes outils que Telegram ou l'application Desktop.

> Sources : [@Teknium, Another awesome IoT Hermes device, 17 octobre 2026](https://x.com/Teknium/status/2111283078396277232), [@iamlukethedev, Teknium just dropped a catalog of 330 open hardware devices, 17 octobre 2026](https://x.com/iamlukethedev/status/2111300782503100851) et [The Hermes Workshop, showcase de matériel](https://teknium.io/hermes-devices)

## GPT 6.1 Sol rejoint Hermes Index

Teknium a signalé le 16 octobre la mise à jour de Hermes Index, le classement des modèles agentiques tenu dans Hermes Agent, avec l'arrivée de GPT 6.1 Sol et de plusieurs autres modèles. Sur le classement, GPT 6.1 Sol se place deuxième avec un score moyen de 57,09 pour 1,19 dollar par tâche, derrière Claude Opus 5.5 qui mène à 63,31.

Le score est la moyenne de quatre suites, Hermes Bench, TerminalBench 4, TerminalBench Science et SkillsBench, et le coût affiché est la moyenne par tâche. Le classement indique aussi les scores de chaque suite : GPT 6.1 Sol atteint 73,93 sur Hermes Bench pour 0,26 dollar par tâche, contre 76,73 pour Claude Opus 5.5.

> Sources : [@Teknium, Hermes Index has been updated, 16 octobre 2026](https://x.com/Teknium/status/2111197448282702310) et [Hermes Index, classement des modèles agentiques](https://portal.nousresearch.com/bench#leaderboard)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
