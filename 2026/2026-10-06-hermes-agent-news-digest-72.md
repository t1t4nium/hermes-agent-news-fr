# Hermes Agent Quotidien #72

Cette édition revient sur le quatre-vingt-treizième numéro des Wingtips consacré à l'installation autonome des skills par l'agent, sur le catalogue The Hermes Workshop qui recense 330 appareils ouverts, sur la gratuité de Solar Mini 4 pendant deux semaines sur Nous Portal, sur les 142 pull requests fusionnées le 5 octobre, et sur la page d'histoires d'usage qui passe à 326 récits.

## Wingtips #93 : l'agent installe ses propres skills

witcheer a consacré le quatre-vingt-treizième numéro des Wingtips à l'installation autonome des skills. L'agent peut trouver un skill et lancer lui-même l'installation, sans qu'on lui fournisse le nom exact ni la commande. Il suffit de demander en langage courant, par exemple « find a skill for flashcards and install it » : il choisit une correspondance et exécute l'installation.

La documentation du système de skills précise la mécanique sous-jacente. Les skills vivent dans `~/.hermes/skills/` et suivent le standard ouvert agentskills.io. L'agent peut créer, mettre à jour et supprimer ses propres skills via l'outil `skill_manage`, et l'installation passe par le Skills Hub, qui regroupe les registres en ligne, skills.sh, les endpoints bien connus et les skills optionnels officiels. Une commande permet aussi d'installer une skill depuis un dépôt GitHub public sans ajouter le dépôt entier : `hermes skills install owner/repo/skills/my-workflow`.

> Sources : [@witcheer, Hermes Wingtips #93: let your Hermes Agent install its own skills, 6 octobre 2026](https://x.com/witcheer/status/2107371954009247994) et [Skills System, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

## The Hermes Workshop : un catalogue de 330 appareils ouverts

Teknium a présenté le 6 octobre un catalogue de matériel ouvert, The Hermes Workshop, à l'adresse teknium.io/hermes-devices. La page recense 330 appareils et outils, 1697 idées d'usage et 30 familles, chacun décrit avec son intérêt, les cas d'usage travaillés et la façon précise dont Hermes Agent s'y connecte et apporte de la valeur.

La règle de la page est qu'un appareil expose une interface locale réelle, REST, MQTT, MCP, SCPI, série, ROS 2 ou un firmware que Hermes peut réécrire et flasher, sans cloud fournisseur quand on peut l'éviter. Hermes écrit le YAML ESPHome et les macros Klipper, flashe les cartes en OTA, surveille imprimantes et réseaux par des cron et mémorise les particularités de chaque appareil dans un skill. La page distingue le gadget seul du gadget avec Hermes : une prise renvoie des watts, avec Hermes elle devient une règle ; une imprimante a une caméra, avec Hermes elle annule elle-même ses impressions ratées. La section « first wave » propose un banc de départ : HA Green et ZBT-2 en colonne vertébrale, deux cartes Hermes Gadget (BOX-3 et AMOLED 1.75) en interphone, OpenWrt One ou BPI-R4 pour le réseau, un parc d'impression Klipper, un banc PyVISA, des corps Reachy Mini et SO-101, et des oreilles RTL-SDR et Meshtastic.

> Sources : [@Teknium, Just made this cool catalog with a ton of open platform hardware, 6 octobre 2026](https://x.com/Teknium/status/2107301976291909994) et [The Hermes Workshop, teknium.io/hermes-devices](https://teknium.io/hermes-devices)

## Solar Mini 4 gratuit deux semaines sur Nous Portal

Nous Research a annoncé le 5 octobre que Solar Mini 4 d'Upstage est gratuit sur Nous Portal pendant deux semaines. Le modèle affiche 3 milliards de paramètres actifs, 35 milliards au total, un contexte de 512 000 jetons et un score de 24 à l'indice Artificial Analysis Intelligence Index, au-dessus de modèles dotés de dix fois plus de paramètres actifs.

witcheer a détaillé la marche à suivre. Sur une installation neuve, `hermes setup --portal` ouvre la connexion au portail, puis, dans n'importe quelle conversation, la commande `/model upstage/solar-mini4:free` bascule sur le modèle, avec `--global` en fin de commande pour en faire le modèle par défaut.

> Sources : [@NousResearch, Solar Mini 4 from @upstageai is free on Nous Portal for the next two weeks, 5 octobre 2026](https://x.com/NousResearch/status/2107138770088714678) et [@witcheer, Solar Mini 4 is free on Nous Portal for the next two weeks, 5 octobre 2026](https://x.com/witcheer/status/2107146375272042977)

## 142 pull requests fusionnées le 5 octobre

iamlukethedev a fait le compte le 6 octobre : Hermes a fusionné 142 pull requests le 5 octobre. Deux changements sont détaillés dans le texte du message :

- Desktop affiche une pastille de progression avant qu'un abonnement atteigne son plafond d'usage, et les fournisseurs limités en débit expliquent pourquoi et jusqu'à quand dans les sélecteurs de modèles.
- Le panneau de réglages de Desktop gagne une entrée Plugins unique qui regroupe les réglages de chaque plugin.

> Source : [@iamlukethedev, Hermes merged 142 PRs on October 5, 6 octobre 2026](https://x.com/iamlukethedev/status/2107274731955306762)

## La page d'histoires d'usage s'étoffe à 326 récits

witcheer a annoncé le 6 octobre l'ajout de 45 nouvelles histoires à la page d'usages, toutes issues de personnes qui utilisent Hermes Agent pour leur travail. Trois exemples sont cités : Razorpay donne à plus de 220 employés leur propre agent permanent, une société d'entretien de piscines signale les mauvais rapports de techniciens pendant que la tournée est encore en cours, et un médecin gagne 30 à 45 minutes de temps.

La page User Stories & Use Cases, consultée le jour même, comptabilise 326 récits répartis en 15 catégories et 11 sources. Les catégories les plus fournies sont le flux de développement (77), l'assistant personnel (49), les intégrations (32), la création (26) et les opérations métier (23). Chaque tuile renvoie vers un vrai post, une issue, une vidéo ou un gist où quelqu'un décrit son usage, collecté sur X, GitHub, Reddit, Hacker News, YouTube, les blogs et les podcasts.

> Sources : [@witcheer, we just added 45 new stories to this page, 6 octobre 2026](https://x.com/witcheer/status/2107458523172901345), [@NousResearch, Here are 326 use cases from real users, 5 octobre 2026](https://x.com/NousResearch/status/2107161699837231107) et [User Stories & Use Cases, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-stories)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
