# Hermes Agent Quotidien #52

Cette édition revient sur le billet de Nous Research qui raconte le nettoyage du
dépôt de Hermes Agent par 1 393 agents, sur le soixante-quatorzième numéro des
Wingtips consacré au choix de l'hôte qui sert un modèle sur OpenRouter, sur un
composeur unique pour plusieurs sessions dans le bureau, sur la page qui
rassemble les prompts Autopilot et sur un hub vocal familial posé sur un frigo.
Aucune release n'a été publiée depuis la v0.21.3 du 14 septembre.

## Le nettoyage du dépôt par 1 393 agents

Nous Research a annoncé le 15 septembre un billet signé Teknium qui raconte le
nettoyage du dépôt de Hermes Agent par l'agent lui-même. Le point de départ :
plus d'un million de lignes de Python hors tests, dont un fichier
`gateway/run.py` de 34 847 lignes, un chantier repoussé parce qu'il aurait
détourné des ingénieurs des fonctionnalités et des correctifs. La demande est
envoyée le 2 septembre à l'agent habituel de Teknium, avec pour objectif une
baisse d'au moins 30 pour cent du nombre de lignes, l'éclatement des fichiers
monstres, l'unification des fonctions utilitaires et la réduction des chaînes
de conditionnelles.

L'exécution principale a duré environ dix-neuf heures actives et a envoyé 1 393
sous-agents, jusqu'à 218 en parallèle. Après un redémarrage, une session de
continuation et deux tours de relecture communautaire, la demande de tirage a
été fusionnée le 4 septembre, pour une baisse de 34,4 pour cent du code Python
hors tests. Le coût de modèle est estimé à environ 19 300 dollars pour
l'exécution principale, soit près de 25 000 dollars avec les sessions de suivi,
hors temps de relecture humaine. L'estimation de l'effort manuel correspondant
va de 150 000 dollars à 1,8 million de dollars pour une petite équipe sur deux
mois à deux ans.

Le déroulé technique est documenté. L'orchestrateur a mesuré le dépôt et l'a
découpé en 36 groupes sans recouvrement, puis a rédigé les consignes de chaque
ouvrier à partir de l'objectif et des règles accumulées. Les ouvriers
travaillaient dans des copies de travail git séparées, les arbres de délégation
descendant jusqu'à trois niveaux sous l'agent d'origine, lequel coordonnait sans
éditer les fichiers sources. Le tout tournait dans un seul processus Python sur
un poste i7 doté de 64 Go de mémoire, les outils en sous-processus locaux et
l'inférence à distance sur Claude Fable 5.1. Environ cinquante minutes après le
départ, l'expiration du jeton d'authentification du fournisseur a tué
l'exécution, les commits et les consignes des ouvriers survivant sur le disque,
et une session séparée a préparé la reprise.

Les contrôles portaient sur les interfaces : schéma JSON d'un outil inchangé,
sortie de `--help` d'une commande devant rester identique octet par octet,
commit obligatoire après chaque étape vérifiée. Pour `gateway/run.py`, les
ouvriers ont séparé la distribution des messages, le streaming, les appels de
procédure à distance et la gestion du cycle de vie en modules distincts. Deux
régressions ont échappé aux tests existants et ont été corrigées avant la
fusion : des noms publics supprimés au motif qu'aucun appel interne ne les
utilisait, alors que des extensions externes peuvent les importer, et une
réécriture automatisée des appels à `suppress()` qui a modifié la gestion des
exceptions à environ 65 endroits.

Les mesures avant et après figurent dans le billet :

- Le Python hors tests passe de 1 063 826 à 698 363 lignes.
- Les fichiers de plus de 5 000 lignes passent de 37 à 6.
- Les fonctions de plus de 300 lignes passent de 192 à 2.
- La plus longue chaîne de conditions passe de 92 à 9 branches.
- `gateway/run.py` passe de 34 847 à 5 512 lignes.

La question de la lisibilité par un agent a été testée sur un échantillon : en
simulant la recherche de 4 000 symboles dans les deux versions, la moyenne de
jetons renvoyés par recherche tombe de 2 218 à 993 et les recherches exigeant
une seconde fenêtre de lecture de 628 à 184, la médiane augmentant en revanche,
le code étant plus dense à fenêtre de lignes égale. Le découpage a aussi un
coût : plus de modules, plus de dépendances d'importation, des points d'entrée
plus lents à charger, et six fichiers qui dépassent encore 5 000 lignes. Les
données du banc d'essai sont publiées dans un gist.

Les leçons de l'exécution ont été réinjectées dans l'outillage. Les ouvriers
avaient lancé une trentaine d'instances de Pyright consommant environ 8,7 Go,
corrigé depuis par le partage d'un serveur entre les copies de travail avec une
vérification que les diagnostics arrivent bien de chacune. Le dépôt contient
désormais des règles sur la taille des fichiers, la complexité des fonctions et
l'emplacement du nouveau comportement, découpées par zone, ainsi qu'un contrôle
qui signale les noms publics supprimés. La skill `hermes-agent-dev` de Teknium a
été mise à jour automatiquement avec les leçons de ce nettoyage, puis
distribuée aux ingénieurs. witcheer a retenu le lendemain ce qui est
reproductible : `/goal` a maintenu l'objectif actif quand l'agent se serait
arrêté, et les ouvriers venaient d'un seul outil, `delegate_task`, chacun dans
sa propre copie de travail git.

