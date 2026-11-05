# Hermes Agent Quotidien #102

Cette édition revient sur le lancement du Hermes Marketplace qui réunit plugins, skills et connecteurs sur une page, sur le hackathon plugins doté de 20 000 dollars, sur la remise de 80 % accordée au modèle Hy4 de Tencent dans le Nous Portal, sur la création de routines depuis l'application mobile, et sur les 24 pull requests fusionnées le 4 novembre.

## Le Hermes Marketplace réunit plugins, skills et connecteurs

Le 4 novembre, Nous Research a lancé le Hermes Marketplace, une page unique qui rassemble tout ce qui étend l'agent : les plugins, les skills et les connecteurs. La page affiche 977 plugins, avec trois familles d'entrées, officielles, certifiées et communautaires. witcheer résume le découpage : les plugins couvrent la mémoire, la voix, les modèles, les outils web et les applications Desktop ; les skills sont le savoir-faire que l'agent charge quand une tâche le demande ; les connecteurs relient Slack, Notion, Linear, Stripe et d'autres services, avec une seule connexion chacun.

iamlukethedev note que presque mille plugins, skills et connecteurs sont désormais installables par une seule commande, et il en retient deux. Le plugin Claude Subscription fait tourner Hermes sur un abonnement Claude Pro ou Max, sans clé API séparée ni facture au jeton. Memory Wiki laisse parcourir ce que l'agent retient sous forme de pages et de journaux quotidiens. tonbistudio a publié une visite vidéo du Marketplace montrant comment installer un plugin, une skill ou un connecteur.

> Sources : [@NousResearch, Plugins, connectors, and skills for Hermes Agent are now unified in a single marketplace, 4 novembre 2026](https://x.com/NousResearch/status/2118058453415371119), [@witcheer, the Hermes Marketplace is here, 4 novembre 2026](https://x.com/witcheer/status/2118063280585421004), [@iamlukethedev, Hermes now has almost 1,000 plugins, skills and connectors in one marketplace, 4 novembre 2026](https://x.com/iamlukethedev/status/2118060359227732281), [@tonbistudio, The new Hermes Marketplace collects plugins, skills, and connectors into one convenient hub, 4 novembre 2026](https://x.com/tonbistudio/status/2118088113063096816) et [Hermes Marketplace, page officielle](https://hermes-agent.nousresearch.com/marketplace)

## Un hackathon plugins doté de 20 000 dollars

Le 4 novembre, Nous Research a ouvert le Hermes Agent Plugin Hackathon. Il dure sept jours et met en jeu 20 000 dollars en espèces, plus des lots. Teknium a relayé l'annonce en invitant à pousser le système de plugins dans ses retranchements.

Les soumissions se ferment le 11 novembre à 17 h, heure de l'Est. Les prix vont de 10 000 dollars pour la première place, avec une enseigne au néon, des produits dérivés et 1 000 dollars de crédits, jusqu'à 1 000 dollars pour la cinquième, avec cinq places de finalistes à 250 dollars de crédits. Pour participer, il faut ouvrir une pull request qui ajoute son plugin au catalogue, poster une vidéo de démonstration de moins de quatre-vingt-dix secondes sur X en mentionnant @NousResearch, puis soumettre les deux liens via un formulaire. Le jury note l'utilité, la fiabilité, la finition et la créativité, et privilégie les plugins qui font plus qu'un simple prompt ou une skill. Les entrées retenues seront listées dans le Hermes Marketplace.

> Sources : [@NousResearch, The Hermes Agent Plugin Hackathon starts now, 4 novembre 2026](https://x.com/NousResearch/status/2118094256438936062) et [@Teknium, It's time for another hackathon, 4 novembre 2026](https://x.com/Teknium/status/2118099324186059220)

## Hy4 de Tencent à moins 80 % pendant une semaine

Le 4 novembre, Nous Research a annoncé que Hy4, le nouveau modèle de Tencent Hunyuan, est vendu 80 % moins cher dans le Nous Portal pendant une semaine. Le modèle ajoute l'entrée d'images et l'usage de l'ordinateur, et Tencent l'a entraîné pour le développement de jeux sous Unity, Unreal et Godot ainsi que pour l'édition de fichiers Word, Excel et PowerPoint.

witcheer complète le tableau : Hy4 apporte la vision et l'usage de l'ordinateur, vise le frontend et le développement de jeux, et aide sur la finance, les tâches de bureau, la science et la recherche, avec de solides capacités d'apprentissage en contexte. Du côté de Tencent, Hy4 se présente comme un modèle open source nouveau avec vision, productif sur la finance, le frontend, le jeu, le bureau et la recherche, construit avec la cybersécurité et la biosécurité en tête.

> Sources : [@NousResearch, Hy4, the new model from @TencentHunyuan, is 80% off in Nous Portal for one week, 4 novembre 2026](https://x.com/NousResearch/status/2118136505046904891), [@witcheer, new marvellous discount in Nous Portal: Hy4 from Tencent Hy is 80% off for a week, 5 novembre 2026](https://x.com/witcheer/status/2118227991364829593) et [@TencentHunyuan, Hy4 is here, new with vision, 4 novembre 2026](https://x.com/TencentHunyuan/status/2117870250830630539)

## Créer une routine depuis l'application mobile

Le 5 novembre, witcheer a montré que l'on peut mettre en place une routine, ou une tâche cron, directement depuis l'application mobile Hermes. Il suffit d'ouvrir le mode Live, de dire ce que l'on veut et quand, et l'agent crée la routine. Elle apparaît ensuite sous « ••• > Routines », avec le moment où elle tourne et ce qu'elle fera.

La démonstration prolonge l'application mobile dont la bêta a été lancée pendant NousCon et couverte par une édition précédente. La création de routines à la voix s'ajoute aux capacités du client mobile, qui se connecte à la passerelle Hermes tournant sur sa propre machine.

> Source : [@witcheer, you can set up a routine (or cron job) directly from the Hermes Mobile app, 5 novembre 2026](https://x.com/witcheer/status/2118350371907101134)

## 24 pull requests fusionnées le 4 novembre

Le changelog du 4 novembre recense 24 pull requests fusionnées. Parmi les changements visibles, les images s'affichent désormais en ligne dans le CLI et la TUI, au lieu d'un simple chemin de fichier, et le terminal de VS Code rend les images en pleine résolution quand son support d'images est activé. Le catalogue accueille le plugin rex, une intégration au terminal Rex. Et le chat de l'application mobile se connecte à une Webapp placée derrière un proxy distant.

Quelques correctifs complètent la journée. Le dashboard refuse les écritures de cookies que le navigateur marque comme venant d'une autre page. En mode bot, un réveil groupé sert plusieurs coéquipiers à la fois, relaie une réponse oubliée une seule fois et rend un résultat clair quand personne ne répond. L'installeur Microsoft Store est publié automatiquement une fois certifié.

> Sources : [Hermes Bible, changelog du 4 novembre 2026](https://www.hermesbible.com/changelog?date=2026-11-04) et [NousResearch/hermes-agent, pull requests fusionnées le 4 novembre 2026](https://github.com/NousResearch/hermes-agent/pulls?q=is%3Apr+merged%3A2026-11-04)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
