# Hermes Agent Quotidien #82

Cette édition revient sur le plugin officiel REA pour rétro-ingénierer des programmes depuis Hermes, sur le score de Nemotron 3.5 Super VL au benchmark Hermes Bench, sur les 50 pull requests fusionnées le 15 octobre, et sur sem-weave, un plugin pour relire du code par fonction.

## REA, le plugin officiel pour rétro-ingénierer des programmes

Teknium a annoncé le 15 octobre le plugin officiel REA (Reverse Engineer Anything) pour Hermes Agent. L'installation tient en une commande, `hermes plugins install rea` puis `hermes plugins enable rea`, qui livre le serveur MCP REA plus une skill qui en détaille l'usage. Le plugin inspecte des exécutables et bibliothèques natifs, des assemblages .NET, des applications Electron et JavaScript, des paquets Android, des images de firmware, des captures réseau et navigateur, et le comportement en cours d'exécution de programmes. REA renvoie des preuves structurées, code décompilé, graphes d'appels, graphes d'application et captures, que Hermes explique ou réutilise comme base.

La fiche du catalogue précise le mécanisme. Le paquet, signé morluto (morluto/rea, licence MIT), épingle rea-agents@6.4.0, lancé via `npx -y rea-agents@6.4.0 mcp` en stdio à chaque session tant que le plugin est actif. Il expose environ 170 outils enregistrés sous `mcp__rea__<outil>`, gardés derrière la recherche d'outils à la demande de Hermes. L'analyse statique, JavaScript, Electron, archives, métadonnées .NET, ressources PE et captures HAR, ne demande que Node.js 22.19 ou plus récent. La décompilation native exige en revanche un moteur à fournir soi-même : Ghidra avec un JDK, Hopper ou IDA, JADX pour le code Android, Binwalk ou Unblob pour les firmwares. REA ne les installe pas, et la skill rappelle à l'agent de ne pas le faire non plus. Un budget d'appel par serveur propre à REA est prévu avec Hermes v0.23.0.

> Sources : [@Teknium, Check out the new official plugin I created for Hermes Agent, 15 octobre 2026](https://x.com/Teknium/status/2110736682207355062), [@witcheer, point Hermes Agent at an app and ask how it works, 15 octobre 2026](https://x.com/witcheer/status/2110740283805581507) et [rea, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/rea)

## Nemotron 3.5 Super VL noté 63,44 sur Hermes Bench

Nous Research a déclaré le 15 octobre que Hermes Agent est le meilleur endroit pour utiliser les nouveaux modèles Nemotron 3.5 Super VL et Bolt de NVIDIA. D'après Nous Research, NVIDIA a mesuré Super VL sur Hermes Bench avec un score de 63,44 et, face à des modèles locaux comparables, le modèle affiche jusqu'à 5 fois le débit en jetons.

NVIDIA décrit Super VL comme un modèle ouvert qui combine raisonnement et usage d'outils avec la compréhension du texte, des images, des documents et de la vidéo, pour des agents au long cours : 120 milliards de paramètres au total, dont 12 milliards actifs.

> Sources : [@NousResearch, Hermes Agent is the best place to use the new NVIDIA Nemotron 3.5 Super VL and Bolt models, 15 octobre 2026](https://x.com/NousResearch/status/2110786024024445201) et [@NVIDIAAI, Meet NVIDIA Nemotron 3.5 Super VL, 15 octobre 2026](https://x.com/NVIDIAAI/status/2110749836450713896)

## 50 pull requests fusionnées le 15 octobre

iamlukethedev a fait le compte le 16 octobre : Hermes a fusionné 50 pull requests le 15 octobre. Les changements mis en avant :

- Une installation neuve se pose sur la dernière release stable, au lieu du bout de la branche main.
- `hermes update` ne refuse plus le canal stable quand git tarde à trouver la nouvelle release.
- La commande /loop affiche désormais une vue en direct.

> Sources : [@iamlukethedev, Hermes merged 50 PRs on October 15, 16 octobre 2026](https://x.com/iamlukethedev/status/2111056522470174956)

## sem-weave, relire du code par fonction

witcheer a signalé le 16 octobre l'entrée de sem-weave au catalogue de plugins : l'agent relit le code par fonction plutôt que ligne à ligne. On peut lui demander où une fonction est définie et qui l'appelle, et obtenir la définition plus chaque appelant avec son fichier et sa ligne.

La fiche du catalogue précise que le paquet, signé Ataraxy Labs (Ataraxy-Labs/sem), apporte deux skills : sem-code-review pour trouver fonctions et classes, inspecter les appelants et relire les diffs Git par entité, et weave-merge-preview pour examiner la fusion d'une branche sans l'appliquer. Le paquet ajoute des instructions, pas des outils, et passe par le terminal et le flux d'approbation existants de l'hôte. Il demande Sem (testé en 0.27.0) et, en option, Weave (0.5.4), installés séparément.

> Sources : [@witcheer, sem-weave is now in the Hermes plugin catalog, 16 octobre 2026](https://x.com/witcheer/status/2111079713456427356) et [sem-weave, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/sem-weave)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