> Sources : [Refactoring Hermes with 1,393 agents, Teknium, blog Nous Research, 15 septembre 2026](https://nousresearch.com/refactoring-hermes-with-1393-agents), [@NousResearch, New blog post: We had a million lines of Python to clean up, 15 septembre 2026](https://x.com/NousResearch/status/2099984561451028913), [@Teknium, My first blog, 15 septembre 2026](https://x.com/Teknium/status/2099996435324518533), [@witcheer, nothing in that run is special to Teknium's setup, 16 septembre 2026](https://x.com/witcheer/status/2100098318361583896) et [PR #102117, dépôt hermes-agent, 4 septembre 2026](https://github.com/NousResearch/hermes-agent/pull/102117)

## Wingtips #74 : choisir l'hôte qui sert un modèle

Le soixante-quatorzième numéro des Wingtips traite du routage d'un modèle sur
OpenRouter : un même nom de modèle est servi par plusieurs hébergeurs, et
OpenRouter choisit l'hébergeur de chaque requête. La section `provider_routing`
de `config.yaml` reprend la main, par exemple pour écarter un hébergeur qui
limite le débit ce jour-là.

La page de la fonctionnalité détaille les réglages. `sort` classe les
hébergeurs par prix, débit en jetons par seconde ou latence du premier jeton,
`only` restreint la requête à une liste d'hébergeurs, `ignore` en exclut
définitivement, `order` fixe un ordre de préférence avec les autres en secours,
`require_parameters` évite les hébergeurs qui abandonnent silencieusement un
paramètre de la requête, et `data_collection` accepte ou refuse l'usage des
invites pour l'entraînement. Une clé `models` permet de fixer un jeu
d'hébergeurs par modèle, la surcharge suivant le modèle sur lequel l'agent se
trouve au moment de l'appel, si bien qu'une bascule par `/model`, un appel de
secours, une tâche planifiée ou un sous-agent sur un autre modèle a ses propres
épingles.

Deux limites sont explicites. Le réglage ne s'applique qu'avec OpenRouter, sans
effet sur une connexion directe à un fournisseur, et il est ignoré sur le Nous
Portal, qui décide du routage de façon centralisée et ne reçoit jamais l'objet
`provider`. Les préférences partent dans le champ `extra_body.provider` des
requêtes de conversation et des résumés de limite d'itérations, les tâches
auxiliaires se réglant à part sous `auxiliary.<tâche>.extra_body`.

> Sources : [@witcheer, Hermes Wingtips #74: provider_routing, 16 septembre 2026](https://x.com/witcheer/status/2100156876209963106) et [Provider Routing, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)

## Un seul composeur pour plusieurs sessions dans le bureau

imbabybrooklyn a montré le 16 septembre une démonstration du bureau où un
composeur unique alimente plusieurs onglets de session : le texte saisi part
vers la session survolée par le curseur. witcheer a repris l'idée le même jour,
plusieurs agents occupés en parallèle et un seul endroit où écrire pour piloter
celui que l'on regarde.

La documentation du bureau décrit la mécanique d'onglets qui porte la
démonstration. Chaque onglet porte une session, ouverte par `Cmd/Ctrl+T` et
parcourue par `Ctrl+Tab` et `Ctrl+Shift+Tab`, tandis que `Ctrl+1` à `Ctrl+9`
sautent directement à une session récente par sa position. Une session peut
aussi être détachée dans sa propre fenêtre, et la sélection de la barre
latérale suit le panneau de conversation qui a le focus.

> Sources : [@imbabybrooklyn, One composer to rule them all; multiple tabs w/ multiple sessions, 16 septembre 2026](https://x.com/imbabybrooklyn/status/2100188485051134401), [@witcheer, several sessions open side by side and one place to type, 16 septembre 2026](https://x.com/witcheer/status/2100189438697455760) et [Hermes Desktop, Windows, tabs & panes, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#windows-tabs--panes)

## Tous les prompts Autopilot sur une page

witcheer a rassemblé le 15 septembre ses prompts Autopilot sur une seule page.
Un Autopilot est une invite à coller dans une conversation Hermes Agent neuve,
qui ne fonctionne que dans un agent parce qu'elle lit la mémoire, les sessions
passées ou la configuration, choses qu'une fenêtre de conversation ne voit pas.

La page des prompts en liste quatre, du plus récent au plus ancien : la revue du
lundi qui s'écrit seule, l'audit de sa propre configuration, la transformation en
skill de ce qui vient d'être fait et l'interview de mémoire pour apprendre à
l'agent comment travaille son utilisateur. Chaque page reprend l'invite telle
qu'elle a été publiée, aucune n'écrit avant un accord explicite, et toutes ont
tourné sur une machine réelle avant publication. L'usage tient en trois étapes :
ouvrir une conversation neuve, coller l'invite entière avec ses balises, puis
répondre à ses questions. Le site héberge aussi la collection des 70 Wingtips,
7 explications de release et un fichier `llms.txt` à donner à un agent.

> Sources : [@witcheer, I put every Hermes Autopilot prompt on one page, 15 septembre 2026](https://x.com/witcheer/status/2099962905651470490) et [Hermes Autopilot prompts, hermes recipes, 15 septembre 2026](https://notwitcheer.github.io/hermes-recipes/prompts/)

## Un hub vocal familial sur le frigo

shantanugoel a publié le 16 septembre une démonstration d'un hub domestique
piloté à la voix, construit autour de Hermes et d'un appareil Zectrix Note 4. On
parle, Hermes traite et retient, et il rappelle ce qui doit l'être. Le dispositif
distingue aussi plusieurs personnes nommées, et il est installé sur le frigo
pour que toute la famille s'en serve. witcheer a salué le travail, un agent avec
lequel toute la famille discute sur le frigo.

> Sources : [@shantanugoel, Built a NousResearch Hermes and voice driven home hub, 16 septembre 2026](https://x.com/shantanugoel/status/2100164527853842574) et [@witcheer, that is super cool - a Hermes Agent the whole family talks to, on the fridge, 16 septembre 2026](https://x.com/witcheer/status/2100175330396815814)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
