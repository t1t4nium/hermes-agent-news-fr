# Hermes Agent Quotidien #57

Cette édition revient sur la mise en ligne du catalogue de plugins de Hermes
Agent, avec ses pages de détail et la garantie d'une révision par un mainteneur, sur le
soixante-dix-neuvième numéro des Wingtips consacré à la désactivation globale
de jeux d'outils, sur un correctif de compaction pensé pour les modèles locaux à
petite fenêtre, sur une journée de fusion record de 419 demandes de tirage, sur
l'arrivée de GLM-5.3 FlashX et sur une nouvelle capacité de connexion aux sites
web. Toujours aucune release publiée depuis la v0.21.3 du 14 septembre.

## Le catalogue de plugins est en ligne

Hermes Agent dispose désormais d'un catalogue de plugins intégré. tonbistudio en
a présenté une vidéo d'introduction le 21 septembre, montrant comment installer
rapidement des plugins, avec trois exemples : resetwatch, hermes-newswire et
hermes-office. Teknium a confirmé le même jour que la mise en ligne était
effective : chaque plugin reçoit une page complète, son readme injecté, avec un
tri par récence et une vue de tous les plugins par auteur.

La page du catalogue en détaille le fonctionnement. Le compteur affiche
222 entrées au total, dont 5 officielles et 217 communautaires, réparties en
neuf catégories : bureau, mémoire, plateformes, web et navigateur, outils, voix,
automatisation, modèles et général. Chaque entrée porte une invite
`hermes plugins install <nom>`, pointe vers le dépôt et sa documentation, et
liste ses outils, hooks et variables d'environnement.

witcheer a expliqué comment un plugin entre au catalogue, en quatre lignes.
Chaque entrée arrive par une demande de tirage lue par un mainteneur, puis
l'entrée épingle un commit exact : l'auteur qui pousse du code à son dépôt ne
change rien à ce que le catalogue installe, puisque `hermes plugins install
<nom>` récupère précisément la version revue. Avant d'installer quoi que ce
soit, la page de détail montre donc le commit exact épinglé, les outils, hooks
et variables d'environnement que le plugin déclare, et le readme de ce commit
examiné.

> Sources : [@tonbistudio, Hermes Agent now has a built-in Plugins Catalog!, 21 septembre 2026](https://x.com/tonbistudio/status/2101912099689840645), [@Teknium, Just FYI it's all live now, 21 septembre 2026](https://x.com/Teknium/status/2101932350821257289), [@witcheer, the plugin catalog pages are live, 21 septembre 2026](https://x.com/witcheer/status/2101937414465864080), [@witcheer, how the catalog works, in four lines, 21 septembre 2026](https://x.com/witcheer/status/2101918193568641162) et [Plugin Catalog, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins)

## Wingtips #79 : agent.disabled_toolsets

Le soixante-dix-neuvième numéro des Wingtips traite de `agent.disabled_toolsets`.
Hermes Agent choisit ses outils par plateforme : le CLI, Telegram, Discord et les
autres gardent chacun leur propre liste de jeux d'outils, configurée dans
`hermes tools`. Cette clé constitue une liste placée au-dessus de toutes : un jeu
d'outils nommé ici est retiré partout.

La page de configuration précise le mécanisme. Pour supprimer des jeux d'outils
à travers le CLI et toutes les plateformes de la passerelle en un seul endroit,
on liste leurs noms sous `agent.disabled_toolsets`, par exemple `memory` pour
masquer les outils de mémoire et l'injection `MEMORY_GUIDANCE`, ou `web` pour
n'avoir ni `web_search` ni `web_extract` où que ce soit.

> Sources : [@witcheer, Hermes Wingtips #79: agent.disabled_toolsets, 21 septembre 2026](https://x.com/witcheer/status/2101910495888392672) et [Configuration, Global Toolset Disable, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Une compaction adaptée aux petites fenêtres locales

witcheer a annoncé le 21 septembre un changement de compaction fusionné le jour
même, destiné à celles et ceux qui font tourner Hermes Agent sur un modèle local
à fenêtre de 8 000 à 32 000 jetons. Quand le contexte se remplit, Hermes résume
la partie la plus ancienne de la conversation et conserve la partie la plus
récente mot pour mot. Ce segment protégé était dimensionné en jetons.

La nouveauté tient à ce dimensionnement : pour un grand modèle à large fenêtre,
le coût est mineur ; pour un petit modèle local, garder mot pour mot une fin de
conversation mesurée en jetons garantit une fenêtre de travail réellement
utilisable au lieu d'une piqûre de résumé qui ampute brutalement le tour en
cours.

> Sources : [@witcheer, a compaction change merged today for local model 8k-32k windows, 21 septembre 2026](https://x.com/witcheer/status/2101948838407786863)

## Une journée de fusion record et les providers de processus en plugins

iamlukethedev a signalé le 21 septembre que Hermes avait fusionné 419 demandes
de tirage en une seule journée, et a isolé deux changements à connaître. Les
fournisseurs externes de modèles de processus (process providers) sont désormais
livrés comme plugins autonomes, de sorte que les fournisseurs OAuth et de
process hors arbre apparaissent dans tous les sélecteurs de modèle. En mode bot
et sur le bureau, GPT Live et la synthèse vocale suivent la configuration du bot.

Ces deux points illustrent la direction des derniers développements : des
capacités autrefois enracinées dans le noyau deviennent des plugins
interchangeables, et les modes d'interface, bot et bureau, partagent de plus en
plus les mêmes réglages de voix.

> Sources : [@iamlukethedev, Hermes merged 419 PRs today, 21 septembre 2026](https://x.com/iamlukethedev/status/2101911386721009758)

## GLM-5.3 FlashX arrive dans Hermes Agent

Teknium a annoncé le 20 septembre que GLM-5.3 FlashX est désormais disponible
dans Hermes Agent via Nous Portal et OpenRouter. L'annonce s'accompagne d'un
lien vers le catalogue de modèles, qui élargit les choix offerts aux
utilisateurs sur ces deux canaux.

Ce genre d'ajout illustre la cadence d'intégration de nouveaux modèles dans les
catalogues de fournisseurs pris en charge par Hermes Agent, qui se rééquilibre
au fil des arrivées.

> Sources : [@Teknium, GLM-5.3 FlashX is now available in Hermes Agent through Nous Portal and OpenRouter, 20 septembre 2026](https://x.com/Teknium/status/2101773802418139526)

## La connexion aux sites web se règle d'une phrase

witcheer a résumé le 21 septembre cinq usages immédiats des deux derniers tags de
Hermes Agent, sortis la semaine passée, v0.21.2 et v0.21.3, dont le premier est
la connexion aux sites web. En disant « connecte-moi à GitHub », l'agent remplit
le mot de passe depuis 1Password, Bitwarden ou le coffre chiffré intégré de
Hermes. La capacité s'appuie sur les demandes de tirage #106480 et #107585.

Cette annonce complète le paysage des gestionnaires de mots de passe déjà
supportés par Hermes, et confirme que la capture et le remplissage des secrets
restent une préoccupation centrale des deux patch releases récentes.

> Sources : [@witcheer, two Hermes Agent tags went out last week, v0.21.2 and v0.21.3, 21 septembre 2026](https://x.com/witcheer/status/2101982106486292787)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)