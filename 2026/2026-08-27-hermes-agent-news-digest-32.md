# Hermes Agent Quotidien #32

Cette édition revient sur la nouvelle release stable v0.20.6, sur la façon de changer de modèle depuis n'importe quel chat, sur le bureau qui pilote toutes ses machines à distance, sur la refonte du catalogue de modèles de Nous Portal, et sur l'arrêt des instances Nitter sous la pression de X Corp.

## Hermes Agent v0.20.6 (v2026.8.27)

Nous Research a tagué la version patch v0.20.6, qui rassemble environ 525 pull requests fusionnées depuis v0.20.5, soit environ 1 313 commits répartis sur 1 557 fichiers.

Les changements notables :
- Navigation réelle consentie : utilisation du profil Chromium par défaut pour la navigation locale, avec flux de fermeture sur approbation sous Windows.
- Le navigateur du bureau gagne sa propre fenêtre de système d'exploitation, un moteur de mise à jour distante géré par SSH et un rail de profils de flotte.
- Élargissement du catalogue MCP distant : plus de 50 serveurs hébergés par des éditeurs, vérifiés en conditions réelles, dont Cloudflare, Grafana Cloud, Better Stack et Railway.
- Cache des résultats à durée de vie (TTL) pour web_search et web_extract.
- Compression lean-tail par défaut.
- tool_search multi-requêtes avec racinisation (stemming).
- Chiffrement optionnel des secrets stockés via le trousseau du système, qui supprime les invites du trousseau macOS à chaque lancement.
- Les programmes de mise à jour suspendent les passerelles via la socket de contrôle au lieu de tuer l'arbre de processus.
- Les installations gérées par image ou par paquet refusent les mises à jour sur place non sûres (phase 3 de l'issue #91277).
- Cron : accusés de réception durables des incidents et échecs de désynchronisation de code plus clairs.
- Contrôles de dépliage de liens Slack.
- Identités de conteneur Docker partagées.
- Backends d'environnement de terminal enfichables.
- Nouveaux modèles dans les sélecteurs : GLM-5.3 Flash, MiniMax M3 (gratuit) et MiniMax H3 Max (vidéo).

Les notes complètes et la liste des contributeurs sont prévues avec v0.21.0.

> Source : [Hermes Agent v0.20.6 (v2026.8.27), GitHub Releases, 27 août 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.27)

## Hermes Wingtips #56 : changer de modèle de n'importe où

Le cinquante-sixième numéro de la série de witcheer porte sur le changement de modèle depuis n'importe où. La commande `hermes model` ouvre un sélecteur interactif, ce qui lui interdit de passer par un pipe, un script ou l'outil terminal d'un autre agent. La parade est de ne pas passer par le sélecteur : dans n'importe quel chat, sur n'importe quelle plateforme, la commande `/model grok-4 --provider` suivie de l'adresse du fournisseur bascule directement le modèle.

> Source : [@witcheer, Hermes Wingtips #56, changer de modèle de n'importe où, 27 août 2026](https://x.com/witcheer/status/2092941623961190832)

## Une fenêtre de bureau pour piloter toutes ses machines

witcheer montre que la fenêtre du bureau Hermes peut piloter toutes les machines où vivent ses agents : un VPS cloud, une machine en SSH ou la passerelle locale se connectent, et on bascule entre elles depuis la barre d'état du bas. Tous les profils de toutes les passerelles connectées s'affichent dans une seule liste, à un clic. La démonstration illustre le moteur de mise à jour distante par SSH et le rail de profils de flotte livrés avec v0.20.6.

> Source : [@witcheer, une fenêtre de bureau pour toutes ses machines, 27 août 2026](https://x.com/witcheer/status/2092861480098058328)

## Nous Portal : une page catalogue de modèles refondue

Nous Research a retravaillé la page catalogue de modèles de Nous Portal, qui rassemble désormais tout au même endroit : les modèles gratuits actifs, les promotions, et une liste triable de tous les autres modèles disponibles.

> Source : [@NousResearch, catalogue de modèles de Nous Portal refondu, 27 août 2026](https://x.com/NousResearch/status/2092776270333395353)

## Les instances Nitter s'arrêtent sous la pression de X Corp

Le 24 août 2026, X Corp a envoyé des lettres de cessation et d'abstention exigeant le retrait permanent des instances Nitter et du dépôt du projet. Les miroirs publics ferment les uns après les autres : nitter.net annonce être hors ligne et le développement arrêté, l'instance tiekoetter indique être fermée pour une durée indéterminée sans date de retour, et XCancel a cessé son service après avoir reçu sa propre lettre de X Corp. La notice de l'instance tiekoetter renvoie vers le commit de note légale en amont et la discussion publique tenue sur le dépôt Nitter. L'arrêt de ces miroirs réduit les accès libres à X pour la veille de l'écosystème.

> Sources : [nitter.tiekoetter.com, notice d'indisponibilité, 27 août 2026](https://nitter.tiekoetter.com/), [zedeus/nitter, commit de note légale, 24 août 2026](https://github.com/zedeus/nitter/commit/f75bf5872e36a255a9765114ec0eb2a0394bef1f), [zedeus/nitter, discussion sur les instances publiques, issue #1442](https://github.com/zedeus/nitter/issues/1442) et [xcancel.com, avis de cessation, 24 août 2026](https://xcancel.com/)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
