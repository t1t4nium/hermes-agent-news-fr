# Hermes Agent Quotidien #73

Cette édition revient sur le lancement de Hermes Index, un classement des modèles par score et par coût par tâche, sur le numéro 94 des Wingtips consacré aux références @file:, sur les 187 pull requests fusionnées le 6 octobre, sur Herald OS, un système d'exploitation ouvert construit autour de l'agent, et sur l'adoption de Hermes Gadget par la communauté.

## Hermes Index : le classement des modèles par score et coût

Nous Research a lancé le 6 octobre Hermes Index, un classement qui note les modèles sur ce qu'ils accomplissent dans Hermes Agent et sur ce que chaque tâche coûte. L'index combine quatre suites exécutées dans le même harnais Hermes Agent : Hermes Bench, TerminalBench 4, TerminalBench Science et SkillsBench. Hermes Bench est une nouvelle suite maison de 150 tâches réparties en 25 catégories, mêlant les skills Hermes, la recherche, les diagrammes et l'art, la mémoire, l'utilisation d'outils et la sécurité.

Teknium précise l'objectif : donner à chaque utilisateur de Hermes Agent un moyen de trouver le meilleur modèle à un moment donné, et le meilleur modèle à un prix donné. witcheer retient que les quatre suites tournent toutes dans le harnais Hermes Agent, pour mesurer ce qu'un modèle fait réellement dans l'agent plutôt qu'un score abstrait.

La page du classement, consultée le 7 octobre, publie les résultats complets. Claude Opus 5.5 mène avec un index de 63,31 pour 4,99 dollars par tâche, devant GPT 6 Astra (56,25 pour 11,61 dollars) et Claude Sonnet 5.5 (53,14 pour 2,82 dollars). Plus bas, DeepSeek V4.1 Flash atteint 36,91 pour 0,26 dollar par tâche et Ling 3.0 Flash 21,56 pour 0,054 dollar. Nous identifie six modèles sur la frontière de Pareto, ceux qu'aucun autre ne bat à la fois sur le prix et sur le score : Claude Opus 5.5, Claude Sonnet 5.5, GPT 6 Sol, DeepSeek V4.1 Flash, GPT 6 Luna et Ling 3.0 Flash.

La notation de Hermes Bench combine 64 contrôles automatiques sur les fichiers et l'état, 77 contrôles hybrides avec un juge LLM, une tâche notée uniquement par un juge et 8 tâches visuelles jugées trois fois avec conservation de la médiane. Chaque évaluation se déroule en pass@1, l'effort de raisonnement étant réglé sur élevé quand le modèle le propose. Le classement signale aussi les fuites de benchmark : certains agents ont trouvé le dépôt public de SkillsBench et réutilisé ses solutions publiées, d'où l'affichage d'un score propre à côté du score brut pour les modèles concernés.

