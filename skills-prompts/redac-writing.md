# Documentation Section Writing

Write the final documentation section by section from the planning material already prepared in `docs/`.

This skill is for drafting final Markdown documentation files. It is not for planning, exploring the repository, verifying the code, reviewing the final document, or rendering/exporting the final format.

## Core Principles

Write clear, useful, source-grounded documentation.

Follow the redaction plan exactly: tone, audience, structure, section order, technical depth, formatting rules, and section-level instructions.

Treat user-specific requirements recorded in the redaction plan as binding constraints. This includes document size, expected length, level of detail, tone, writing preferences, structure, architecture, examples, diagrams, priorities, exclusions, and final format.

Do not invent missing behavior. If a fact is not present in `docs/`, do not add it.

Prefer precise technical writing over generic explanation.

Do not add plausible technical details just because they are common. This includes endpoints, HTTP status codes, error response formats, Docker Compose snippets, Makefile targets, commands, environment variables, defaults, limits, ports, CI steps, dependencies, or examples unless they are explicitly present in the redaction plan or supporting files in `docs/`.

## Source Boundary

The only authorized source directory is `docs/`.

You must read only documents located inside `docs/`.

Do not read source code, prompts, configuration files, tests, repository files, generated artifacts outside `docs/`, or any other folder.

Do not verify the code yourself under any circumstance. The codebase has already been explored by previous agents, and all usable information is already in `docs/`.

If a technical detail is missing from `docs/`, treat it as missing. Do not inspect the repository to recover it.

If the redaction plan mentions repository files such as `app/main.py`, `tools.py`, `Dockerfile`, or `Makefile`, treat them only as paths reported by the documents in `docs/`. This does not authorize you to read those files.

The current supporting source documents in `docs/` are:

- the current `*-design.md`: user preferences, selected documentation direction, audience, scope, constraints, and final structure intent
- `codebase-map.md`: repository map and inspection status
- `technical-findings.md`: primary technical evidence source

## Output Boundary

Write output files only inside `docsgen/`.

Do not write inside `docs/`. Do not write inside the source tree. Do not create files in any other directory.

Create `docsgen/` if it does not exist.

Write Markdown files only.

## Required Input

Before writing, read the redaction plan located in `docs/`,and all the files inside via multi-files read.

If several redaction plans exist, use the one that best matches the user's current request. Prefer the most recent relevant plan.

The redaction plan is the main authority for:

- document objective
- user requirements and preferences
- target audience
- tone
- structure
- section order
- section instructions
- required evidence
- requested document size and expected length
- expected depth
- formatting rules
- rendering/export constraints
- review criteria

Use other files in `docs/` only to support the section being written, and only when the redaction plan indicates that they are relevant. For technical facts, prefer `technical-findings.md`; use `codebase-map.md` for inspection status and repository structure; use the design document for user preferences and documentation direction.

## Writing Scope

Write the documentation in small batches of two sections per file.

Do not write all sections in one file.

Default batches:

- Sections 1 and 2
- Sections 3 and 4
- Sections 5 and 6
- Continue the same pattern until all sections are drafted

If the document has an odd number of sections, the final file may contain one section only.

If the user or workflow asks for a specific pair of sections, write only that pair.

If no specific pair is requested, write the next missing pair based on the files already present in `docsgen/`.

Before writing a new pair, check which earlier section files already exist in `docsgen/` and avoid repeating their explanations. Use them only to maintain continuity and transitions.

## File Naming

Use clear file names that preserve order.

Recommended pattern:

```text
docsgen/YYYY-MM-DD-<topic>-sections-01-02.md
docsgen/YYYY-MM-DD-<topic>-sections-03-04.md
docsgen/YYYY-MM-DD-<topic>-sections-05-06.md
```

Use zero-padded section numbers when possible.

If the topic is unclear, use a concise topic inferred from the redaction plan.

## Writing Rules

For each section:

- Follow the exact section goal from the redaction plan.
- Cover all required content.
- Use the section-level evidence provided in the plan.
- Preserve the intended section order and hierarchy.
- Respect the expected length and depth.
- Respect user-specific preferences recorded in the plan, including document size, level of detail, tone, structure, examples, diagrams, priorities, exclusions, and final format.
- Respect the style and formatting rules from the plan.
- Use tables, examples, code blocks, or diagrams only when the plan asks for them or when they clearly improve the section.
- Avoid content that the plan says belongs in another section.
- Pay special attention to duplication: do not repeat definitions, architecture overviews, setup steps, warnings, tool descriptions, configuration tables, examples, or conclusions already covered in previous sections.
- Avoid repeating material already assigned to another section. If a reminder is necessary, keep it short and refer back to the earlier idea instead of rewriting it.
- Each section must add new value according to its role in the redaction plan.
- Phrase uncertainties cautiously when the plan marks information as uncertain.
- Do not convert open questions or missing information into documentation content. If Docker Compose, an endpoint, an error code, a command, or a target is marked as missing or uncertain, omit it or clearly state that it is not documented.

Do not include planning notes, local review criteria, internal reasoning, or commentary in the generated documentation.

The output files must read like final documentation, not like a plan.

## Technical Writing Rules

When writing technical sections, include concrete details from `docs/`:

- names
- file paths
- functions or classes
- endpoints
- inputs and outputs
- parameters
- return values
- constraints
- limits
- defaults
- commands
- environment variables
- data flow
- dependencies
- known edge cases

Do not use vague wording when precise facts are available.

Do not add API endpoints, status codes, error payloads, deployment modes, Makefile commands, Docker Compose examples, or configuration values unless the plan or `docs/` explicitly provides them.

Bad:

- "The application exposes an API."

Good:

- "The API exposes `POST /generate`, which receives a user message and returns the agent response with a session identifier."

## Markdown Requirements

Use clean Markdown.

Preserve the heading levels expected by the redaction plan.

Do not wrap the whole file in code fences.

Use inline code formatting for paths, commands, variables, functions, classes, endpoints, and schema names.

Use fenced code blocks only for actual examples.

Keep prose readable and structured. Avoid giant paragraphs.

## Completion Behavior

After writing the file or files, respond with:

1. The created file path or paths.
2. The sections written.
3. Any missing information that affected the writing.
4. The next section pair to write, if any.

If no file was created, state clearly why.
