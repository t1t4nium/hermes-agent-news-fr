# Quotidien d'actualité Hermes Agent

Chaque jour, une nouvelle édition couvre l'actualité de Hermes Agent et de
Nous Research, les nouvelles releases et fonctionnalités, ainsi que l'évolution
de l'écosystème.

Chaque édition est identifiée par un numéro incrémenté (#1, #2, #3, etc.), et
classée par année de publication dans le répertoire correspondant `YYYY/`.

Skills dédiées :
- `.hermes/skills/hermes-agent-news-fr` pour écrire le Quotidien ;
- `.hermes/skills/humanizer` pour humaniser un texte et supprimer les AI-isms/tics d'IA.

## Règles

- Hallucinations et inventions strictement interdites.
- Les affirmations et les écrits doivent être sourcés.
- Pas de répétition/redondance avec les éditions précédentes.
- Bannir les AI-isms et les tics d'IA.
- Ton : à l'identique des autres éditions, technique et posé.
- Langue : en français.
- Nom de fichier : YYYY-MM-DD-hermes-agent-news-digest-n.md (n = numéro édition).
- Quand un sujet pointe une ressource consultable (exemples : page, dépôt,
  documentation, article), ouvrir ce lien et enrichir le sujet avec les informations
  vérifiables qu'il apporte. Toute donnée ajoutée reste rattachée à la source.
- Ne pas répéter dans le corps d'un sujet une information déjà portée par sa
  ligne de sources, sauf si elle est nécessaire au récit.

## Sources

Les sources se trouvent dans le fichier `data/sources.json`.

## Fonctionnement

Deux tâches planifiées automatisent le quotidien.

- La collecte des tweets X tourne toutes les quatre heures et écrit les tweets
  des dernières 24h dans `data/x/YYYY-MM-DD.json`, à partir des comptes listés
  dans `data/sources.json`.
- L'écriture de l'édition tourne une fois par jour et suit le process ci-dessous.
  Elle lit les tweets collectés et le flux des releases, puis écrit l'édition
  du jour.

Une tâche hebdomadaire assure le suivi du projet et de la production.

Les données (`data/`), les scripts (`scripts/`) et les skills (`.hermes/skills/`)
vivent dans le dépôt git, à la racine. Seuls les dumps de tweets (`data/x/`)
restent hors du suivi git.

## Process

Pour écrire l'édition du jour :
1. Déterminer la date du jour et l'heure (par exemple avec la commande `date`).
2. Lire les deux dernières éditions pour éviter de répéter un sujet déjà couvert.
3. Identifier le numéro de l'édition précédente et incrémenter pour définir le
   numéro de l'édition du jour.
4. Consulter les dernières releases depuis le dépôt GitHub de Hermes Agent
   (méthode détaillée dans la skill `hermes-agent-news-fr`).
5. Consulter les tweets des dernières 24h disponibles dans `data/x/YYYY-MM-DD.json`
   (méthode de sourçage détaillée dans la skill `hermes-agent-news-fr`).
6. Sélectionner des sujets jamais couverts (uniquement actualité, fonctionnalité,
   release et usage).
7. Écrire l'édition en résumant puis en traduisant en français chaque sujet
   sélectionné. Pour les releases, lister et résumer en une phrase chaque
   changement apporté.
8. Relire le fichier écrit et s'assurer que tous les mots français sont bien
   accentués, et qu'il n'y a aucun tic d'IA.

## Format

```markdown
# Hermes Agent Quotidien #<numéro édition>

Petite introduction sur les sujets couverts.

<pour chaque sujet>
## Titre du sujet

Contenu.

> Sources avec lien + auteur + titre ou description + date
</pour chaque sujet>

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
```
