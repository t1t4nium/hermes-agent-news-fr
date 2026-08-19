# Hermes Agent Quotidien #24

La famille de modèles open-weight Ornith 1.5 embarque une configuration Hermes Agent dans sa fiche de modèle, Hermes gagne la capacité de faire visiter ses propres interfaces et celles des sites externes, et la documentation officielle se dote d'un glossaire qui décrypte le langage de symboles du terminal.

## Ornith 1.5 intègre Hermes Agent dans sa fiche de modèle

Le 19 août, Ornith a publié Ornith 1.5, une famille de modèles open-weight qui couvre 9B dense, 35B MoE et 397B MoE. Le point qui concerne Hermes Agent : la fiche de modèle est fournie avec une configuration de connexion prête à l'emploi pour son agent.

Comme l'a résumé witcheer, il suffit de pointer son Hermes Agent vers un serveur local Ornith 1.5, du plus petit au plus gros modèle de la gamme. Ornith décrit une famille entraînée en cycle d'auto-amélioration : le modèle propose de nouvelles tâches, génère ses propres scaffolds et produit les rollouts de renforcement, ce qui crée continuellement de nouvelles expériences d'apprentissage. Les modèles et leurs versions quantifiées sont publiés sous licence MIT. witcheer précise qu'un benchmark est prévu prochainement.

L'intégration se joue côté configuration : la fiche fournit le réglage prêt à l'emploi, et l'agent se branche sur une URL locale.

> Sources : [@witcheer, Ornith 1.5 et Hermes Agent, 19 août 2026](https://x.com/witcheer/status/2090097521934643678)

## Hermes construit des visites guidées de ses interfaces et des sites externes

Le 19 août, imbabybrooklyn a montré qu'Hermes peut générer un parcours guidé de lui-même. La démonstration montre l'agent qui construit à la demande un tour de ses propres pages, puis guide l'utilisateur étape par étape pour prendre en main l'outil.

witcheer a précisé la portée de la fonction : elle ne se limite pas à une surface propre. Il suffit d'ouvrir un site dans le panneau d'aperçu, et Hermes construit à la volée une visite de cette page. Il n'existe nulle part de contenu de visite préenregistré dans l'application. L'agent scanne l'écran, identifie les contrôles réels et les met en évidence un par un. Pour qui a du mal à suivre le rythme auquel le logiciel évolue, c'est un moyen direct de se faire expliquer par l'agent les fonctions qui viennent de changer.

## Les checkpoints de fichiers permettent de restaurer un projet supprimé

Le 19 août, witcheer a montré le retour en arrière par fichiers. Dans la démonstration, il laisse son Hermes Agent supprimer tout un projet, puis tape la commande de restauration. Le principe : Hermes prend un instantané de ses fichiers avant toute opération destructive, et une seule commande remet tout en place.

La fonction est opt-in, elle s'active via l'option de ligne de commande hermes chat --checkpoints. Elle se distingue du rollback du curateur, qui restaure les instantanés de la curation de mémoire : celui-ci opère au niveau des fichiers du projet.

## Un glossaire des symboles du terminal dans la documentation officielle

Le 18 août, witcheer a signalé l'ajout d'un glossaire dans la documentation officielle. La page de référence CLI Symbols Glossary décrypte tous les symboles de l'interface terminal, qu'il fallait jusqu'alors apprendre par osmose : une puce pour un appel d'outil, une coche ou une croix pour le résultat, des chevrons pour les sections repliées, des spinners braille pendant la réflexion, des badges pour les sous-agents, la voix et les approbations.

Une seule page de référence donne désormais à un coup d'oeil ce que fait l'agent.

> Source : [@witcheer, glossaire CLI, 18 août 2026](https://x.com/witcheer/status/2089750604776132946)

## Sources

- [@witcheer - Ornith 1.5 et Hermes Agent, 19 août 2026](https://x.com/witcheer/status/2090097521934643678)
- [@imbabybrooklyn - Hermes visite ses propres pages, 19 août 2026](https://x.com/imbabybrooklyn/status/2089993608413741338)
- [@witcheer - Visites des sites externes, 19 août 2026](https://x.com/witcheer/status/2090080139182821777)
- [@witcheer - /rollback et checkpoints de fichiers, 19 août 2026](https://x.com/witcheer/status/2090067309020815714)
- [@witcheer - Glossaire CLI, 18 août 2026](https://x.com/witcheer/status/2089750604776132946)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)