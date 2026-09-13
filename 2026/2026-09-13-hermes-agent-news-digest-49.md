# Hermes Agent Quotidien #49

Cette édition revient sur l'appel de Teknium à tester l'écran de bot avant sa sortie,
sur le cap des trois mille contributeurs franchi par le projet, sur le
soixante et onzième numéro des Wingtips consacré à la reprise d'une session
lancée depuis un script, sur l'adoption de Hermes comme worker navigateur par
Puppetmaster, sur une page qui rassemble les explications de release, sur un
prompt d'audit de configuration et sur deux réglages mesurés qui raccourcissent
l'attente de préremplissage en local. Aucune release n'a été publiée depuis la
v0.21.2 du 11 septembre.

## L'écran de bot part en relecture avant sa sortie

Teknium a demandé le 12 septembre des relectures et des tests sur l'affichage à
distance d'une passerelle, en invitant à envoyer agents et cerveaux sur la
demande de tirage concernée pour la nettoyer avant publication.

La demande de tirage #108914 va plus loin qu'un simple affichage : un bot installé
sur une passerelle Linux sans écran reçoit son
propre bureau Xfce, que Hermes Desktop diffuse en direct. On peut prendre la main
pour se connecter ou résoudre une authentification à deux facteurs, puis rendre
l'écran au bot, qui poursuit avec la session ouverte.

Le reste de la description précise les garde-fous. La direction de l'écran passe
par un bail, un seul pilote à la fois, agent ou personne, et un filtre côté
serveur refuse les événements de clavier et de souris des spectateurs qui ne
détiennent pas ce bail. Les actions de `computer_use` sont refusées avec le code
`human_has_control` tant qu'une personne pilote, et deux actions demandent ou
attendent explicitement la main. Le démarrage automatique du bureau reste
désactivé par défaut. Trois surfaces y mènent dans l'application : une vignette
vivante en tête du panneau des tâches planifiées, rafraîchie toutes les quatre
secondes et en lecture seule, une ligne Screen sous chaque en-tête de passerelle
ou de profil dans la barre des sessions, et un clic droit sur un bot. Le panneau
noVNC indique qui détient la main et propose les boutons de prise et de retour de
contrôle. Quand les paquets manquent sur l'hôte, la même fenêtre propose de les
installer, avec une demande de mot de passe administrateur masquée. En ligne de
commande, `hermes computer-use screen` prend les sous-commandes `status`, `start`,
`stop` et `install`.

Une relecture indépendante a relevé cinq problèmes de priorité haute et un de
priorité moyenne ; tous ont été reproduits, corrigés et revérifiés sur un écran
Xvnc et Xfce réel. La demande de tirage reste ouverte et compte vingt
participants.

