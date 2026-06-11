# DocumentationAgent

DocumentationAgent est un prototype de workflow multi-agents pour produire une documentation de codebase a partir d'un dossier cible.

Le projet cherche a decouper le travail de documentation en etapes specialisees : cadrer la demande, explorer le projet, produire des documents de preparation, planifier la redaction, puis ecrire la documentation finale par sections.

## Principe

Les agents sont construits avec LlamaIndex `FunctionAgent` et utilisent un modele Ollama. Chaque agent recoit un prompt specialise depuis `skills-prompts/`, precede par un prompt general commun.

Les outils disponibles permettent notamment de :

- lire et ecrire des fichiers dans le workspace ;
- lire plusieurs fichiers en une seule operation quand c'est pertinent ;
- executer des commandes shell controlees ;
- faire de la recherche ou de l'extraction web via Tavily.

Le projet cible a documenter est attendu dans `process/`. Les documents intermediaires sont ecrits dans `docs/`, puis les sections redigees dans `docsgen/`. Ces dossiers sont ignores par Git car ils contiennent des donnees de travail ou des generations locales.

## Agents et passage de fichiers

Le workflow est encore en phase de debug, mais il s'organise autour de trois agents principaux qui se transmettent des fichiers Markdown.

### BrainstormingAgent

Role : cadrer la demande utilisateur et preparer la base de travail.

L'agent inspecte le projet dans `process/`, pose les questions necessaires sur la documentation attendue, propose plusieurs approches a valider, puis explore plus finement la codebase selon l'approche choisie.

Il produit dans `docs/` :

- `YYYY-MM-DD-<topic>-design.md`
- `codebase-map.md`
- `technical-findings.md`

Ces fichiers contiennent respectivement l'orientation documentaire, la carte de codebase et les faits techniques detailles.

### WritingPlanAgent

Role : transformer les documents de preparation en plan de redaction.

Il lit uniquement les fichiers dans `docs/`, en particulier :

- le document de design ;
- `codebase-map.md` ;
- `technical-findings.md`.

Il produit dans `docs/` :

- `YYYY-MM-DD-<topic>-redaction-plan.md`

Ce plan precise la structure finale, les sections a ecrire, le ton, la taille attendue, les sources a utiliser et les contraintes utilisateur.

### WritingAgent

Role : rediger la documentation finale par morceaux.

Il lit le plan de redaction et les documents autorises dans `docs/`. Il ne relit pas la codebase directement.

Il produit dans `docsgen/` des fichiers Markdown par paires de sections, par exemple :

- `YYYY-MM-DD-<topic>-sections-01-02.md`
- `YYYY-MM-DD-<topic>-sections-03-04.md`
- `YYYY-MM-DD-<topic>-sections-05-06.md`

Les futurs agents prevus sont un agent de review et un agent de mise en forme/export, mais ils ne sont pas encore implementes.

## Fichiers principaux

- `app/agents.py` : declaration du modele Ollama, des agents et de la fonction commune `query`.
- `app/workflow.py` : orchestration de debug des etapes du workflow.
- `app/tools.py` : outils exposes aux agents, avec garde-fous de workspace, limites de sortie et support multi-file read.
- `skills-prompts/general_prompt.md` : cadre commun injecte avant les prompts specialises.
- `skills-prompts/brainstorming_agent.txt` et `skills-prompts/brainstorming.md` : prompts du `BrainstormingAgent`.
- `skills-prompts/redac-planning.md` : prompt du planificateur de redaction.
- `skills-prompts/redac-writing.md` : prompt de l'agent de redaction.
- `requirements.txt` : dependances Python du prototype.

`app/main.py` est actuellement vide dans l'etat suivi du repo.

## Configuration

La configuration passe par un fichier `.env` local, ignore par Git.

Variables importantes :

- `OLLAMA_MODEL`
- `OLLAMA_API_KEY`
- `PROMPTS_DIR`
- `TAVILY_API_KEY`
- `WORKSPACE_DIR`
- variables Langfuse, si l'observabilite est activee

Le workflow utilise aussi Langfuse/OpenInference pour tracer les appels agents quand la configuration est disponible.

## Etat du projet

Le repo est un prototype actif. Le `BrainstormingAgent` a progressivement recu une responsabilite supplementaire : il ne fait plus seulement le cadrage, il produit aussi les documents techniques de preparation necessaires au planner.

Le README donne une vue d'ensemble du fonctionnement. Les consignes fines de comportement, les limites de lecture, les formats attendus et les regles anti-invention sont portees par les prompts dans `skills-prompts/`.
