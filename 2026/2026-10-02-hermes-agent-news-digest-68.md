# Hermes Agent Quotidien #68

Cette édition revient sur l'accélération de `hermes update`, sur les 182 pull requests fusionnées le 1er octobre, sur la commande `/branch` présentée dans les Wingtips, et sur la rencontre Hermes à Stockholm le 15 octobre.

## `hermes update` devient environ quatre fois plus rapide

Teknium, de retour de congé, a annoncé le 1er octobre que `hermes update` devrait être environ quatre fois plus rapide pour tout le monde. witcheer a détaillé les chiffres le lendemain : l'étape de build de Desktop prend environ 22 secondes sous Linux, les interfaces TUI et web sont sautées quand rien n'a changé, et sous Windows la vérification de syntaxe s'exécute en environ une seconde.

> Sources : [@Teknium, I'm back from vacation and Hermes update should be around 4x faster for everyone, 1er octobre 2026](https://x.com/Teknium/status/2105809042291798441) et [@witcheer, what a great time to run hermes update, 2 octobre 2026](https://x.com/witcheer/status/2105894981911413165)

## 182 pull requests fusionnées le 1er octobre

iamlukethedev a fait le compte le 2 octobre : Hermes a fusionné 182 pull requests le 1er octobre, pour démarrer le mois fort. Trois entrées figurent dans le texte du message, le reste de la liste étant détaillé dans la capture jointe :

- Les intégrations YouTube sont de nouveau lisibles dans l'application Desktop empaquetée, via un hôte de lecture en boucle locale.
- Les intégrations X et Instagram n'exécutent plus les scripts vendeurs dans la fenêtre de l'application.
- Desktop conserve sa passerelle distante.

> Source : [@iamlukethedev, Hermes started October strong, 182 PRs merged today, 2 octobre 2026](https://x.com/iamlukethedev/status/2105849499356950850)

## Wingtips #89 : /branch

witcheer a consacré le quatre-vingt-neuvième numéro des Wingtips à la commande `/branch`. Elle copie la conversation en cours dans une nouvelle session, historique compris, pour poursuivre dans la copie, ce qui permet d'essayer une autre idée sans perdre le fil. La documentation des commandes précise le comportement : l'alias `/fork` existe ; sur Discord, Telegram, Slack et Matrix, la branche s'ouvre dans un nouveau fil frère et le fil courant reste sur la session d'origine, tandis que `--here` bascule le fil courant sur la branche ; le CLI et les plateformes sans fils branchent toujours sur place. En CLI classique, la commande est refusée en plein tour, comme `/handoff`, il faut attendre la fin de la réponse en cours puis réessayer.

> Sources : [@witcheer, Hermes Wingtips #89: /branch, 2 octobre 2026](https://x.com/witcheer/status/2105922267636965538) et [Slash Commands Reference, /branch, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## Rencontre Hermes à Stockholm le 15 octobre

witcheer a annoncé que Nous Research soutient les événements communautaires, avec Stockholm pour prochaine étape. Le jeudi 15 octobre, Alper Aydemir organise une rencontre Hermes Agent dans les locaux de Volumental, sur Söder Mälarstrand, avec au programme présentations, échanges, snacks et bière. La page Luma de l'événement précise les modalités : de 17 h à 21 h (GMT+2), inscription soumise à l'approbation de l'hôte, adresse exacte communiquée après inscription, arrivée avant 18 h demandée pour pouvoir entrer, et un lien Google Meet pour suivre la soirée en ligne. alpervm annonce de son côté qu'une centaine de personnes sont déjà inscrites.

> Sources : [@witcheer, Nous Research supports community events and Stockholm is next, 2 octobre 2026](https://x.com/witcheer/status/2106019951895097353), [@alpervm, 100 people already signed up, 2 octobre 2026](https://x.com/alpervm/status/2106008876843769908) et [Hermes Stockholm meetup, page Luma](https://luma.com/ynmfdbnb)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
