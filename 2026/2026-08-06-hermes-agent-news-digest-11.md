# Hermes Agent Quotidien #11

Un navigateur intégré rend Hermes Desktop capable de voir et contrôler le web aux côtés de l'utilisateur, AnyDoc convertit tous les formats de documents en Markdown localement, Actual Inc. intègre Hermes nativement, et la documentation officielle reçoit une mise à jour structurelle.

## Un navigateur intégré dans Hermes Desktop, contrôlé par l'agent

Le 5 août, Brooklyn! (@imbabybrooklyn) a annoncé que Hermes Desktop dispose désormais d'un navigateur intégré que l'agent peut contrôler et dans lequel il peut voir le contenu :

> "Hermes Desktop now has an in-app browser that hermes can control and is aware of."

Tonbi (@tonbistudio) a publié le 6 août une vidéo de démonstration et détaillait les possibilités :

> "This new Hermes Desktop browser isn't just an extra window with a browser bolted on, the agent can operate, see, and analyze what it sees along with you."

Parmi les usages cités : faire défiler son fil X puis demander un résumé des sujets chauds, regarder un tutoriel YouTube et demander à l'agent d'en extraire le transcript ou d'implémenter les concepts, ou encore ouvrir des liens de recherche dans le navigateur et les analyser ensemble.

Teknium a relayé les deux annonces. Brooklyn! a confirmé que le navigateur conserve l'état de connexion (persistent login state). Plusieurs utilisateurs ont noté que la fonctionnalité est pour l'instant limitée à l'application desktop locale et ne fonctionne pas encore via une passerelle distante.

> Sources : [@imbabybrooklyn, 5 août 2026](https://x.com/imbabybrooklyn/status/2085019745221554678) - [@tonbistudio, 6 août 2026](https://x.com/tonbistudio/status/2085153882708078596)

## AnyDoc : Hermes Agent lit tous les formats de documents

Le 6 août, Teknium a annoncé que Hermes Agent peut désormais lire n'importe quel format de fichier : PDF, Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, tous convertis automatiquement en Markdown propre au moment où l'agent lit le fichier, entièrement en local. Zéro configuration, l'installation est automatique.

La fonction repose sur AnyDoc, une bibliothèque open-source en Rust publiée par Firecrawl (@firecrawl). Nicolas Camara (@nickscamara_) a détaillé les performances le 4 août : conversion en moins de 5 ms, 500 fichiers DOCX traités en 1,7 seconde, couverture de 13 formats.

Un utilisateur a déjà publié un plugin complémentaire, hermes-docs (@dyiapanis), qui ajoute la couche OCR que AnyDoc n'inclut pas nativement.

> Source : [@Teknium, 6 août 2026](https://x.com/Teknium/status/2085156837561893117) - [@nickscamara_, 4 août 2026](https://x.com/nickscamara_/status/2084669934194266370)

## Actual Inc. s'intègre nativement à Hermes Agent

Le 6 août, Actual Inc. (@actualinc) a annoncé que sa plateforme d'inférence personnelle fonctionne désormais nativement avec Hermes Agent :

> "The world's best harness, Hermes Agent by @NousResearch now works with Actual out of the box. Hermes is the most effective harness for every model and thats why we're thrilled to use it natively. Hermes agent users can now use their personal inference capacity from anywhere."

Teknium a relayé l'annonce. Actual Inc. propose de l'inférence depuis n'importe quel appareil, et cette intégration permet aux utilisateurs d'Hermes de brancher leur propre capacité de calcul personnelle sans configuration supplémentaire.

> Source : [@actualinc relayé par @Teknium, 6 août 2026](https://x.com/actualinc/status/2085172429895172136)

## Documentation Hermes Agent retravaillée

Le 5 août, Witcheer (@witcheer) a annoncé une mise à jour importante de la documentation officielle d'Hermes Agent, alimentée par les retours des utilisateurs sur X, Reddit, GitHub et Discord des derniers mois.

Les nouveautés au programme de la doc :

- Un guide pour exécuter Hermes de manière sécurisée sur une machine personnelle ou professionnelle.
- Une checklist de dépannage pour quand l'agent semble moins performant que d'habitude.
- Une explication du temps de première réponse sur les modèles locaux (et ce qui l'améliorera).
- Une page de correspondance des fichiers : quel fichier fait quoi (SOUL.md, USER.md, MEMORY.md, AGENTS.md).
- Un tableau de facturation par plan pour les fournisseurs par abonnement.
- Un avertissement sur le fait de pointer deux agents vers le même dossier Hermes home.

Witcheer rappelle que Hermes Agent embarque une skill de lecture de sa propre documentation, ce qui permet à l'agent de chercher la réponse et d'expliquer la correction en cas de problème.

> Source : [@witcheer relayé par @Teknium, 5 août 2026](https://x.com/witcheer/status/2085040329816731713)

## Sources

- [@imbabybrooklyn - Navigateur intégré dans Hermes Desktop, 5 août 2026](https://x.com/imbabybrooklyn/status/2085019745221554678)
- [@tonbistudio - Démonstration du navigateur, 6 août 2026](https://x.com/tonbistudio/status/2085153882708078596)
- [@Teknium - AnyDoc : tous les formats de documents, 6 août 2026](https://x.com/Teknium/status/2085156837561893117)
- [@nickscamara_ - AnyDoc présentation, 4 août 2026](https://x.com/nickscamara_/status/2084669934194266370)
- [@actualinc relayé par @Teknium - Intégration Actual Inc., 6 août 2026](https://x.com/actualinc/status/2085172429895172136)
- [@witcheer relayé par @Teknium - Mise à jour documentation, 5 août 2026](https://x.com/witcheer/status/2085040329816731713)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
