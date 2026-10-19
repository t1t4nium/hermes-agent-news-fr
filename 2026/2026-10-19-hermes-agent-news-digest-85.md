# Hermes Agent Quotidien #85

Cette édition revient sur les 55 pull requests fusionnées le 18 octobre, sur vibeline, une frise chronologique des sessions de l'agent, sur un réglage Telegram qui rattrape les messages reçus pendant l'arrêt, et sur deux usages de la communauté : découper son agent en profils et le transformer en petit studio de jeu.

## 55 pull requests fusionnées le 18 octobre

iamlukethedev a fait le compte le 19 octobre : Hermes a fusionné 55 pull requests le 18 octobre. Les changements mis en avant :

- /usage dans Desktop et le TUI affiche les limites de compte du fournisseur avant l'envoi du premier message.
- Les bacs à sable Docker se resserrent : les fichiers ne peuvent plus ramener vers l'hôte des bits setuid/setgid ni des capacités de fichier, et les fichiers écrits en root sont rendus à l'utilisateur à la fin.
- Les plugins peuvent poster dans la conversation en cours et modifier ce message sur place.
- Deux nouveaux hooks : post_compaction se déclenche sur chaque chemin de compression, et on_session_delete informe les plugins de chaque suppression et archivage de session.
- Les commandes slash des plugins reçoivent la session appelante sur chaque surface.
- Les clients en retard, qui se reconnectent ou qui attendent, se rétablissent depuis la passerelle au lieu de faire échouer le tour.
- Les passerelles sans surveillance ne gèlent plus et ne sortent plus sur un hook de shell.
- Le catalogue accueille hermes-whatsapp-voice, scalekit et completion-sound, et fish-audio passe en v1.7.7.
- Les helpers de découverte et de recherche de l'outil skills reçoivent des noms publics.

> Sources : [@iamlukethedev, Hermes merged 55 PRs on October 18, 19 octobre 2026](https://x.com/iamlukethedev/status/2111997878998835226)

## vibeline, une frise des sessions de l'agent

witcheer a présenté le 19 octobre vibeline, un plugin communautaire pour Hermes Agent qui dessine la chronologie des sessions de l'agent. Dans sa démonstration, chaque sous-agent se ramifie au moment où il est lancé, et un clic sur une étape montre ce qui s'y est passé.

> Sources : [@witcheer, new community plugin for Hermes Agent: vibeline, 19 octobre 2026](https://x.com/witcheer/status/2112129130653536410)

## Hermes Wingtips #106, rattraper les messages Telegram hors ligne

witcheer a publié le 19 octobre le conseil Hermes Wingtips #106. Par défaut, quand la passerelle de Hermes Agent démarre, elle saute les messages Telegram arrivés pendant qu'elle était éteinte. Pour un agent qui tourne sur un ordinateur en veille ou éteint la nuit, une seule commande suffit :

`hermes config set platforms.telegram.extra.drop_pending_on_cold_boot false`

Au démarrage suivant, ces messages arrivent, dans l'ordre.

> Sources : [@witcheer, Hermes Wingtips #106: Telegram messages sent while your agent was off, 19 octobre 2026](https://x.com/witcheer/status/2112083830148649392)

## Demander à Hermes de répartir ses profils

witcheer a partagé le 19 octobre une invite à copier-coller pour celles et ceux qui utilisent un seul Hermes Agent pour le travail, la maison et le reste. On lui demande si une partie mérite un agent à soi : il relit les conversations passées et sa mémoire, puis indique quelles tâches restent avec lui et lesquelles obtiennent leur propre profil, avec la commande pour chacune.

> Sources : [@witcheer, using one Hermes Agent for work, home and everything in between, 19 octobre 2026](https://x.com/witcheer/status/2112166878915534951)

## Un studio de jeu bricolé avec Hermes

Teknium a annoncé le 19 octobre vouloir transformer Hermes Agent en studio de jeu bricolé. iamlukethedev a détaillé l'idée : Hermes écrit déjà du code, produit des images, fait de la voix et lance ses propres sous-agents. Mis en boucle, cela donne un petit studio : un agent écrit la logique du jeu, un autre les sprites et les visuels, un autre la musique et le son, un dernier joue la version compilée et relève les défauts.

> Sources : [@Teknium, Going to make hermes agent into a DIY game dev studio, 19 octobre 2026](https://x.com/Teknium/status/2112092888821842088) et [@iamlukethedev, Hermes already writes code, makes images, does voice, 19 octobre 2026](https://x.com/iamlukethedev/status/2112100287599284537)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
