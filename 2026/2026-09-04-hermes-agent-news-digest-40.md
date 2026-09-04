# Hermes Agent Quotidien #40

Cette édition revient sur l'installation en un clic des modèles locaux dans Hermes Desktop, mise en avant pour le matériel NVIDIA, sur le soixante-deuxième numéro des Wingtips consacré au modèle des tâches cron, et sur un projet communautaire : un cron Hermes Agent qui écrit un véritable journal chaque nuit.

## Hermes Desktop installe les modèles locaux en un clic

Nous Research a annoncé le 3 septembre que Hermes Desktop sait désormais mettre en place les modèles locaux en un clic. L'application lit le matériel de la machine, choisit le modèle le plus adapté, puis le télécharge et configure le runtime. Un autre message de Nous Research précise que cette installation convient particulièrement au matériel NVIDIA, et le compte NVIDIA RTX Spark ajoute qu'elle arrive sur les systèmes NVIDIA sous Windows et Linux.

witcheer, qui utilise beaucoup les modèles locaux, présente la nouveauté comme la chute du principal frein à leur adoption. Choisir le bon modèle demandait jusqu'ici un savoir-faire propre : ce qui tient dans la mémoire, quelle quantification, quels réglages de runtime. Hermes Desktop gère désormais tout cela d'un clic.

La documentation détaille le fonctionnement. Hermes télécharge et maintient le moteur d'inférence llama.cpp et en choisit la compilation adaptée au matériel, et il gère la mémoire : plus aucune taille de contexte, couche GPU ou quantification à régler. Chaque modèle du catalogue est évalué par rapport à la machine (tient entièrement dans le GPU, utilise la RAM système, ou trop gros), et Hermes retient la compilation de plus haute qualité qui tourne entièrement sur le GPU, sans jamais proposer de build sous 4 bits. Sous Windows et Linux, il faut un GPU NVIDIA (CUDA) ou le processeur ; sur macOS, une puce Apple Silicon ; les GPU AMD passent par Vulkan.

> Sources : [@NousResearch, Hermes Desktop now sets up local models in one click, 3 septembre 2026](https://x.com/NousResearch/status/2095602995874410664), [@NousResearch, Our new one-click local model setup is perfect for use with NVIDIA hardware, 3 septembre 2026](https://x.com/NousResearch/status/2095627661632557363), [@witcheer, this is the biggest barrier to local models falling in one update, 3 septembre 2026](https://x.com/witcheer/status/2095604129221460042), [@NVIDIARTXSpark, Local AI agents should be easy to set up, 3 septembre 2026](https://x.com/NVIDIARTXSpark/status/2095595273451884884) et [Local Models, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/local-models)

## Wingtips #62 : donner aux tâches cron un modèle dédié

Dans le soixante-deuxième numéro de sa série Wingtips, witcheer explique que les tâches cron et les sessions de chat n'ont pas à partager le même modèle. Sans réglage propre au cron, une nouvelle tâche tourne sur le modèle global par défaut, celui avec lequel on discute, même quand il s'agit d'un petit résumé quotidien. Il présente deux façons d'orienter la dépense des tâches planifiées.

La documentation précise l'ordre de résolution du modèle au moment du déclenchement : l'épinglage propre à la tâche d'abord, puis le réglage `cron.model` du fichier `config.yaml`, puis le défaut global. `cron.model` fixe un modèle par défaut pour toute la flotte cron, indépendant du modèle de chat : on le pose une fois avec `hermes config set cron.model <name>`, et changer son modèle de conversation ne touche plus aux tâches planifiées. Une tâche individuelle peut aussi épingler son propre modèle et son propre fournisseur. Quand rien de tout cela n'est défini, Hermes fige le fournisseur et le modèle au moment de la création : si le défaut global change ensuite, la tâche échoue en se fermant. Elle saute l'exécution, ne lance aucun appel d'inférence et prévient une seule fois, à moins de désactiver la garde de dérive avec `cron.model_drift_guard false`.

> Sources : [@witcheer, Hermes Wingtips #62 : cron.model, 4 septembre 2026](https://x.com/witcheer/status/2095722000907923465) et [Scheduled Tasks (Cron), documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)

## Un cron Hermes Agent qui écrit un vrai journal chaque nuit

witcheer a mis en avant le 4 septembre un projet communautaire : un cron Hermes Agent qui rédige pendant la nuit un véritable journal, avec sa une, ses rubriques et la numérotation des pages. Il souligne une première idée du dépôt, que les chiffres ne viennent jamais du modèle : la météo, les marchés et le livre de comptes du foyer sont produits par du Python.

Le dépôt, vaelkeep/hermes-paper-agent, se présente comme un journal qui s'écrit lui-même : un agent fait tourner les rubriques, les figures sortent du code, et il refuse de publier une édition contenant des fautes. Les rubriques de données (météo via Open-Meteo, finance via Yahoo, comptes, étapes) sont du code ; le rédactionnel revient à l'agent. Une vérification passe sur chaque édition et, si elle revient en rouge, l'agent corrige la ligne signalée avant qu'une seconde passe ne soit propre : le dépôt illustre le cas d'une cellule de tableau de 27 caractères pour une limite de 26, rattrapée avant publication. L'architecture s'appuie sur un fichier AGENTS.md qui fixe les ordres permanents du rédacteur en chef de nuit et sur une skill installée dans Hermes. Le projet est publié en licence MIT.

> Sources : [@witcheer, a community project worth your time: a Hermes Agent cron that writes an actual newspaper overnight, 4 septembre 2026](https://x.com/witcheer/status/2095850825813782836) et [vaelkeep/hermes-paper-agent, dépôt GitHub](https://github.com/vaelkeep/hermes-paper-agent)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