> Sources : [@NousResearch, Introducing Hermes Index, 6 octobre 2026](https://x.com/NousResearch/status/2107592255124951360), [@Teknium, We just launched Hermes Index!, 6 octobre 2026](https://x.com/Teknium/status/2107596615477604808), [@witcheer, Hermes Index scores models on what they get done, 7 octobre 2026](https://x.com/witcheer/status/2107705107777274121), [Hermes Index, portal.nousresearch.com/bench](https://portal.nousresearch.com/bench) et [AlphaSignal, Hermes Index ranks agent models by quality and cost, 7 octobre 2026](https://alphasignal.ai/news/nous-research-s-hermes-index-ranks-ai-agents-by-score-and-real-cost)

## Wingtips #94 : attacher un fichier à son message

witcheer a consacré le numéro 94 des Wingtips aux références de contexte. Un agent peut recevoir un fichier entier comme partie du message, sans copier-coller : on tape @, on choisit file: dans le menu, puis on ajoute le nom du fichier et sa question, par exemple « @ file:meeting-notes.md turn this into a to-do list ».

La documentation des références de contexte détaille la mécanique. La syntaxe @file: injecte le contenu d'un fichier, avec une plage de lignes possible (@file:chemin:10-25) ; @folder: injecte l'arborescence d'un dossier ; @diff et @staged injectent les changements git ; @git:N les N derniers commits ; @url: extrait une page web. Dans le CLI interactif, @ déclenche la complétion, et le contenu est expansé avant l'envoi au modèle, sous une section « Attached Context ». C'est une fonctionnalité de CLI : sur les plateformes de messagerie, le @ n'est pas expansé par la passerelle, et l'agent passe par read_file, search_files ou web_extract à la place.

> Sources : [@witcheer, Hermes Wingtips #94: attach a file to your message, 7 octobre 2026](https://x.com/witcheer/status/2107731405987856566) et [Context References, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)

## 187 pull requests fusionnées le 6 octobre

iamlukethedev a fait le compte le 7 octobre : Hermes a fusionné 187 pull requests le 6 octobre. Deux changements figurent dans le texte du message :

- La saisie vocale affiche les mots en direct pendant que l'on parle, dans le CLI, le TUI et Desktop, et les longs enregistrements sont transcrits sur tous les fournisseurs STT cloud.
- Les fournisseurs TTS de plugins qui diffusent du PCM peuvent rejoindre la voix en temps réel.

> Source : [@iamlukethedev, Hermes merged 187 PRs on October 6, 7 octobre 2026](https://x.com/iamlukethedev/status/2107751205632184693)

## Herald OS : un système d'exploitation autour de l'agent

iamlukethedev a annoncé le 7 octobre la mise en open source de Herald OS, un système d'exploitation où l'agent n'est plus une application mais une partie du système. On parle ou on tape à Hermes, qui agit sur toute la machine : ouvrir des applications, chercher et organiser des fichiers, surveiller ce qui tourne, mémoriser ce qui compte, lancer des routines planifiées et construire du logiciel pendant que l'on regarde. witcheer en retient deux usages : dire « Hey Hermes » pour parler à son ordinateur, et sélectionner une partie de l'écran pour interroger dessus.

Le dépôt précise les installations possibles. Herald OS se présente comme une application macOS (Apple Silicon, macOS 13 et plus), un système Linux complet sur PC x86_64 fondé sur Fedora, un paquet Arch, ou un paquet Arch plus une commande sous Omarchy. Chaque action qui modifie quelque chose passe par un système de permissions contrôlé par l'utilisateur. Le projet est en alpha 0.1, sous licence MIT, indépendant et non affilié à Nous Research ; Hermes Agent est installé à ses côtés.

> Sources : [@iamlukethedev, I built an operating system where the AI agent isn't another app, 7 octobre 2026](https://x.com/iamlukethedev/status/2107765448343261506), [@witcheer, Luke open-sourced Herald OS, 7 octobre 2026](https://x.com/witcheer/status/2107768823168528634) et [iamlukethedev/Herald-OS, dépôt GitHub](https://github.com/iamlukethedev/Herald-OS)

## Hermes Gadget : la communauté s'en empare

adolandev a fait le point le 7 octobre sur Hermes Gadget, trois jours après l'avoir publié comme SDK ouvert et démo. La communauté s'en est emparée : des gens font tourner Hermes sur des montres LilyGO, des AIPI Lite, des gadgets de bureau et de vieux téléphones Android, et partagent leur travail. witcheer précise que 17 pull requests de la communauté ont déjà été fusionnées, et Teknium salue l'effort.

> Sources : [@adolandev, Three days ago, Hermes Gadget was an open SDK and a demo, 7 octobre 2026](https://x.com/adolandev/status/2107813150686888407), [@witcheer, Adolan's Hermes Gadget SDK came out on Saturday, 7 octobre 2026](https://x.com/witcheer/status/2107815475493167408) et [@Teknium, Love this hermes gadgets effort by the community!, 7 octobre 2026](https://x.com/Teknium/status/2107813397534543900)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
