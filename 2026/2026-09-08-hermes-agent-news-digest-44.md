# Hermes Agent Quotidien #44

Cette édition revient sur la release de correctifs v0.21.1, sur le nettoyage
automatique des sessions terminées documenté au soixante-sixième numéro des
Wingtips, sur la documentation de la délégation qui précise désormais la sortie
JSON des sous-agents, sur la refonte du Nous Portal, sur un guide pour traquer
la consommation de jetons, et sur une mesure de l'efficacité d'un affinage de
Qwen 3.8.

## Hermes Agent v0.21.1, release de correctifs

Le 7 septembre, teknium1 a publié la release v0.21.1 (tag v2026.9.7), une
release de correctifs qui regroupe l'état courant de la branche principale
depuis v0.21.0 pour les déploiements étiquetés et les consommateurs en aval.

Mesuré au commit de référence, l'intervalle ouvert depuis v0.21.0 compte 5 139
commits hors fusion dans 4 364 fichiers modifiés (+601 014 / −768 419 lignes),
et 632 demandes de tirage fusionnées au moment de la préparation. Le regroupement
couvre la modularisation du code, le travail de performance sur les opérations
fichier et au démarrage, les mises à jour de fournisseurs et de modèles, les
contrôles de session et les annotations de navigateur du bureau, les améliorations
d'autorisation MCP, les correctifs de planification et de livraison des tâches
cron, et des gains de fiabilité de la délégation. La release ne prétend pas
énumérer chaque fonctionnalité de l'intervalle : les notes complètes devraient
accompagner v0.22.0. La mise à jour se fait avec `hermes update`.

