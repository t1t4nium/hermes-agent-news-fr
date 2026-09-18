# Hermes Agent Quotidien #54

Cette édition revient sur la direction annoncée pour Hermes Agent, un noyau
allégé et davantage de plugins, sur la levée du voile autour du modèle furtif
Union Alpha, révélé comme le système de routage Pareto 26.9, sur le
soixante-seizième numéro des Wingtips consacré aux raccourcis vi dans le CLI,
sur un plugin communautaire qui met une équipe de profils Hermes à la tête d'un
dépôt, et sur un avertissement de la communauté à propos d'un service tiers
portant le nom Hermes. Aucune release n'a été publiée depuis la v0.21.3 du
14 septembre.

## Un noyau allégé et davantage de plugins

Teknium a annoncé le 17 septembre la direction prise par Hermes Agent : rendre
Hermes plus proche de Pi, et moins d'OpenClaw. witcheer a précisé le même jour
la ligne directrice en une phrase : un noyau plus léger et beaucoup plus de
plugins. Hermes reste un agent assistant personnel, mais le noyau embarque
moins de fonctionnalités par défaut, pour qu'il y ait moins à comprendre à
l'installation et moins à maintenir côté Nous Research. Les intégrations
deviennent des plugins, ajoutés depuis le catalogue, relus et installés par
nom, qu'il s'agisse d'une autre plateforme de messagerie, d'un nouveau panneau
dans Hermes Desktop ou d'un outil de niche.

iamlukethedev a apporté le contexte sur ce que signifie concrètement cette
orientation. Les fournisseurs de mémoire sont le premier banc d'essai : au lieu
que Hermes regroupe et maintienne chaque intégration, celles-ci vivent dans les
dépôts de leurs créateurs et se distribuent par le nouveau catalogue de plugins.
Moins de code embarqué, moins de gonflement, moins de maintenance dans le
noyau, plus de responsabilité pour les créateurs de plugins, et une
découvrabilité réelle grâce au catalogue. Hermes reste un agent personnel,
l'écosystème autour devient plus modulaire.

