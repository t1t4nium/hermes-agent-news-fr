# Hermes Agent Quotidien #97

Cette édition revient sur les 22 pull requests fusionnées le 30 octobre, sur inspeximus, un fournisseur de mémoire qui corrige un souvenir et peut défaire la correction, sur la Nous Girl qui arrive dans le terminal, et sur un article de recherche qui plaide pour l'oubli dans les agents de découverte.

## 22 pull requests fusionnées le 30 octobre

iamlukethedev a fait le compte le 31 octobre : Hermes a fusionné 22 pull requests le 30 octobre. Il en retient deux. Un job cron peut désormais être arrêté en cours d'exécution depuis Desktop (stop, annulation ou suppression), et chaque job choisit sa politique de traitement des exécutions manquées. Desktop et la Webapp font aussi clignoter l'onglet ou la barre des tâches et envoient de vraies notifications quand Hermes a besoin d'attention.

Le changelog du 30 octobre précise et complète :

- Le probe idle orphelin de la passerelle est résolu avant l'ouverture d'une lecture, pour que la passerelle démarre sans se bloquer (#144845).
- Un agent Cloud ne se bloque plus au premier démarrage sur sa lecture de configuration à distance (#146130).
- Un serveur de modèle local en panne n'envoie plus la Webapp vers la connexion fournisseur : Hermes l'annonce clairement et laisse changer de modèle ou réessayer (#146883).
- Une clarification à plusieurs questions tient en un seul formulaire sur Desktop et la Webapp (#146881).
- Les raccourcis Ctrl fonctionnent dans une fenêtre d'application Chrome comme sur Desktop (#146879).
- L'installation de Desktop propose toujours Nous Portal sur l'écran de clé API, même si d'autres services échouent (#146880).
- Les images de la Webapp restent dans le cache du navigateur, et les vidéos SSH de plus de 100 MiB se lisent (#146860).
- Dans les groupes, un membre mentionné qui ne répond pas est signalé avec la raison, au lieu d'un silence (#146289).
- Desktop ne coupe plus les connexions de passerelle saines au retour de focus, de veille ou après un blocage du renderer (#146843).
- hermes plugins doctor ne copie plus un plugin dans son propre dossier temporaire, ni un dossier qui contient seulement un plugin (#146836, #146761).
- La carte d'erreur de Desktop passe en v2, avec gravité, une seule action et un bloc de détails à copier ; Continue conserve le brouillon en cours (#146776, #146828).
- Un changement de modèle ou une annulation Discord n'est plus écrasé comme expiré (#146752).

> Sources : [Hermes Bible, changelog du 30 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-30) et [@iamlukethedev, Hermes merged 22 PRs on October 30, 31 octobre 2026](https://x.com/iamlukethedev/status/2116325057006113245)

## inspeximus, une mémoire que l'on corrige puis restaure

witcheer a présenté le 30 octobre inspeximus, un fournisseur de mémoire communautaire de DanceNitra. Si l'on a dit une chose fausse à son agent, on corrige ce qu'il retient, et l'on peut défaire la correction si l'on change d'avis.

Le catalogue précise le fonctionnement. Une correction retire l'ancienne valeur par clé, qui cesse de revenir comme contexte ; revert(key) la restaure ensuite depuis la seule clé, sans retaper ce que le registre disait. Le plugin ajoute cinq outils : inspeximus_remember pour stocker un fait sous une clé stable, inspeximus_correct pour le remplacer, inspeximus_revert pour remettre l'ancienne valeur, inspeximus_forget pour effacer un sujet en laissant un reçu, et inspeximus_forget_me pour effacer ce que la personne qui parle a écrit dans une session partagée.

Avant chaque tour, Hermes appelle prefetch(query) ; le fournisseur répond avec la récupération moins ce qu'une correction ultérieure a retiré, si bien qu'une valeur corrigée trois sessions plus tôt ne peut pas revenir comme contexte. Le fournisseur ne fait aucun appel réseau et n'embarque aucune télémétrie : le stockage est un fichier local. Le rappel sémantique est optionnel et désactivé sans embedder configuré ; activé, inspeximus envoie le texte à stocker ou à interroger vers l'URL d'embedding définie par l'opérateur, un Ollama en boucle locale par défaut. Sans embedder, le rappel est lexical et rien ne quitte la machine. L'installation passe par hermes plugins install inspeximus, puis hermes memory setup et memory.provider: inspeximus dans config.yaml.

> Sources : [@witcheer, told your Hermes Agent the wrong thing? correct what it remembers, 30 octobre 2026](https://x.com/witcheer/status/2116247263257186350) et [inspeximus, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/inspeximus)

## La Nous Girl dans le terminal

witcheer a annoncé le 30 octobre que l'on peut mettre la Nous Girl dans son terminal Hermes Agent. Elle est dessinée en braille dans le bandeau de démarrage, dans une palette monochrome chaude. Un constructeur de la communauté l'a faite pour NousCon : c'est un plugin avec deux peaux, sombre et claire.

iamlukethedev a relayé le lendemain que le terminal Hermes Agent a pris un look NousCon, et souligne que c'est sa partie préférée de Hermes : les gens construisent aussi les choses amusantes.

> Sources : [@witcheer, you can put the Nous Girl in your Hermes Agent terminal, 30 octobre 2026](https://x.com/witcheer/status/2116229395950055673) et [@iamlukethedev, Hermes Agent's terminal just got a NousCon look, 31 octobre 2026](https://x.com/iamlukethedev/status/2116417743125930037)

## Pour découvrir davantage, il faut oublier

iamlukethedev a relayé le 31 octobre un article de UC Berkeley et de Stanford, « Scaling Discovery Requires Forgetting ». Les agents menant de longues boucles de recherche et d'optimisation finissent par toucher un mur : l'historique s'accumule, ils s'ancrent à leurs anciennes tentatives et leurs modifications deviennent plus petites.

L'article, déposé sur arXiv le 14 octobre 2026 (arXiv:2610.20563), est signé par Shangyin Tan, Ben Zhou, Lakshya A Agrawal et d'autres, de UC Berkeley, Stanford et Bespoke Labs. Il compare trois façons de dépenser le même budget : un seul agent qui itère longtemps, plusieurs agents en parallèle, et une équipe qui communique. Les trois finissent par plafonner à mesure que l'historique s'accumule. La réponse tient dans l'oubli : jeter périodiquement l'état de la recherche, dont la session de chaque agent et l'historique des candidats, et repartir du meilleur candidat trouvé. Sur quatre tâches de programmation heuristique, d'optimisation de noyau et d'entraînement de modèle, l'oubli apporte jusqu'à 15 % face aux agents parallèles et jusqu'à 39 % face à un agent seul. La conclusion : pour la découverte ouverte, ce qu'un agent a le droit de retenir compte autant que le calcul qu'on lui donne.

> Sources : [@iamlukethedev, Your agent's memory might be what's holding it back, 31 octobre 2026](https://x.com/iamlukethedev/status/2116459368942371276) et [Scaling Discovery Requires Forgetting, arXiv:2610.20563, 14 octobre 2026](https://arxiv.org/abs/2610.20563)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