> Sources : [Hermes Agent v0.21.1 (v2026.9.7), release GitHub, teknium1, 7 septembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.7) et [flux des releases, dépôt hermes-agent](https://github.com/NousResearch/hermes-agent/releases.atom)

## Wingtips #66 : le nettoyage automatique des sessions

Dans le soixante-sixième numéro des Wingtips, witcheer aborde ce que deviennent
les sessions terminées que plus personne ne rouvrira. Hermes conserve chaque
conversation pour pouvoir la reprendre ou la chercher plus tard, mais une
passerelle ou un montage cron actif accumule vite des sessions closes
inutilisées.

La documentation répond avec `sessions.auto_prune`, activé par défaut depuis
une évolution récente. Quand il est à `true`, les sessions terminées inactives
depuis `sessions.retention_days`, 90 jours par défaut, sont purgées au démarrage
de l'interface, de la passerelle ou du cron. Après une purge qui a effectivement
retiré des lignes, la base `state.db` est compactée par `VACUUM` pour récupérer
de l'espace disque, mais à deux conditions : au moins 30 jours se sont écoulés
depuis le dernier `VACUUM` réussi, et plus de 25 % des pages du fichier sont
récupérables ; une base dense ne paie pas une réécriture complète pour quelques
mégaoctets. La purge tourne au plus une fois par `sessions.min_interval_hours`,
24 heures par défaut, un horodatage conservé dans `state.db` lui-même pour être
partagé entre tous les processus Hermes du même répertoire d'accueil. Sans
purge, le fichier grossit sans borne, jusqu'à plusieurs gigaoctets en quelques
semaines sur une installation passerelle plus cron ; qui veut tout garder peut
mettre `sessions.auto_prune: false`.

> Sources : [@witcheer, Hermes Wingtips #66 : sessions[.]auto_prune, 8 septembre 2026](https://x.com/witcheer/status/2097201422844436642) et [Sessions, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)

## La délégation précise la sortie attendue des sous-agents

witcheer a signalé le 8 septembre un nouveau passage d'enrichissement de la
documentation, encore façonné par les questions posées. Le site met à jour la
délégation : les valeurs par défaut actuelles sont désormais écrites, et une
section s'ajoute sur `output_schema` pour qu'une réponse de sous-agent revienne
dans la forme JSON demandée.

La documentation décrit le contrat. Chaque tâche de `delegate_task` peut porter
un `output_schema`, un objet JSON Schema contre lequel la réponse finale de
l'enfant doit se valider. Le sous-agent voit le schéma d'avance comme contrat de
sortie ; à la réception, le parent valide, et en cas d'échec renvoie à l'enfant
une seule boucle de correction bornée portant les erreurs de validation mot à
mot, sans recoller le schéma. Le résultat de la tâche gagne alors `schema_valid`
et, en cas d'échec, `schema_errors`. Le conseil posé dans la doc : garder un
schéma indulgent, ne demander que les champs réellement lus ; les tâches sans
`output_schema` ne changent pas de comportement.

> Sources : [@witcheer, Hermes Agent documentation got another round of updates, 8 septembre 2026](https://x.com/witcheer/status/2097321792872345654) et [Subagent Delegation, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)

## Le Nous Portal fait peau neuve

witcheer a présenté le 8 septembre, dans une vidéo commentée, ce que montre
chaque page du Nous Portal récemment refondu. La page d'accueil, l'aperçu,
résume le principe : une seule connexion relie Hermes au catalogue de modèles,
aux outils hébergés et à l'hébergement cloud, et la section pour démarrer donne
les trois voies d'entrée, dont une clé API pour son propre code.

La page d'accueil du portail confirme cette refonte. Le compte unique alimente
le catalogue de plusieurs centaines de modèles des différents laboratoires,
avec des options gratuites et des remises réservées au portail, la passerelle
d'outils dont l'usage facture les mêmes crédits que les modèles, et
l'hébergement cloud qui fait tourner l'agent sans arrêt et prélève les coûts de
serveur sur le solde de crédits. Les abonnements se déclinent par paliers, Pro
à 100 dollars de crédits mensuels avec un plafond de report de 50 dollars, Ultra
à 200 dollars avec 220 dollars de crédits. La vidéo prolonge la mise en avant
récente de l'offre du portail, déjà couverte par ce quotidien à l'occasion de la
réduction de moitié.

> Sources : [@witcheer, we recently revamped Nous Portal, 8 septembre 2026](https://x.com/witcheer/status/2097284608177864967) et [Nous Portal](https://portal.nousresearch.com/)

## Où passent vraiment vos jetons Hermes

witcheer a relayé le 7 septembre un point de départ pour comprendre comment
fonctionnent jetons et contexte dans Hermes Agent. Le contexte, l'usage, le coût
et le stockage sont quatre choses distinctes, et Hermes donne une vue sur
chacune : `/context all` pour ce que contient la fenêtre, `hermes prompt-size`
pour la taille du prompt, et ainsi de suite selon la lecture.

Le message cite un article de Hermes Release Watch intitulé « Where Your Hermes
Tokens Are Actually Going », un guide pratique pour trouver ce qui remplit le
contexte, couper les frais inutiles et dépenser son budget de modèle plus
intelligemment. Le constat de départ : la plupart des gens remarquent le
gaspillage de jetons quand l'indicateur de contexte commence à monter. Le sujet
prolonge les Wingtips et les récents échanges sur la gestion du contexte déjà
couverts par ce quotidien.

> Sources : [@witcheer, if you want to understand how tokens and context work in Hermes Agent, 7 septembre 2026](https://x.com/witcheer/status/2096965743204008279) et [Where Your Hermes Tokens Are Actually Going: How to Find the Waste and Fix It, Hermes Release Watch](https://x.com/i/article/2096769133232947200)

## Qwopus 3.8 Flash, environ deux fois plus efficace

witcheer a mesuré le 8 septembre sur sa carte RTX 5090 l'affinage
Qwopus 3.8 27B Flash, dérivé de Qwen 3.8 27B et entraîné à raisonner plus
efficacement, contre son modèle de base. D'après son relevé, le gain
d'efficacité atteint environ deux fois : sur GPQA-diamond en mode raisonnement,
méthode gloutonne, 198 questions, la variante Flash obtient 70,7 % avec 4 229
jetons par bonne réponse en 2,7 heures.

Le message s'appuie sur l'annonce de KyleHessling, le 4 septembre, qui présentait
cet affinage comme l'un des plus grands sauts de valeur ajoutée jamais engagés
dans un affinage, très proche du modèle de base à haut niveau de raisonnement
mais nettement plus économe dans sa chaîne de pensée, parfois d'un facteur dix.
L'intérêt porte ici sur l'usage de tels modèles locaux dans Hermes Agent, comme
l'illustre aussi une vidéo de witcheer sur le retour aux modèles locaux.

> Sources : [@witcheer, Qwopus 3.8 27B Flash is a fine-tune of Qwen 3.8 27B, 8 septembre 2026](https://x.com/witcheer/status/2097209459600671072) et [@KyleHessling1, Qwopus 3.8 27B Flash is out now, 4 septembre 2026](https://x.com/KyleHessling1/status/2095885740517314985)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
