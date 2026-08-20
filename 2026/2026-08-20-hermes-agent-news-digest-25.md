# Hermes Agent Quotidien #25

Hermes s'appuie sur l'évaluateur de skills de NVIDIA au moment de l'installation pour détecter secrets et failles, le bureau accepte des thèmes de n'importe quelle couleur via un plugin accent picker, et deux outils communautaires donnent une vue matérielle de ses agents : un poste de commande 3D et un suivi des quotas du bureau.

## NVIDIA SkillEvaluator passe les skills au crible à l'installation

Le 20 août, Nous Research a détaillé l'intégration de l'évaluateur de skills de NVIDIA dans Hermes Agent. À l'installation d'une skill, Hermes le lance pour vérifier la présence de données personnelles (PII), de secrets qui fuient, de contrebande Unicode, ainsi que les problèmes de licence et de sécurité, le tout avant la confirmation de l'utilisateur.

Nous a d'abord passé l'outil sur ses propres skills embarquées et a utilisé ses résultats pour en améliorer 11. La mécanique figurait déjà en une ligne dans les notes de v0.20.4 (édition #23) ; cette annonce précise le périmètre exact des contrôles et le travail de correction qu'elle a entraîné en interne.

> Source : [@NousResearch, SkillEvaluator sur les skills, 20 août 2026](https://x.com/NousResearch/status/2090166128509096187)

## Chaque thème du bureau peut prendre n'importe quelle couleur

Le 20 août, imbabybrooklyn a montré un rafraîchissement d'Hermes Desktop : via le plugin accent picker, n'importe quel thème peut désormais être décliné dans la couleur de son choix. Le réglage se trouve dans la section plugins de l'application.

Le tweet illustre la même logique de personnalisation que le plugin de thèmes existant : l'accent devient une variable réglable, et le choix de couleur s'ajoute aux options de surface déjà présentes (le mode verre mat couvert au #23). Teknium a accompagné la démonstration d'un simple signe d'approbation.

> Source : [@imbabybrooklyn, accent picker, 20 août 2026](https://x.com/imbabybrooklyn/status/2090352831299527009)

## Hermes3D, un poste de commande 3D pour les agents

Luke The Dev a présenté le 20 août Hermes3D, un centre de commande 3D en direct pour Hermes Agent. Le projet reprend l'idée de Claw3D, son outil initialement construit autour d'OpenClaw, et la reconstruit pour Hermes. Le principe : Bot Mode donne à chaque agent un rôle, un modèle, une mémoire, des skills, des outils et une personnalité, et Hermes3D donne à cette équipe un espace de travail visible.

On y voit quels agents travaillent, qui est bloqué, on peut inspecter leurs tâches, ouvrir le tableau Kanban, et s'approcher d'un agent pour lui parler. Quand les agents communiquent, se délèguent du travail ou se passent une tâche, le mouvement est visible en temps réel dans l'espace. Le projet est open source, le dépôt est annoncé dans le premier commentaire du fil. witcheer a salué l'initiative.

> Source : [@iamlukethedev, Hermes3D, 20 août 2026](https://x.com/iamlukethedev/status/2090403072837362117)

## Resetwatch suit les quotas du bureau Nous

Le 20 août, Adolan a lancé Resetwatch, un outil communautaire pour Hermes Desktop de Nous Research. Il affiche le quota restant et l'heure de réinitialisation de chaque fenêtre de modèle : ce qui reste, et quand le compte est de nouveau disponible. Les plans Nous, Claude, Codex, Cursor et Kimi apparaissent sur une carte, avec le nom du plan.

L'outil fonctionne sans qu'aucune conversation ne soit ouverte. Teknium a relayé la publication en le jugeant utile pour beaucoup d'utilisateurs.

> Source : [@adolandev, Resetwatch, 20 août 2026](https://x.com/adolandev/status/2090312525237633145)

## Hermes Cloud présenté comme l'ordinateur distant de l'agent

Le 20 août, Nous Research a consacré un fil à Hermes Cloud : Hermes Agent a son propre ordinateur distant, sur lequel on n'est pas verrouillé, pour quelques dollars par mois au lieu de 200. Le fil compare les différences, notamment la possibilité de connecter n'importe quel provider, abonnement ou modèle.

> Source : [@NousResearch, Hermes Cloud, 20 août 2026](https://x.com/NousResearch/status/2090432358969196548)

## Sources

- [@NousResearch - SkillEvaluator sur les skills, 20 août 2026](https://x.com/NousResearch/status/2090166128509096187)
- [@imbabybrooklyn - Accent picker, 20 août 2026](https://x.com/imbabybrooklyn/status/2090352831299527009)
- [@iamlukethedev - Hermes3D, 20 août 2026](https://x.com/iamlukethedev/status/2090403072837362117)
- [@adolandev - Resetwatch, 20 août 2026](https://x.com/adolandev/status/2090312525237633145)
- [@NousResearch - Hermes Cloud, 20 août 2026](https://x.com/NousResearch/status/2090432358969196548)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