> Sources : [@Teknium, We are going to lean into making Hermes more like Pi, and less like OpenClaw, 17 septembre 2026](https://x.com/Teknium/status/2100645382552428963), [@witcheer, our focus for Hermes Agent right now, in one line: a leaner core and a lot more plugins, 17 septembre 2026](https://x.com/witcheer/status/2100673008897548704) et [@iamlukethedev, Important context on what "making Hermes more like Pi" actually means, 17 septembre 2026](https://x.com/iamlukethedev/status/2100661727503544439)

## Union Alpha était Pareto 26.9

Le mystère du modèle furtif Union Alpha a été levé le 18 septembre. tonbistudio
a raconté que son « détective Hermes » avait vu juste : il était sceptique sur
la théorie multi-modèles de Hermes, mais il a été annoncé que Union Alpha était
en réalité un système de routage de modèles appelé Pareto 26.9, signé
@TheUnbiasedCo. Hermes avait remarqué que le modèle se comportait comme une
combinaison de plusieurs modèles déjà testés, et, avec des indices tirés de la
documentation Cloudflare, en avait conclu qu'il routait plusieurs modèles.

L'article de révélation publié par @unionalphaai confirme le dispositif. Pareto
n'est pas un jeu de poids unique, mais un système : plusieurs modèles, ouverts
et de pointe, travaillent sur la même tâche, avec un harnais qui vérifie le
travail et fait appel à un modèle plus fort quand la tâche l'exige. Il n'y a pas
eu d'entraînement. Les versions précédentes de Pareto ont appris à mesurer
quels modèles sont exceptionnellement bons à quelles tâches, et l'équipe pense
que les routeurs du futur ressembleront à des modèles. La demande a atteint des
milliards de jetons par minute quelques heures après le lancement, rendant le
modèle inutilisablement lent, et AWS a triplé la capacité du jour au lendemain.
Le prix prévu est de 2,50 dollars pour l'entrée, 0,25 pour le cache et 7,50
pour la sortie par million de jetons, moins du quart du prix catalogue
d'Astra. La fiche OpenRouter confirme que Union Alpha était un modèle furtif
développé et opéré par Unbiased, révélé comme Pareto, et que la période
gratuite est terminée.

> Sources : [@tonbistudio, Turns out Detective Hermes was right!, 18 septembre 2026](https://x.com/tonbistudio/status/2100814420205093104), [Union Alpha is Pareto 26.9, article @unionalphaai, 18 septembre 2026](https://x.com/i/article/2100722366200557603) et [Union Alpha, fiche modèle OpenRouter](https://openrouter.ai/stealth/union-alpha)

## Wingtips #76 : les raccourcis vi dans le CLI

Le soixante-seizième numéro des Wingtips traite de `display.vim_mode`, un
réglage du CLI de Hermes Agent. La boîte de saisie où l'on tape son message à
l'agent utilise par défaut les touches d'édition standard du terminal. Pour
ceux qui tapent en vim toute la journée, cette boîte peut adopter les touches
vi : Échap passe en mode NORMAL, la touche i en mode INSERT.

La page de configuration détaille le réglage. `display.vim_mode` est une clé
booléenne, propre au CLI, qui active les raccourcis vi/vim dans le composeur
d'entrée, avec le mode NORMAL/INSERT/REPLACE affiché en direct à droite de la
barre d'état. Le réglage est lu au démarrage et ne se modifie qu'à la
configuration, sans bascule en cours de session.

> Sources : [@witcheer, Hermes Wingtips #76: display.vim_mode, 18 septembre 2026](https://x.com/witcheer/status/2100853054970990803) et [Configuration, Display Settings, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Une équipe de profils Hermes à la tête d'un dépôt

witcheer a relayé le 18 septembre un plugin construit par un membre de la
communauté, qui place une équipe de profils Hermes en charge d'un dépôt dans la
durée. À chaque cycle, le plugin vérifie d'abord l'état réel du dépôt (git,
tests, CI), transforme ce qu'il trouve en travaux proposés sur un tableau
Kanban, et attend l'approbation avant toute modification. On fixe la portée
autorisée, de la lecture seule à l'ouverture de demandes de tirage.

> Sources : [@witcheer, a Hermes Agent community member built a plugin that puts a team of Hermes profiles in charge of a repo over time, 18 septembre 2026](https://x.com/witcheer/status/2100876902663618594)

## Un avertissement sur un service tiers et le rappel de la licence

Un compte de veille de la communauté, HermesWatcher, a publié le 18 septembre
un avertissement à propos d'iHermes, un service tiers qui porte le nom Hermes.
Selon le compte, deux utilisateurs distincts, qui n'avaient fourni aucun
contexte personnel, se sont vu montrer des informations personnelles liées à
d'autres personnes, dont des prénoms d'enfants, des villes et codes postaux,
des emplois et lieux de travail, des détails financiers et familiaux. Le compte
recommande de ne pas connecter de comptes sensibles ni de fournir
d'informations personnelles à ce service, et soulève des questions sur
l'isolation entre utilisateurs et la gestion de la mémoire. Ces affirmations
proviennent d'un compte communautaire et n'ont pas été vérifiées
indépendamment.

witcheer a rappelé le même jour un point de vigilance sur tout produit portant
le nom Hermes. Hermes Agent est open source, sous licence MIT : n'importe qui
peut reprendre le code pour construire un service hébergé, un plugin ou un
projet communautaire, et beaucoup le font. Un produit construit sur Hermes
Agent n'est pas fabriqué ni exploité par Nous Research. Les surfaces officielles
sont le dépôt Hermes Agent, la documentation, le Nous Portal et Hermes Desktop.
Avant de connecter ses comptes ou de partager des données personnelles avec un
service construit sur Hermes, witcheer conseille de vérifier qui l'exploite,
quel modèle il utilise, où les données sont stockées et qui peut les lire, et
si le code est public.

> Sources : [@HermesWatcher, URGENT WARNING TO ANYONE USING OR CONSIDERING iHermes, 18 septembre 2026](https://x.com/HermesWatcher/status/2100765429660848203) et [@witcheer, one thing to keep in mind with any product that carries the Hermes name, 18 septembre 2026](https://x.com/witcheer/status/2100822183287148715)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
