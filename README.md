# Le Quotidien d'actualité Hermes Agent

L'actualité [Hermes Agent](https://github.com/NousResearch/hermes-agent) résumée et traduite en français, tous les jours.

Le quotidien est produit chaque jour par un workflow agentique incluant un agent Hermes. Le setup est décrit ci-dessous.

## Sources

L'actualité du projet, de [Nous Research](https://nousresearch.com/) et de la communauté, est récupérée :
- depuis le flux de releases GitHub du projet ;
- depuis les comptes X (Twitter) des fondateurs, développeurs et employés de Nous Research ;
- auprès des contributeurs majeurs du projet.

Les sources se trouvent dans le fichier `data/sources.json`.

## Workflow

Le workflow est simple :
1. Toutes les 4 heures, le script `scripts/collect_sources.py` collecte les données depuis les sources.
2. Tous les jours à 17h, l'agent écrit le quotidien sur la base des données collectées, puis le publie.
3. Tous les dimanches à 7h, un suivi hebdomadaire est réalisé pour s'assurer le bon fonctionnement du workflow et identifier les possibles améliorations.

## Setup

Prérequis :
- Hermes Agent doit être installé et fonctionnel ;
- Un email doit être configuré sur la gateway de l'agent pour recevoir l'output d'une cronjob par ce canal.

### Cloner le dépôt

J'ai construit le workflow agentique depuis l'espace de travail de mon agent : `/home/hermes/workspace`.

```
cd /home/hermes/workspace
git clone https://github.com/t1t4nium/hermes-agent-news-fr
```

### Autoriser les skills du dépôt

```
cd /home/hermes/workspace/hermes-agent-news-fr
hermes skills trust .
```

### Wrapper pour le script de collecte

Hermes Agent exige que les scripts appelés par cron soient dans `~/.hermes/scripts/`.
J'ai donc créé un wrapper pour ne pas devoir déplacer le script du repo.

`TARGET_SCRIPT` doit pointer vers le script de collecte dans le repo.

Créer `~/.hermes/scripts/collect_sources.py` :

```python
#!/usr/bin/env python3
"""Wrapper calling the project script for cron execution."""

import subprocess
import sys

TARGET_SCRIPT = "/home/hermes/workspace/hermes-agent-news-fr/scripts/collect_sources.py"

if __name__ == "__main__":
    res = subprocess.run([sys.executable, TARGET_SCRIPT] + sys.argv[1:])
    sys.exit(res.returncode)
```

### Les cronjobs

Pour la livraison de l'output des jobs par email, penser à modifier l'adresse
email de destination.

Pour les jobs agent, penser à sélectionner un modèle adapté. Par exemple DeepSeek V4 Pro.

#### Collecte des sources

```bash
hermes cron create "0 */4 * * *" \
  --no-agent \
  --script collect_sources.py \
  --workdir /home/hermes/workspace/hermes-agent-news-fr \
  --name "hermes-agent-news-fr : collecte des sources"
```

#### Écriture du quotidien

```
prompt=$(cat <<'EOF'
# Écrire le Quotidien d'actualité Hermes Agent

Objectif : écrire l'édition du jour.

Avant tout, détermine la date du jour via la commande `date`, puis vérifie que
la collecte des tweets du jour `data/x/YYYY-MM-DD.json` s'est bien déroulée en
comparant volume et structure de données avec la collecte de la veille.

Si tu soupçonnes un problème de collecte : exécute le script
`scripts/collect_sources.py` pour confirmer. S'il est avéré qu'il y a un
problème de collecte : tu n'écris pas l'édition du jour, tu analyses sans
modifier quoi que ce soit et en restant dans le périmètre du projet pour tenter
de déterminer la cause. Puis, rédige un rapport en précisant ce que tu as
analysé, ce qui ne va pas et comment corriger.

Si la collecte s'est bien déroulée : écrire l'édition du jour en respectant les
instructions du fichier AGENTS.md.
EOF
)
hermes cron create "0 17 * * *" \
  "$prompt" \
  --workdir /home/hermes/workspace/hermes-agent-news-fr \
  --deliver email:mail@example.com \
  --name "hermes-agent-news-fr : écrire l'édition du jour"
```

Activer les toolsets : `browser`, `file`, `terminal`, `web`.

#### Suivi hebdomadaire

```
prompt=$(cat <<'EOF'
# Suivi hebdomadaire du Quotidien Hermes Agent

Mission :
- S'assurer que les scripts et cronjobs produisent le résultat attendu, et que
  dans l'ensemble le process de production est fonctionnel et optimal.
- Identifier les anomalies, les erreurs, les manques, les lacunes et les
  dérives, et proposer des corrections ou améliorations.
- Identifier de nouvelles sources pour le quotidien (nouveau venu dans l'équipe
  de développement Hermes Agent, contributeur reconnu de la communauté ou de
  l'équipe de développement).

Rapport de mission :
- Ce qui a été analysé ;
- Ce qui ne va pas et comment corriger ;
- Ce qui pourrait être amélioré ;
- Les nouvelles sources identifiées (le cas échéant) ;
- Observations et remarques.

Si tout semble bon et fonctionner correctement, ne rien inventer et simplement
signaler, par un court message, que tout va bien.

Règles :
- Ne rien modifier
- Ne rien supprimer
- S'en tenir au périmètre du projet
EOF
)
hermes cron create "0 7 * * 0" \
  "$prompt" \
  --workdir /home/hermes/workspace/hermes-agent-news-fr \
  --deliver email:mail@example.com \
  --name "hermes-agent-news-fr : suivi hebdomadaire"
```

Activer les toolsets : `browser`, `file`, `terminal`, `web`.

## Licence

Le code de l'agent est sous licence MIT.

Le contenu produit pour le Quotidien est sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr).
