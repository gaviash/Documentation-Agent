# DocumentationAgent

DocumentationAgent est un prototype termine de workflow multi-agents pour produire une documentation de codebase a partir d'un dossier cible.

Le projet valide une chaine complete : cadrage utilisateur, exploration de codebase, production de documents de preparation, plan de redaction, redaction par sections, review legere, puis rendu final avec Pandoc.

## Principe

Les agents sont construits avec LlamaIndex `FunctionAgent` et utilisent des modeles Ollama. Chaque agent recoit un prompt specialise depuis `skills-prompts/`, precede par un prompt general commun.

Le projet cible a documenter est attendu dans `process/`. Les documents intermediaires sont ecrits dans `docs/`, les sections redigees dans `docsgen/`, puis le document final est genere dans `docsgen/`.

Les outils exposes aux agents permettent de lire/ecrire/editer des fichiers, executer certaines commandes shell, faire de la recherche web via Tavily et lancer Pandoc pour le rendu final.

## Agents et fichiers transmis

### BrainstormingAgent

Role : cadrer la demande, poser les questions utiles, proposer des approches, explorer la codebase, puis produire les documents de preparation.

Il lit le projet dans `process/` et produit dans `docs/` :

- `YYYY-MM-DD-<topic>-design.md`
- `codebase-map.md`
- `technical-findings.md`

Ces fichiers contiennent l'orientation documentaire, la carte de codebase et les faits techniques utiles aux agents suivants.

### WritingPlanAgent

Role : transformer les documents de preparation en plan de redaction.

Il lit uniquement les fichiers de `docs/` et produit :

- `YYYY-MM-DD-<topic>-redaction-plan.md`

Le plan contient la structure finale, le ton, les contraintes utilisateur, les sections attendues, les sources a utiliser et la checklist de review.

### WritingAgent

Role : rediger la documentation finale par morceaux.

Il lit le plan et les fichiers autorises dans `docs/`, puis produit dans `docsgen/` des fichiers Markdown par paires de sections :

- `YYYY-MM-DD-<topic>-sections-01-02.md`
- `YYYY-MM-DD-<topic>-sections-03-04.md`
- `YYYY-MM-DD-<topic>-sections-05-06.md`

### ReviewAgent

Role : faire une review legere avant export.

Il lit le plan de redaction et les sections produites dans `docsgen/`. Il ne relit pas la codebase et ne refait pas d'audit technique. Son travail consiste surtout a corriger les problemes de formulation, redondance, coherence, syntaxe, Markdown et conformite au plan.

Il peut produire un rapport de review court dans `docsgen/`.

### DocAgent

Role : preparer le rendu final.

Il nettoie les eventuelles coquilles de jonction en debut/fin de fichiers, concatene les sections si necessaire, puis lance Pandoc pour generer le document final.

Le rendu DOCX utilise le fichier de reference Pandoc place a la racine :

- `reference-doc.docx`

## Pandoc et rendu final

Le rendu final s'appuie sur Pandoc. La commande utilisee par le DocAgent est adaptee selon les fichiers disponibles, mais suit cette forme :

```bash
pandoc docsgen/documentation.md \
  --from markdown+pipe_tables+fenced_code_blocks+fenced_divs+smart \
  --to docx \
  --toc \
  --number-sections \
  --reference-doc ../reference-doc.docx \
  -o docsgen/documentation.docx
```

Si les fichiers Markdown ne sont pas concatenes avant rendu, Pandoc peut recevoir plusieurs fichiers d'entree dans le bon ordre.

## Fichiers principaux

- `app/agents.py` : declaration des modeles, agents et fonction commune `query`.
- `app/workflow.py` : orchestration de debug des etapes du workflow.
- `app/tools.py` : outils exposes aux agents, avec garde-fous de workspace, limites de sortie, edition ciblee et support multi-file read.
- `skills-prompts/general_prompt.md` : cadre commun injecte avant les prompts specialises.
- `skills-prompts/brainstorming_agent.txt` et `skills-prompts/brainstorming.md` : prompts du `BrainstormingAgent`.
- `skills-prompts/redac-planning.md` : prompt du planificateur de redaction.
- `skills-prompts/redac-writing.md` : prompt de l'agent de redaction.
- `skills-prompts/redac-review.md` : prompt du ReviewAgent.
- `skills-prompts/doc-agent.md` : prompt du DocAgent.
- `requirements.txt` : dependances Python.

## Configuration

La configuration passe par un fichier `.env` local, ignore par Git.

Variables importantes :

- `OLLAMA_MODEL`
- `REVIEW_MODEL`
- `OLLAMA_API_KEY`
- `PROMPTS_DIR`
- `TAVILY_API_KEY`
- `WORKSPACE_DIR`
- variables Langfuse, si l'observabilite est activee

Le workflow utilise Langfuse/OpenInference pour tracer les appels agents quand la configuration est disponible.

Dependances notables :

- LlamaIndex
- Ollama
- Tavily
- Langfuse / OpenInference
- Pandoc

## Etat et limites du projet

Le repo est considere comme termine au sens prototype : la chaine complete existe et peut produire un document final correct.

Les resultats obtenus sont globalement bons et exploitables. En revanche, la methode actuelle est tres instable et couteuse. Elle repose sur le fait de laisser les agents gerer presque toutes les decisions, lectures, corrections et transitions entre etapes. Cette approche est sensible aux prompts, a la casse, aux noms de fichiers, aux sorties tronquees, aux comportements repetitifs des agents et aux erreurs de parsing ou de format.

Le workflow peut aussi consommer un nombre tres important de tokens pour produire une documentation relativement courte. Sur certaines runs, l'ordre de grandeur approche 500k tokens pour un seul document. C'est disproportionne pour une generation documentaire classique.

En clair : ce prototype prouve que le workflow multi-agents fonctionne et peut produire une documentation correcte, mais la methode est a revoir. Une version plus robuste devrait probablement reduire l'autonomie des agents, passer davantage de chemins explicites, limiter les lectures, simplifier les etapes, mieux structurer les donnees intermediaires et eviter de faire "raisonner" les agents sur toute la chaine.