> Sources : [@Teknium, Would anyone like to review or test remote gateway viewing?, 12 septembre 2026](https://x.com/Teknium/status/2098881098885595149) et [Demande de tirage #108914, Bot Screen, teknium1, 12 septembre 2026](https://github.com/NousResearch/hermes-agent/pull/108914)

## Hermes Agent franchit les trois mille contributeurs

Teknium a annoncé le 12 septembre que Hermes Agent a atteint 3 000 contributeurs,
en remerciant les développeurs qui ont travaillé à rendre le projet meilleur pour
tous.

Le jalon s'inscrit dans une progression continue. Les notes de v0.21.0, publiées
le 31 août, créditaient plus de 760 contributeurs sur la fenêtre de la release,
et le projet avait franchi la barre des 100 000 demandes de tirage début
septembre.

> Source : [@Teknium, Hermes Agent has just hit 3000 contributors, 12 septembre 2026](https://x.com/Teknium/status/2098800012549619996)

## Wingtips #71 : reprendre une conversation lancée depuis un script

Dans le soixante et onzième numéro des Wingtips, witcheer traite le cas d'un
appel à Hermes Agent depuis un script ou une tâche planifiée, lancé avec
`hermes -z`. L'appel suivant peut reprendre la même conversation : en ajoutant
`--resume latest`, les tours précédents reviennent avec la réponse, de sorte
qu'un second prompt s'appuie sur le premier. L'identifiant ou le titre d'une
session fonctionne à la place du mot-clé `latest`. C'est le même agent, les mêmes
outils et les mêmes skills que dans une conversation normale, sans la couche
interactive.

La référence des commandes confirme les deux extrémités du mécanisme. `hermes -z`
est l'entrée scriptée pure : un prompt entre, le texte de la réponse finale
sort, rien d'autre sur la sortie standard ni sur la sortie d'erreur, sans
bannière, indicateur d'activité ni aperçu d'outil, et `--usage-file` écrit en
plus un rapport d'usage en JSON. L'option globale `--resume <session>` reprend
une session par identifiant ou par titre, le mot-clé `latest` reprenant la plus
récente, et `--in <dir>` limite la recherche à l'espace de travail du
répertoire donné.

> Sources : [@witcheer, Hermes Wingtips #71 : hermes -z --resume, 13 septembre 2026](https://x.com/witcheer/status/2099034806466015383) et [CLI Commands Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)

## Puppetmaster adopte Hermes comme worker navigateur

witcheer a relevé le 12 septembre qu'un projet communautaire d'essaims de
travailleurs de code a choisi Hermes Agent comme worker navigateur. L'orchestrateur
lance des travailleurs indépendants, confie une tâche à chacun et conserve ce qui
remonte, afin qu'un travail puisse être inspecté et repris. Pour tout ce qui
réclame un vrai navigateur, il préfère Hermes : le worker tourne sans écran, la
boîte à outils navigateur passe directement, et une page hébergée sur un réseau
privé bascule sur le moteur local de Hermes.

Le fichier `docs/ADAPTERS.md` du dépôt Puppetmaster documente l'adaptateur
correspondant. Il appelle la ligne de commande de Hermes en mode sans interface et
sert aussi bien de worker d'analyse, en lecture seule, que de worker d'édition
complète. Deux particularités de Hermes y sont traitées explicitement : le
processus tue son propre groupe de processus à la sortie, ce qui impose un
lancement dans une session séparée pour que le démontage n'atteigne jamais
l'orchestrateur, et le code de retour n'est pas fiable, si bien qu'un worker
d'édition est jugé sur le diff git capturé et un worker d'analyse sur la sortie
standard analysée. Les travailleurs Hermes reçoivent aussi le contexte CodeGraph
pertinent quand le dépôt en contient un. L'essaim navigateur du projet s'appuie
sur Hermes pour cette raison, moteur local de repli compris pour les hôtes
accessibles seulement par réseau privé, l'adaptateur sans navigateur restant la
solution de repli, Cursor, Claude Code et Codex n'ayant pas de navigateur sans
interface. Une commande
d'installation enregistre le serveur MCP du projet dans la configuration de
Hermes, y branche des accroches de cycle de vie et y dépose une skill dédiée.

Le dépôt `professorpalmer/Puppetmaster` se présente comme un plan de contrôle
neutre pour essaims d'agents à état durable, sous licence MIT, publié sur PyPI
sous le nom `puppetmaster-ai`. Sa release v0.9.69 a fait de Hermes un adaptateur
de première classe, validé de bout en bout.

> Sources : [@witcheer, a community project that runs swarms of coding workers picked Hermes Agent as its browser worker, 12 septembre 2026](https://x.com/witcheer/status/2098713900770369859) et [professorpalmer/Puppetmaster, docs/ADAPTERS.md, dépôt GitHub](https://github.com/professorpalmer/Puppetmaster/blob/main/docs/ADAPTERS.md)

## Les explications de release réunies sur une page

witcheer a rassemblé le 12 septembre sur une seule page toutes les explications de
release qu'il a écrites pour Hermes Agent. Le principe exposé : quand Nous
Research publie une nouveauté, l'annonce dit de quoi il s'agit, puis, quelques
jours plus tard, une fois les questions arrivées, il écrit ce que la fonction
fait et comment s'en servir, en vérifiant chaque point contre la documentation.

La page recense sept entrées, de la plus récente à la plus ancienne : Hermes sur
Omarchy le 9 septembre, la recherche web sans clé le 7, la messagerie entre bots
le 5, le pilotage des sous-agents en direct le 3, la centrale de commande MCP le
2, `/bg` contre `/btw` le 1er septembre, et la navigation sur un profil réel le
30 août. Chaque page reprend le texte publié sur X, et les deux premières étaient
des Wingtips avant que cette série ait son nom. La méthode est décrite aussi :
la graine est le flot de questions posées sous l'annonce sur X, reddit et
Discord, chaque mécanique est vérifiée contre la documentation en ligne, et
contre la source au tag de release quand la documentation est en retard, le
dispositif est essayé sur sa propre machine quand la fonction s'adresse à
l'agent, et le texte reste sobre, en étapes numérotées avec un lien vers la
documentation.

> Sources : [@witcheer, every Hermes Agent release explainer I have written, on one page, 12 septembre 2026](https://x.com/witcheer/status/2098860721928847420) et [Hermes release explainers, hermes recipes](https://notwitcheer.github.io/hermes-recipes/explainers/)

## Un prompt pour faire auditer sa configuration par l'agent

witcheer a publié le 12 septembre un prompt à recoller dans une conversation
neuve pour savoir ce que l'agent changerait à sa propre installation. L'agent
lance ses deux commandes de diagnostic, lit le rapport face à l'usage réel, et
rend trois changements avec la ligne exacte de chacun, le prompt complet étant
placé en premier commentaire.

Ce prompt pose trois principes. Le premier est la lecture seule : lancer
`hermes doctor` et `hermes dump`, lire la sortie et s'arrêter là, sans modifier
fichier, configuration ni installation. Le deuxième est le nombre : retenir les
trois constats qui comptent le plus pour l'usage réel, une ligne chacun, le reste
allant en note de bas de page. Le troisième est la précision : pour chaque
changement, donner la ligne `hermes config set` qui l'applique et dire en mots
simples ce qu'elle fait. Les instructions enchaînent ensuite cinq étapes, relevé
des contrôles qui ne passent pas, relevé du modèle, du fournisseur et des
réglages qui s'écartent des valeurs par défaut, confrontation à l'historique de
la session, rédaction des trois changements, puis attente : l'agent montre la
liste et laisse l'utilisateur exécuter les commandes lui-même.

> Source : [@witcheer, want to know what your Hermes Agent would change about its own setup?, 12 septembre 2026](https://x.com/witcheer/status/2098769643599020208)

## Deux réglages qui effacent l'attente de préremplissage

witcheer a mesuré le 13 septembre deux réglages de `llama-server` qui répondent
au reproche le plus répété sur les modèles locaux, l'attente du premier jeton à
chaque requête quand un agent de code présente un long prompt. Les mesures
portent sur Qwen3.8-27B Q6_K servi par llama.cpp sur une seule RTX 5090, avec un
lot de un, 304 requêtes et une variable changée à la fois.

La mise en cache du préfixe, sur un même prompt système réutilisé avec une
nouvelle question, fait passer l'attente du premier jeton de 1,004 à 0,069
seconde sur un prompt de 2 954 jetons, et de 3,814 à 0,086 seconde sur un prompt
de 11 570 jetons, sans toucher à la vitesse de décodage. Le décodage spéculatif,
mené avec la tête de prédiction multiple livrée dans le même fichier de modèle et
deux jetons de brouillon (n = 2), fait passer le décodage de 61 à 109 jetons par
seconde en prose, 113 en conversation, 139 en code et 144 en texte répétitif,
pour un coût de 9 millisecondes sur l'attente du premier jeton. Les deux cumulés,
une réponse courte au contexte de 11 570 jetons descend de 4,25 à 0,30 seconde.

Le rapport détaillé ajoute les limites et les nuances. Le mode à quatre jetons de
brouillon (n = 4) atteint 168 à 184 jetons par seconde en code et en texte
répétitif mais perd 5 à 8 pour cent face au mode à deux en prose et en
conversation, et la recherche par n-grammes ne donne rien sur des réponses de
256 jetons. La méthode complète et le détail par modèle sont publiés dans le
dépôt de mesure de l'auteur, avec un relevé de non-régression : la sortie
spéculative est identique octet pour octet au décodage glouton simple sur 59 pour
cent des réponses, et les treize divergences examinées sont toutes des
basculements vers le second choix du modèle cible, sur un écart de 0,004 à 0,133
nat et une médiane de 0,030. Les limites assumées restent un seul modèle, une
seule quantification, une seule version de llama.cpp, un lot de un, des réponses
de 256 jetons et 32 paires de prompts.

> Sources : [@witcheer, two llama-server flags remove most of that wait, 13 septembre 2026](https://x.com/witcheer/status/2099095882444538285) et [Speculative decoding and prefix caching on one RTX 5090, Qwen3.8-27B Q6_K, rapport llm-bench-rig, 13 septembre 2026](https://github.com/notwitcheer/llm-bench-rig/blob/main/reports/spec-cache-study-qwen38.md)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
