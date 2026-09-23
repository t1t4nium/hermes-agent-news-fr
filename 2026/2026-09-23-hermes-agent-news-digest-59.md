# Hermes Agent Quotidien #59

Cette édition revient sur l'arrivée d'un mode Simple dans l'application de bureau Hermes, sur la disponibilité de Claude Opus 5.5 et des modèles GPT-6 Sol et Luna dans Hermes Agent, sur l'enrichissement de la page des cas d'usage, qui passe à 326 récits, et sur l'adaptation de l'application Hermes Bots aux écrans pliables. Aucune release publiée depuis la v0.21.4 du 21 septembre.

## Le bureau Hermes gagne un mode Simple

imbabybrooklyn a présenté le 22 septembre un mode Simple dans Hermes Desktop, une interface plus propre sans l'instrumentation de développement, avec la possibilité de revenir à tout moment au mode avancé, l'espace de travail se retrouvant exactement comme on l'a laissé. witcheer a expliqué la genèse de la fonction : le mois dernier, il a demandé ce qui rendrait Hermes plus simple, et l'une des demandes les plus claires était un bureau destiné à celles et ceux qui ne sont pas développeurs. Le mode Simple se limite au chat, aux sessions, aux capacités et à la messagerie, sans rien d'autre à l'écran. tonbistudio a publié une vidéo qui montre le passage d'une vue à l'autre.

La documentation du bureau détaille ce que le mode Simple met de côté. Il est centré sur le chat : la barre d'état, le rail de profils, le terminal, l'explorateur de fichiers, les panneaux de relecture, la vue technique des appels d'outils, les diffs de code en ligne et les lignes des artefacts et des tâches planifiées s'écartent ; les capacités et la messagerie restent, car c'est par elles que l'on configure Hermes. La réflexion démarre repliée, les lignes de session montrent le titre, un aperçu et la dernière activité, et la barre de titre conserve les réglages et l'éditeur de disposition. Le sélecteur de disposition du mode Simple propose une barre latérale à gauche ou à droite, tandis que les modèles et les dispositions enregistrées relèvent du mode avancé. Le mode Simple démarre avec la barre latérale à gauche.

> Sources : [@imbabybrooklyn, Introducing Simple mode in Hermes Desktop, 22 septembre 2026](https://x.com/imbabybrooklyn/status/2102491612186034651), [@witcheer, one of the clearest asks was a Desktop for people who are not developers, 22 septembre 2026](https://x.com/witcheer/status/2102497326266798429), [@tonbistudio, Hermes Desktop App now has a Simple Mode, 22 septembre 2026](https://x.com/tonbistudio/status/2102527893071143411) et [Hermes Desktop, Interface mode, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#interface-mode)

## Claude Opus 5.5 arrive dans Hermes Agent via Nous Portal

Teknium a annoncé le 22 septembre que Claude Opus 5.5 d'Anthropic est désormais disponible dans Hermes Agent via le portail Nous. Le même jour, witcheer a appelé à faire remonter les retours sur le comportement d'Opus 5.5 dans Hermes Agent.

tonbistudio a livré ses premières impressions le 23 septembre, après avoir passé la journée sur ses tests habituels et sur un projet à large base de code. Il le juge vraiment bon, plus agréable à utiliser que GPT-6 Astra, et note que c'est la première fois qu'un modèle moins cher revendique l'aptitude de Fable et la tient réellement, avec un ressenti proche de Claude 4.5.

> Sources : [@Teknium, Anthropic's Claude Opus 5.5 is now available in Hermes Agent via Nous Portal, 22 septembre 2026](https://x.com/Teknium/status/2102442142040014893), [@witcheer, give us your feedback on how Opus 5.5 behaves in Hermes Agent, 22 septembre 2026](https://x.com/witcheer/status/2102443613062152648) et [@tonbistudio, First impressions of Opus 5.5, 23 septembre 2026](https://x.com/tonbistudio/status/2102577336738824391)

## GPT-6 Sol et Luna disponibles dans Hermes Agent

Teknium a annoncé le 22 septembre que les nouveaux GPT-6-Sol et GPT-6-Luna sont disponibles dans Hermes Agent via le portail Nous et OpenRouter, et bientôt aussi via les abonnements Codex.

OpenAI a présenté ces deux modèles le même jour comme une extension de l'univers GPT-6. Sol et Luna s'appuient sur les avancées qui sous-tendent GPT-6 Astra, en reportant une grande partie de ses points forts dans des modèles plus rapides et plus abordables, pensés pour le travail à grande échelle. La mise en cache et l'inférence ont aussi été rendues plus efficaces.

> Sources : [@Teknium, The new GPT-6-Sol and GPT-6-Luna are now available in Hermes Agent, 22 septembre 2026](https://x.com/Teknium/status/2102472696525377909) et [@OpenAI, Please welcome GPT-6 Sol and GPT-6 Luna to the GPT-6 universe, 22 septembre 2026](https://x.com/OpenAI/status/2102460975790137662)

## La page des cas d'usage passe à 326 récits

witcheer a annoncé le 23 septembre que 64 nouveaux cas d'usage de Hermes Agent ont été ajoutés le mois dernier à la page de documentation, 45 venant de Reddit et 19 de X. La page en affiche désormais 326, chacun lié au billet d'origine.

La page des cas d'usage confirme la structure. Elle recense 326 récits répartis en 15 catégories et provenant de 11 sources. Les flux de développement dominent avec 77 entrées, devant les assistants personnels (49) et les intégrations (32). X, Reddit, Discord, GitHub, les blogs et YouTube figurent parmi les sources les plus représentées. Chaque vignette pointe vers un billet, une issue, une vidéo ou un gist où quelqu'un décrit son usage de Hermes, collectés sur X, GitHub, Reddit, Hacker News, YouTube, les blogs et les podcasts.

> Sources : [@witcheer, we added 64 new Hermes Agent use cases to the docs page last month, 23 septembre 2026](https://x.com/witcheer/status/2102741867678871994) et [User Stories & Use Cases, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-stories)

## Hermes Bots pour iPhone Duo

iamlukethedev a montré le 23 septembre une déclinaison de Hermes Bots pour iPhone Duo. Plutôt que d'étirer l'application iPhone sur un écran plus grand, il a cherché à exploiter la pliure : une fois l'appareil ouvert, Hermes s'anime des deux côtés de l'écran avec une scène d'agent, l'Agent Stage, qui affiche l'animal de compagnie du bot, son activité en cours, le temps écoulé, le plan en direct et les sous-agents.

> Source : [@iamlukethedev, Hermes Bots for iPhone Duo, 23 septembre 2026](https://x.com/iamlukethedev/status/2102727731909943540)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
