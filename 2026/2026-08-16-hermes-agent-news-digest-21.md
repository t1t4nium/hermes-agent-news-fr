# Hermes Agent Quotidien #21

Le panneau des capacités du desktop se dote d'une interface de gestion par profil, et witcheer dresse une liste de cinq PRs post-v0.20.0 qui méritent l'attention.

## Le panneau des capacités passe au crible par profil

Le 16 août, Teknium a dévoilé une refonte du panneau des capacités dans Hermes Agent Desktop. L'onglet permet maintenant de restreindre l'ensemble des skills, outils et MCPs à un profil ou un bot spécifique. Chaque profil peut ainsi n'exposer que les capacités qui le concernent, sans mélange avec la configuration globale.

Deuxième ajout : un navigateur de skills intégré. Depuis le panneau, on peut parcourir le catalogue et installer une skill directement, sans passer par la ligne de commande. Teknium a accompagné l'annonce d'une capture montrant la vue liste des capacités avec les toggles par profil et le bouton d'accès au skills browser.

> Source : [@Teknium, 16 août 2026](https://x.com/Teknium/status/2088874095345856541)

## Cinq PRs depuis v0.20.0 que witcheer recommande

Le 16 août, witcheer a publié une liste commentée de cinq pull requests fusionnées depuis la sortie de v0.20.0.

**/heartbeat (#79681) : donner un pouls à une session.** La commande `/heartbeat every 30m check the deployment` fixe une instruction récurrente qui réintègre la session comme un tour normal dès qu'elle est inactive et que l'intervalle est écoulé. L'agent continue d'avancer sur un travail long sans qu'on ait besoin de le relancer.

**Wake word mains-libres pour les agents distants (#79491).** Quand l'agent tourne sur un serveur ou Hermes Cloud mais que le micro est sur le portable, le desktop transmet désormais le flux audio au backend via la connexion authentifiée existante. La détection du mot de réveil fonctionne donc même quand l'agent n'a pas de microphone propre.

**read_file comprend les vrais documents (#79781).** Le PDF, les formats Office legacy (.doc, .ppt, .xls), OpenDocument, RTF et EPUB sont maintenant extraits automatiquement en texte clair. Le convertisseur s'installe seul au premier usage ; les formats existants restent inchangés.

**/learn peut digérer des livres entiers (#80804).** Pointé sur un ouvrage ou un corpus important, /learn construit une skill de connaissance structurée : un index léger et des fichiers de référence par chapitre chargés à la demande, au lieu de tout entasser dans un seul fichier.

**Les mises à jour du desktop deviennent transparentes, sur tous les OS (#83634).** L'application se ferme, `hermes update` s'exécute en arrière-plan, l'application se rouvre. Une petite fenêtre de statut suit l'opération, et chaque mise à jour rafraîchit aussi le mécanisme de mise à jour lui-même.

> Source : [@witcheer, 16 août 2026](https://x.com/witcheer/status/2089004661386686593)

## Witcheer benchmarke les quants de Qwen 3.8-27B

Le 16 août, witcheer a publié une analyse quantitative de la taxe de quantification sur Qwen 3.8-27B. Sept échelons GGUF testés sur une RTX 5090 : l'écart entre Q8_0 et le 2-bit est de 2,9 points, sans cliff à aucun seuil. Q6_K atteint Q8_0 à la deuxième décimale, ce qui rend le plus gros fichier de l'échelle inutile.

La valeur remarquable est UD-IQ3_XXS : 92,7 contre 93,7 pour Q8_0, pour un fichier de 11,1 Go à 96 tok/s. Assez pour loger un dense 27B dans une carte 16 Go à qualité quasi maximale. Même le plancher 2-bit à 9 Go tient 90,8, avec des pertes concentrées sur MMLU et HumanEval.

Ses recommandations : UD-Q4_K_XL sur les cartes 24 Go, UD-IQ3_XXS sur les 16 Go, et ignorer Q8_0.

> Source : [@witcheer, 16 août 2026](https://x.com/witcheer/status/2088940018144326007) - méthodologie complète dans le [Grimoire](https://t.me/witcheergrimoire)

## Sources

- [@Teknium - Panneau des capacités, 16 août 2026](https://x.com/Teknium/status/2088874095345856541)
- [@witcheer - 5 PRs depuis v0.20.0, 16 août 2026](https://x.com/witcheer/status/2089004661386686593)
- [@witcheer - Benchmark Qwen 3.8-27B, 16 août 2026](https://x.com/witcheer/status/2088940018144326007)
- [PR #79681 - /heartbeat](https://github.com/NousResearch/hermes-agent/pull/79681)
- [PR #79491 - Hands-free wake word remote agents](https://github.com/NousResearch/hermes-agent/pull/79491)
- [PR #79781 - read_file documents](https://github.com/NousResearch/hermes-agent/pull/79781)
- [PR #80804 - /learn digests whole books](https://github.com/NousResearch/hermes-agent/pull/80804)
- [PR #83634 - Desktop updates every OS](https://github.com/NousResearch/hermes-agent/pull/83634)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
