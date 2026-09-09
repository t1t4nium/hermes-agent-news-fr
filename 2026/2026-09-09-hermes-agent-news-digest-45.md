# Hermes Agent Quotidien #45

Cette édition revient sur la Perplexity Search API désormais utilisable comme
moteur des outils web de Hermes, sur l'intégration de première classe de
l'agent dans Omarchy, la distribution Linux agentique de DHH, sur l'arrivée de
GPT-Image-2.5 dans Hermes via les abonnements Codex et fal, sur le conseil des
Wingtips dédié à la commande de diagnostic partagé, et sur l'import des
conversations Claude Code et Codex dans le bureau Hermes.

## La Perplexity Search API comme moteur de recherche de Hermes

NousResearch a annoncé le 9 septembre qu'il est désormais possible d'utiliser
l'API Perplexity Search dans Hermes Agent, rejoint par une annonce de
Perplexity et un message de soutien du cofondateur de Perplexity. La série de
statuts de la nuit couvre le même lancement d'un outil web pour l'agent.

La documentation d'intégration de Perplexity précise le mécanisme. Hermes peut
utiliser Perplexity comme backend de ses outils `web_search` et `web_extract` :
`web_search` renvoie des résultats classés de la Search API, `web_extract` les
passages pertinents de chaque URL. L'intégration change les outils web, pas le
modèle qui pilote l'agent, et se règle en mettant la clé `PERPLEXITY_API_KEY`
dans `.env` puis les sélections `web.backend`, `web.search_backend` et
`web.extract_backend` sur `perplexity`. Le fournisseur est inclus dans Hermes
v0.21.1 (tag v2026.9.7) et ultérieur, via la demande de tirage 102055. Le
statut de l'équipe Perplexity indique que la Search API donne accès à un index
de plus de 400 milliards d'URLs, avec des résultats en temps réel et des
extraits classés par pertinence. Le sujet prolonge le panorama des moteurs
possibles pour les outils web, où le tourniquet sans clé tient une place déjà
documentée par ce quotidien.

> Sources : [@NousResearch, You can now use the Perplexity Search API in Hermes Agent, 9 septembre 2026](https://x.com/NousResearch/status/2097485341250752979), [@perplexitydevs, Perplexity Search API is now available in Hermes Agent, 9 septembre 2026](https://x.com/perplexitydevs/status/2097483428895801607) et [Perplexity web search in Hermes, documentation Perplexity](https://docs.perplexity.ai/docs/getting-started/integrations/hermes)

## Hermes intégré en première classe à Omarchy

NousResearch a annoncé le 8 septembre le support de première classe de Hermes
dans Omarchy, la distribution Linux agentique d'Arch créée par David Heinemeier
Hansson, le créateur de Ruby on Rails. L'application bureau s'installe
depuis le menu AI, ou Hermes se règle comme agent terminal par défaut, et le
thème d'Omarchy définit alors les couleurs de l'application bureau, du TUI et
du CLI.

witcheer détaille la portée pratique : l'application bureau s'installe depuis
le menu AI comme n'importe quelle application Omarchy, et faire d'Hermes
l'agent terminal par défaut lui fait reprendre le thème d'Omarchy dans
l'application, le TUI et le CLI, en un seul jeu de couleurs. Le site officiel
d'Omarchy décrit la distribution comme l'OS malléable pour l'âge des agents,
avec une installation rapide, des agents qui déboguent les problèmes et des
milliers de plugins communautaires. Teknium et witcheer reprennent chacun
l'annonce dans la même fenêtre de temps.

> Sources : [@NousResearch, Hermes now has first-class support in Omarchy, 8 septembre 2026](https://x.com/NousResearch/status/2097403926072987986), [@witcheer, Hermes Agent is now built into Omarchy, 8 septembre 2026](https://x.com/witcheer/status/2097405028076343661) et [Omarchy, site officiel](https://omarchy.org/)

## GPT-Image-2.5 arrive dans Hermes via Codex et fal

Teknium a annoncé le 8 septembre que GPT-Image-2.5 est désormais disponible
dans Hermes Agent à travers les abonnements Codex et l'inférence de fal, et
que l'accès arrivera bientôt sur le Nous Portal. L'annonce accompagne la
parution de ChatGPT Images 2.5 chez OpenAI, présentée comme plus rapide, plus
nette et plus fidèle.

Le communiqué d'OpenAI du 8 septembre confirme les deux modèles d'image
GPT-Image-2.5 Sunburst et GPT-Image-2.5 Flare, disponibles dans l'API, avec
une génération d'images plus rapide, une meilleure fidélité pour des images
plus naturelles et reconnaissables, et des détails cohérents à travers les
éditions multiples. Le sujet prolonge les annonces de modèles récentes déjà
couvertes par ce quotidien, l'intérêt portant ici sur l'ajout de la génération
d'images comme capacité utilisable depuis Hermes.

> Sources : [@Teknium, GPT-Image-2.5 now available in Hermes Agent through Codex subscriptions and @fal, 8 septembre 2026](https://x.com/Teknium/status/2097465800231883091) et [Introducing ChatGPT Images 2.5, OpenAI, 8 septembre 2026](https://openai.com/index/introducing-chatgpt-images-2-5/)

## Wingtips #67 : hermes debug share

Dans le soixante-septième numéro des Wingtips, witcheer présente `hermes
debug share`, la commande à lancer quand on veut poser une question sur ce
qu'Hermes Agent a fait, sur Discord ou dans une issue. Les premières questions
qui reviennent sont toujours les mêmes : quelle version, quel modèle, quel
fournisseur, que disent les journaux. Hermes a une seule commande qui construit
tout le paquet.

Le conseil reprend la forme de la série : montrer la commande, ce qu'elle
rassemble, et quand l'employer. Elle évite de reposer les mêmes questions de
base sur la version, le modèle et le fournisseur avant toute demande d'aide,
et rejoint la collection des Wingtips déjà présentée par ce quotidien.

> Sources : [@witcheer, Hermes Wingtips #67 : hermes debug share, 9 septembre 2026](https://x.com/witcheer/status/2097565476435992883)

## Importer ses conversations Claude Code et Codex dans le bureau

witcheer a listé le 9 septembre cinq changements de la release v0.21.1,
regroupée lundi, utilisables dès aujourd'hui. Le premier, la demande de tirage
104229, permet d'apporter ses conversations Claude Code et Codex dans Hermes
Desktop : ouvrir la palette de commandes, choisir Import session, prévisualiser
la conversation et la continuer dans l'application bureau.

La demande de tirage, portée par teknium1 et intitulée « import foreign
coding-agent sessions from the sidebar », ajoute une entrée Import session à
la barre latérale du bureau. Elle liste les transcriptions des agents de
codage étrangers présents sur la machine hôte, les prévisualise en lecture
seule, et continue une copie sous le profil choisi. C'est l'équivalent bureau
de `hermes sessions import` et de `hermes --resume @claude|@codex`, bâti sur le
même analyseur et le même stockage en base. Le sujet complète la couverture de
la release v0.21.1 déjà faite par ce quotidien en pointant une de ses capacités
précises.

> Sources : [@witcheer, Hermes Agent v0.21.1 shipped on Monday as a rollup, 9 septembre 2026](https://x.com/witcheer/status/2097593332515938514) et [feat(desktop): import foreign coding-agent sessions from the sidebar, PR 104229, dépôt hermes-agent](https://github.com/NousResearch/hermes-agent/pull/104229)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).