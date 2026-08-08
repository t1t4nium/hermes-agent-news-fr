# Hermes Agent Quotidien #12

Parler à l'agent pendant qu'il raisonne, la skill Polymarket rendue optionnelle, le sélecteur de modèles qui retrouve ses catalogues live, un plugin de thème pour Hermes Desktop et un jalon de 1,5 trillion de tokens sur OpenRouter.

## Parler à l'agent quand il réfléchit

Le 7 août, Brooklyn! (@imbabybrooklyn) a présenté une nouvelle manière d'interagir avec l'agent :

> "Talk to your agent as it thinks to correct its thoughts mid-stream."

L'idée est de pouvoir corriger l'agent au cours de son raisonnement, pendant qu'il génère, au lieu d'attendre la réponse complète. Teknium a relayé l'annonce.

> Source : [@imbabybrooklyn, 7 août 2026](https://x.com/imbabybrooklyn/status/2085536836428935502)

## La skill Polymarket devient optionnelle

Teknium a annoncé le 6 août que la skill Polymarket a quitté l'installation par défaut pour rejoindre les skills optionnelles. La décision fait suite aux soupçons de paris truqués impliquant des influenceurs et à la demande répétée des utilisateurs de la retirer. Le changement est porté par la PR n°80515.

> "Sometimes cleaning up is as good as new features!" commente Teknium.

> Source : [@Teknium, 6 août 2026](https://x.com/Teknium/status/2085434455074951473)

## Le sélecteur de modèles retrouve les catalogues live

Witcheer (@witcheer) a corrigé le 6 août un défaut du sélecteur de modèles quand Hermes Agent tourne contre Ollama ou llama.cpp. Après avoir tiré un nouveau modèle, seul le modèle par défaut enregistré apparaissait dans la liste. La cause : le sélecteur confondait les réglages enregistrés par modèle avec une liste de modèles à afficher, et ne demandait jamais au serveur ce qu'il proposait d'autre.

Les catalogues live sont de retour dans les sélecteurs du Desktop et de la commande `/model` de Telegram, et la correction est fusionnée pour la prochaine release. Witcheer précise que la correction est partie d'une PR communautaire de @HexLab98, dont la paternité est conservée.

> Sources : [@witcheer, 6 août 2026](https://x.com/witcheer/status/2085399102645588298) - [@witcheer, PR communautaire de @HexLab98](https://x.com/witcheer/status/2085399105094697414)

## Theme Lab : un plugin de thème conçu par Hermes lui-même

@twodogseeds a publié le 7 août Theme Lab, un plugin de thème couleur pour l'application Hermes Desktop. On y dépose une image, les couleurs en sont extraites, on peut réordonner les teintes et chaque nuancier dispose d'une roue chromatique pour une personnalisation complète.

La particularité tient à la façon dont il a été construit : l'auteur a demandé à son agent Hermes de lire et d'apprendre le SDK de Hermes Desktop, puis de décrire le plugin. Quelques itérations et validations plus tard, le plugin est disponible sur github.com/0-CYBERDYNE-SYSTEMS-0/theme-lab. Teknium a relayé la démonstration.

> Source : [@twodogseeds relayé par @Teknium, 7 août 2026](https://x.com/twodogseeds/status/2085601860761825449)

## Piloter son téléphone : d'ADB à un MCP avec plugin Hermes

@sudoPhoeniX raconte le 7 août l'évolution de son contrôle de téléphone portable via Hermes Agent. Il a commencé par piloter l'appareil par câble avec adb, puis est passé à un MCP qui le contrôle, complété par un plugin Hermes qui diffuse l'état de l'écran en direct à côté de l'agent.

> "We're getting close to needing nothing but Hermes on your desktop to control and automate almost anything."

Teknium a relayé le post.

> Source : [@sudoPhoeniX relayé par @Teknium, 7 août 2026](https://x.com/sudoPhoeniX/status/2085551167535559057)

## 1,5 trillion de tokens traités sur OpenRouter

Noctus (@noctus91) a relevé le 6 août que Hermes Agent traite 1,5 trillion de tokens sur OpenRouter, soit presque autant que les 49 autres applications suivies réunies. Teknium a répondu en remerciant l'ensemble des contributeurs et des utilisateurs d'Hermes Agent.

> Source : [@noctus91 relayé par @Teknium, 6 août 2026](https://x.com/Teknium/status/2085507282121720275)

## Sources

- [@imbabybrooklyn - Parler à l'agent pendant qu'il réfléchit, 7 août 2026](https://x.com/imbabybrooklyn/status/2085536836428935502)
- [@Teknium - Skill Polymarket optionnelle, 6 août 2026](https://x.com/Teknium/status/2085434455074951473)
- [@witcheer - Sélecteur de modèles corrigé, 6 août 2026](https://x.com/witcheer/status/2085399102645588298)
- [@witcheer - PR communautaire de @HexLab98, 6 août 2026](https://x.com/witcheer/status/2085399105094697414)
- [@twodogseeds relayé par @Teknium - Theme Lab, 7 août 2026](https://x.com/twodogseeds/status/2085601860761825449)
- [@sudoPhoeniX relayé par @Teknium - Contrôle du téléphone, 7 août 2026](https://x.com/sudoPhoeniX/status/2085551167535559057)
- [@noctus91 relayé par @Teknium - 1,5T tokens sur OpenRouter, 6 août 2026](https://x.com/Teknium/status/2085507282121720275)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)