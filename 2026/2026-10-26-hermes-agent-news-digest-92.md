# Hermes Agent Quotidien #92

Cette édition revient sur les 117 pull requests fusionnées le 25 octobre, sur hermes record qui transforme une démonstration de navigateur en skill, sur la skill Unbroker qui retire les infos personnelles des courtiers de données, sur HermesOBD le tableau de bord OBD-II bâti pour une Mustang, sur le plugin agent-run-debugger, sur les mentions X à venir dans Herald et sur le conseil Wingtips consacré aux skills nommées.

## 117 pull requests fusionnées le 25 octobre

iamlukethedev a fait le compte le 26 octobre : Hermes a fusionné 117 pull requests le 25 octobre. Les changements à retenir :

- L'agent peut désormais choisir et chercher lui-même les voix ElevenLabs quand il parle, par leur identifiant de voix.
- Les conversations de groupe de Desktop gagnent le renommage, la dissolution, les mentions et le collage de pièces jointes.
- La passerelle sert maintenant l'espace de travail de Desktop à l'application web.

Le changelog du 25 octobre relève aussi l'arrivée du plugin RentAHuman et de son MCP au catalogue, qui permet de créer des primes, d'envoyer des messages et de gérer des paiements ; la réépinglage de diff-review en 1.1.0, qui corrige une injection d'options git ; et la fiche catalogue de hermes-resetwatch, qui nomme désormais chaque identifiant qu'elle lit, en lecture seule.

> Sources : [@iamlukethedev, Hermes merged 117 PRs on October 25, 26 octobre 2026](https://x.com/iamlukethedev/status/2114551938755010612) et [Hermes Bible, changelog du 25 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-25)

## hermes record, montrer un parcours au lieu de le décrire

witcheer a présenté le 25 octobre hermes record, un plugin Hermes Labs construit par Nous Research. Au lieu de décrire une tâche de navigateur, on l'exécute une fois : le plugin s'attache au navigateur Chromium (Chrome, Chromium, Brave, Edge) par le protocole DevTools, observe ce qui se passe dans l'onglet actif et enregistre la démonstration dans un fichier JSON. La skill embarquée apprend ensuite à /learn à transformer cet enregistrement en skill qui rejoue le parcours avec les outils navigateur de Hermes. Dans sa vidéo, witcheer enregistre sa commande de pizza puis la fait rejouer.

Le catalogue précise l'installation : `hermes plugins install workflow-record`. Le plugin ajoute une commande CLI, `hermes record`, et une skill. Aucun outil de modèle, aucun hook, rien ne s'exécute pendant les conversations, et la seule dépendance est websockets, déjà livrée avec Hermes. L'origine remonte à la pull request hermes-agent #72199, sortie du coeur vers ce plugin.

> Sources : [@witcheer, hermes record, a Hermes Labs plugin, 25 octobre 2026](https://x.com/witcheer/status/2114405376959635912) et [workflow-record, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/workflow-record)

## Unbroker, retirer ses infos des courtiers de données

Nous Research a mis en avant le 26 octobre la skill Unbroker, installable en une ligne avec `hermes skills install official/security/unbroker`. Elle cherche où les informations personnelles d'une personne (nom, adresses, téléphone, courriel, proches) sont exposées sur les courtiers de données et les sites de recherche de personnes, puis les retire automatiquement quand c'est possible, avec des étapes guidées seulement quand un site exige un CAPTCHA, une pièce d'identité, un appel ou un fax.

La documentation en précise les garde-fous : pas de contournement d'anti-bot, aucune action sans consentement enregistré, pas de suppression des archives publiques ni des comptes que la personne contrôle. Le moteur est un CLI Python sans dépendance. Pour les personnes de Californie, une seule requête DROP efface les données chez tous les courtiers enregistrés, environ 545. Pour les autres, la couverture passe par des courriels ciblés CCPA et GDPR.

> Sources : [@NousResearch, Great time to use the Unbroker skill!, 26 octobre 2026](https://x.com/NousResearch/status/2114530795868373035), [@witcheer, hermes skills install official/security/unbroker, 26 octobre 2026](https://x.com/witcheer/status/2114607210877821024) et [Unbroker, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-unbroker)

## HermesOBD, regarder une Mustang en direct

witcheer a raconté le 26 octobre l'histoire d'un utilisateur de Hermes Agent qui a pris en charge la Mustang 2005 d'un voisin et a demandé à son agent de lui construire une application Mac pour suivre la voiture en direct. HermesOBD est le résultat, un build communautaire open source signé trafalger1801 : un tableau de bord OBD-II en direct pour macOS qui dialogue avec un adaptateur Bluetooth de voiture.

> Source : [@witcheer, HermesOBD is the result, a new open-source community build, 26 octobre 2026](https://x.com/witcheer/status/2114680949472379256)

## agent-run-debugger, retrouver l'étape qui a cassé

witcheer a présenté le 26 octobre agent-run-debugger, un plugin communautaire pour Hermes Agent. Quand une longue tâche s'arrête à mi-chemin, il montre l'étape qui a échoué, avec son erreur. Dans son test, il a lu la session et pointé un script de rapport qui s'arrêtait sur une mauvaise ligne d'un CSV, tout en classant les explications possibles.

Le catalogue en précise le fonctionnement : un debugger local, hors ligne, pour les runs échoués, bloqués ou coûteux. On importe une trace choisie, au format JSONL de Hermes, de Claude Code ou au format neutre v1, et l'on obtient une chronologie déterministe, les points d'échec observés, des hypothèses classées avec leurs preuves, les lacunes restantes et un rejeu inerte du run enregistré. Installation : `hermes plugins install agent-run-debugger`, signé Sahil-SS9.

> Sources : [@witcheer, agent-run-debugger shows you the step that broke, 26 octobre 2026](https://x.com/witcheer/status/2114699817217896910) et [agent-run-debugger, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/agent-run-debugger)

## Herald, bientôt les mentions X

iamlukethedev a annoncé le 26 octobre l'arrivée prochaine des mentions X dans Herald. On voit un post qui mérite une action, on répond avec @HeraldHermes suivi de ce que l'on veut faire. Herald envoie une notification sur le téléphone, le téléphone transmet à son propre Hermes, et Hermes exécute la tâche. Le lien est en lecture seule : Herald ne publie jamais depuis le compte.

> Source : [@iamlukethedev, Coming soon to Herald: X mentions, 26 octobre 2026](https://x.com/iamlukethedev/status/2114524194017079781)

## Wingtips #111, nommer la skill puis l'appeler

witcheer a publié le 26 octobre le conseil Wingtips #111. Quand une tâche que l'on refera se termine, on demande à l'agent de garder les étapes en skill : `save what we did as a skill called weekly-update`. Il écrit les étapes de la conversation et les enregistre sous le nom choisi.

> Source : [@witcheer, Hermes Wingtips #111: name the skill, then call it, 26 octobre 2026](https://x.com/witcheer/status/2114650743500382473)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
