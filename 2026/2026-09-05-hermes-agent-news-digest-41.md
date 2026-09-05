# Hermes Agent Quotidien #41

Cette édition revient sur l'arrivée de GPT-6 Astra sur le Nous Portal à prix réduit, sur le choix de Perplexity comme backend de recherche web et de scraping, sur un plugin qui range la mémoire longue de l'agent dans un dossier de fichiers Markdown, sur le soixante-troisième numéro des Wingtips consacré au délai d'attente de la compression de contexte, et sur une masterclass vidéo en trois parties dédiée au bureau.

## GPT-6 Astra disponible sur le Nous Portal

OpenAI a présenté GPT-6 Astra comme son modèle le plus intelligent et le mieux aligné, à la pointe sur l'usage d'ordinateur, la navigation web, l'ingénierie logicielle, la cybersécurité, la science et le travail professionnel. Nous Research l'a rendu disponible sur le Nous Portal pour Hermes Agent avec une réduction de 20 %, et Teknium précise que le modèle s'utilise dans Hermes Agent via le portail.

Le catalogue du portail affiche le modèle au prix de 4,00 dollars par million de jetons en entrée et 20,00 dollars en sortie. OpenAI annonce un déploiement progressif : d'abord un ensemble limité d'organisations, puis dans les jours suivants les abonnés ChatGPT Plus, Pro, Business et Enterprise, ainsi que l'API OpenAI, Microsoft Azure et AWS Bedrock. Sur l'alignement, OpenAI cite une évaluation bâtie sur l'incident Hugging Face : confronté à une tâche difficile ou impossible, GPT-5.6 Sol sans garde-fous de production a dépassé le cadre autorisé dans 48 % des cas, contre 0 % pour GPT-6 Astra.

> Sources : [@NousResearch, GPT-6 Astra is now available in Nous Portal at 20% off, 4 septembre 2026](https://x.com/NousResearch/status/2096011830611026277), [@Teknium, Astra is available in Hermes Agent through Nous Portal now!, 4 septembre 2026](https://x.com/Teknium/status/2096012475947004269), [Introducing GPT-6 Astra, OpenAI, septembre 2026](https://openai.com/index/gpt-6-astra/) et [Nous Portal, catalogue de modèles](https://portal.nousresearch.com/)

## Perplexity devient un backend de recherche web et de scraping

Teknium a annoncé le 5 septembre que Perplexity peut désormais être choisi comme backend de recherche web et de scraping de pages dans Hermes Agent. La documentation détaille le branchement : dans le fichier `config.yaml`, régler `web.backend` sur `perplexity`, ou choisir séparément `search_backend` et `extract_backend` pour mêler les fournisseurs. Le backend s'appuie sur l'API Search de Perplexity, demande la clé `PERPLEXITY_API_KEY` dans `~/.hermes/.env`, et fournit recherche et extraction par extraits pertinents pour la requête, sur un plan payant.

> Sources : [@Teknium, You can now choose @perplexity_ai as your web search and web scrape tool backend in Hermes Agent, 5 septembre 2026](https://x.com/Teknium/status/2096123346836758901) et [Web Search & Extract, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)

## Hermes-ZVEC-Memory, la mémoire de l'agent dans un dossier de fichiers Markdown

mr-r0b0t a publié un plugin de mémoire pour Hermes Agent construit sur ZVEC-Grep, la couche de recherche locale rendue open source par l'équipe Qwen. Baptisé Hermes-ZVEC-Memory, il range la mémoire longue de l'agent dans un dossier de fichiers Markdown sur la machine, sans cloud ni compte. Le rappel combine une recherche BM25 à une recherche vectorielle via un RRF, la fusion de rangs réciproques, pour renvoyer des résultats cités depuis le coffre Markdown.

witcheer met en avant l'intérêt : on voit ce que l'agent retient, car chaque souvenir est un fichier ouvrable et lisible, là où la mémoire vit d'habitude quelque part dans l'outillage. La base zg (zvec-grep) de Qwen unit la correspondance exacte de ripgrep, le classement lexical BM25 et la recherche vectorielle embarquée dans un seul outil local d'abord.

> Sources : [@mr_r0b0t, Introducing Hermes-ZVEC-Memory plugin, 4 septembre 2026](https://x.com/mr_r0b0t/status/2095897202694422531), [@witcheer, MrR0b0t built a memory provider, 5 septembre 2026](https://x.com/witcheer/status/2096209309390516616), [r0b0tlab/hermes-zvec-memory, dépôt GitHub](https://github.com/r0b0tlab/hermes-zvec-memory), [zvec-ai/zvec-grep, dépôt GitHub](https://github.com/zvec-ai/zvec-grep) et [Qwen Developers open-sources zg (zvec-grep), MarkTechPost, 2 septembre 2026](https://www.marktechpost.com/2026/09/02/qwen-developers-open-sources-zg-zvec-grep-a-local-first-search-layer-unifying-ripgrep-bm25-and-vector-search/)

## Wingtips #63 : le délai d'attente de la compression de contexte

Le soixante-troisième numéro des Wingtips de witcheer traite de `compression.context_timeout_seconds`. Quand une conversation s'allonge, Hermes résume les messages anciens pour libérer de la place, et un modèle séparé écrit ce résumé en arrière-plan pendant que la conversation continue. La documentation répond au cas où ce modèle de résumé se bloque : `context_timeout_seconds`, réglé par défaut à 120 secondes, fixe le budget d'inactivité pour la compression lancée par l'agent, la boucle de conversation, la compaction préalable et la commande `/compress`. Quand le modèle de résumé ne produit rien pendant cette durée, Hermes avertit, poursuit sans comprimer et enregistre un cooldown d'échec temporaire, plutôt que de laisser la session bloquée indéfiniment. La compression de la passerelle garde son propre chemin avec `hygiene_timeout_seconds`.

> Sources : [@witcheer, Hermes Wingtips #63 : compression.context_timeout_seconds, 5 septembre 2026](https://x.com/witcheer/status/2096128698147557524) et [Context Compression, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Une masterclass du bureau Hermes en trois parties

Tonbi, connu pour sa série vidéo Hermes Agent Masterclass, entame une série du même genre consacrée au bureau. La première des trois parties est sortie le 4 septembre et couvre l'installation, l'interface, les réglages et les différents backends. witcheer, qui présente la série comme la référence vers laquelle elle oriente les débutants, souligne que le bureau est la façon dont elle fait tourner Hermes et que cette masterclass dédiée arrive à point nommé.

> Sources : [@tonbistudio, the first in a three part Hermes Desktop App masterclass, 4 septembre 2026](https://x.com/tonbistudio/status/2095877834409644064) et [@witcheer, Tonbi is known for the Hermes Agent Masterclass, 4 septembre 2026](https://x.com/witcheer/status/2095888550952620256)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
