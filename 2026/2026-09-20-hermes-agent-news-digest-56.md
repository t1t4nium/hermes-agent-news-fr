# Hermes Agent Quotidien #56

Cette édition revient sur le soixante-dix-huitième numéro des Wingtips consacré
à la politique personnalisable des approbations intelligentes, sur un moteur de
contexte communautaire pour les longues conversations, sur le réglage de la
longueur des réponses au vol et sur un nouveau contrôle d'affichage dans
l'application de bureau. Elle aborde enfin la réponse de Hermes à une
comparaison portant sur la compaction, entre un modèle tiers et son
fonctionnement interne. Aucune release n'a été publiée depuis la v0.21.3 du
14 septembre.

## Wingtips #78 : approvals.smart_policy

Le soixante-dix-huitième numéro des Wingtips traite de `approvals.smart_policy`,
une clé qui prolonge le mode d'approbation intelligent de Hermes Agent. Quand
l'agent veut exécuter une commande terminale jugée risquée, un second modèle
l'examine au préalable, lit la commande et répond d'un mot : approuver, refuser,
ou faire remonter, c'est-à-dire vous demander. Cette clé permet d'ajouter vos
propres règles à cet examen.

La page de configuration détaille le mécanisme. En mode `smart`, un modèle
assistant (guardian LLM) évalue si une commande signalée est réellement
dangereuse : les commandes à faible risque sont approuvées automatiquement pour
cette seule exécution, les commandes réellement risquées sont refusées, et les
décisions incertaines remontent à l'utilisateur. `approvals.smart_policy`
ajoute vos propres règles aux instructions de cet examinateur ; le texte est
inséré dans le message système du modèle gardien, par le canal de confiance,
jamais à côté du texte non fiable de la commande. On peut ainsi resserrer ou
desserrer son jugement selon l'environnement, sans écrire de code, par exemple
faire toujours remonter toute commande qui modifie quelque chose sous `/etc`,
ou approuver par avance les redémarrages docker d'un dossier de déploiement.

> Sources : [@witcheer, Hermes Wingtips #78: approvals.smart_policy, 20 septembre 2026](https://x.com/witcheer/status/2101606053800456228) et [Configuration, Smart Approvals, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Un moteur de contexte pour les longues conversations

witcheer a relayé le 20 septembre un plugin construit par un membre de la
communauté, un moteur de contexte pensé pour les longues conversations. Le
plugin conserve chaque message d'une session dans un stockage SQLite local,
replie les tours les plus anciens en résumés en couches, et construit l'invite
en direct à partir de ces résumés complétés des messages les plus récents.

L'archive est d'abord la valeur sûre : rien ne se perd, tout est écrit dans la
base locale. La fenêtre reste lisible parce que l'ancien est condensé, et le
contexte vivant se recompose à chaque tour à partir des résumés et de la fin de
la session, plutôt que de garder une fenêtre fixe qui écarte brutalement ce qui
dépasse.

> Sources : [@witcheer, a Hermes Agent community member built a context engine plugin for long conversations, 20 septembre 2026](https://x.com/witcheer/status/2101634750473498915)

## La longueur des réponses se règle d'une commande

tonbistudio a montré le 20 septembre comment régler la longueur des réponses de
l'agent en une seule commande terminale : `hermes config set
agent.text_verbosity low/medium/high`. Placer `low` donne des réponses courtes,
`medium` un niveau intermédiaire. Le réglage relève de la section `agent` de la
configuration.

La page de configuration précise la portée du réglage. `agent.text_verbosity`
est une clé indépendante de la profondeur de raisonnement, qui ne s'applique
qu'aux modèles de la famille Responses (les GPT-5 OpenAI et suivants, en direct
sur OpenAI, Codex ChatGPT et Azure). Hermes l'envoie comme champ
`text: {verbosity: ...}` en tête de requête, uniquement sur ces routes ; la clé
n'est jamais envoyée sur `chat_completions`, ni sur les requêtes Anthropic ou
xAI, et une valeur vide ne renvoie rien de plus au fournisseur.

Dans cet esprit de configuration pilotée depuis le CLI, witcheer a rappelé le
même jour une habitude de veille : avant d'écrire la moindre ligne sur un
réglage de Hermes Agent, il interroge l'installation elle-même avec
`hermes config get approvals.mode`, qui affiche la valeur réellement en cours
d'exécution, qu'elle soit celle par défaut ou non, sans avoir à fouiller
`config.yaml`.

> Sources : [@tonbistudio, Ever get tired reading super long responses from your AI agent?, 20 septembre 2026](https://x.com/tonbistudio/status/2101546210238885966), [@witcheer, a habit from this week: before I write a line about a Hermes Agent setting, 20 septembre 2026](https://x.com/witcheer/status/2101665688024731827) et [Configuration, Answer length, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Masquer les blocs de diff dans l'application de bureau

Le produit a mis en ligne le 20 septembre un nouveau contrôle d'affichage dans
l'application de bureau de Hermes Agent : il est possible de masquer les grands
blocs de diff de code dans les réglages, sous l'onglet Apparence. La demande
venait d'une personne proche de l'équipe, et la possibilité de plier ces blocs
n'avait pas été envisagée plus tôt.

Le message invite la communauté à proposer d'autres éléments d'interface à
pouvoir masquer. Le réglage rejoint les commutateurs d'affichage de
l'application, qui visent à alléger la lecture quand les pans de code deviennent
secondaires.

> Sources : [@imbabybrooklyn, You can now hide the big code diffs blocks in Settings→Appearance, 20 septembre 2026](https://x.com/imbabybrooklyn/status/2101496611218104331)

## Compaction : Hermes répond à une comparaison avec Jev

Une comparaison a circulé à propos de la compaction, technique par laquelle un
agent condense une conversation qui s'allonge. Le 19 septembre, Teknium a
répondu à une affirmation selon laquelle Jev, un modèle tiers, rendrait la
compaction plus rapide et meilleure, en donnant les faits tirés d'une évaluation
reproductible. Selon lui, la compaction de Jev souffre de plusieurs problèmes ;
le principal est que, passée sur l'évaluation publique de compaction de Hermes
(que chacun peut exécuter), elle aboutit à une règle programmatique, qui n'a
besoin ni de Jev ni d'aucun autre modèle.

iamlukethedev a résumé le résultat chiffré du test, mené contre Hermes avec la
même évaluation. La compaction de production de Hermes atteint 78,9 % de rappel
à 55 000 jetons, contre 75,5 % pour Jev. Ces chiffres et ces critiques émanent
de l'auteur de Hermes et d'un membre de la communauté, à propos d'un produit
tiers dont la méthode n'a pas été vérifiée indépendamment.

> Sources : [@Teknium, Okay, everyone wants us to give the unbiased facts, 19 septembre 2026](https://x.com/Teknium/status/2101398453578555898) et [@iamlukethedev, This is how agent features should be evaluated, 19 septembre 2026](https://x.com/iamlukethedev/status/2101415185793843340)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)