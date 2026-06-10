# Document Writing Planning

Create one detailed writing plan for the final documentation.

This skill is for planning only. Do not write the final documentation.

## Core Principles

Be practical, clear, source-grounded, and adaptive to the user's request.

User-specified preferences are binding constraints: document size, length, depth, architecture, structure, tone, format, examples, diagrams, priorities, exclusions, and writing style.

The plan must match the requested document size and complexity. A small requested document needs a compact but precise plan; a larger or more technical document needs denser section instructions.

Prefer a simple, high-quality structure over unnecessary sections, diagrams, appendices, or review steps.

## Source Boundary

The only authorized source directory is `docs/`.

Read only files located inside `docs/`. Do not read source code, repository files, prompts, notes, drafts, configuration files, or files in other folders.

Use the user's request as context, but all factual planning assumptions about the project must be grounded in `docs/`.

If useful information is missing from `docs/`, record it as missing information or an open question. Do not search elsewhere.

When `docs/` mention paths such as `app/main.py`, `app/tools.py`, `Dockerfile`, or `Makefile`, treat them as reported facts from documentation, not as files you personally inspected. In the plan, list only documents from `docs/` as source material. Code paths may appear inside section evidence for traceability, but never in the `Source Material From docs/` table as direct sources.

Do not turn missing information or open questions into writing requirements. If Docker Compose, an endpoint, a Makefile target, an error format, an HTTP status code, an environment variable, or a command is not explicitly documented in `docs/`, mark it as missing or omit it.

## Output Boundary

Write exactly one Markdown plan file inside `docs/`.

Do not create folders. Do not create multiple files. Do not create separate source inventories, reports, section files, review notes, active plans, or draft placeholders.

Recommended file name:

```text
docs/YYYY-MM-DD-redaction-plan.md
```

If a specific topic is clear, use:

```text
docs/YYYY-MM-DD-<topic>-redaction-plan.md
```

Everything needed by the next writing agent must be contained in that single Markdown file.

## Planning Requirements

The plan must include:

- document objective
- user requirements and preferences
- target audience and desired reader outcome
- source inventory limited to files in `docs/`
- assumptions, missing information, and open questions
- recommended strategy and alternatives when useful
- proposed document structure
- detailed section-by-section writing instructions
- style and formatting rules
- rendering/export requirements
- review checklist
- execution phases

When the available `docs/` material supports it, prefer a simple codebase or architecture diagram near the introduction or early overview section. Include it only if it improves comprehension.

The section-by-section instructions are the most important part of the plan. They must be detailed enough for a future writer to draft each section without rereading every source document.

## Plan File Template

Use this structure for the single plan Markdown file:

```markdown
# Document Writing Plan: <document name>

## 1. Objective

Explain what the document must achieve.

## 1.1 User Requirements And Preferences

- Requested document size:
- Expected length:
- Expected level of detail:
- Required tone:
- Required structure or architecture:
- Required format:
- Requested examples, diagrams, tables, or code snippets:
- Priorities:
- Exclusions:
- Other writing preferences:

## 2. Target Audience

- Primary audience:
- Secondary audience:
- Reader knowledge level:
- Desired reader action or understanding:

## 3. Source Material From docs/

List only files that are actually inside `docs/`.

Do not list repository source files such as `app/main.py`, `tools.py`, `Dockerfile`, `Makefile`, or CI files here. If those paths are mentioned by documents in `docs/`, include them only inside section evidence as traceability.

| Source | Type | Relevance | Notes |
|---|---|---|---|

## 4. Assumptions & Open Questions

### Assumptions

- ...

### Open Questions

- ...

## 5. Recommended Strategy

Explain the chosen writing approach and why.

### Alternatives Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|

## 6. Proposed Document Structure

| Section | Purpose | Key Content | Sources From docs/ | Review Criteria |
|---|---|---|---|---|

## 7. Section-by-Section Instructions

### Section 1: <name>

#### Section Goal

Explain what this section must achieve for the reader.

#### Required Content

List the concrete points that must be covered.

#### Evidence And Technical Details From docs/

Copy the relevant facts from `docs/` directly into this section instruction.

Do not only point to source file names. Source names are useful for traceability, but the writer must have enough factual material here to draft the section.

Include only facts explicitly supported by `docs/`. Do not add plausible defaults, common framework behavior, endpoints, status codes, Docker Compose examples, Makefile targets, commands, environment variables, limits, or error formats unless they are clearly present in `docs/`.

For technical sections, include concrete names, paths, responsibilities, inputs, outputs, parameters, return values, constraints, limits, examples, defaults, data flow, dependencies, and known edge cases whenever they are available in `docs/`.

For API sections, include endpoint paths, HTTP methods, request fields, response fields, schemas, session behavior, errors or limitations if documented, and example payloads when enough information is available.

For tool sections, include each tool name, purpose, parameters, return shape, constraints, timeouts, output limits, safety rules, external services used, and example use cases when documented.

For configuration or deployment sections, include environment variables, required/optional status, defaults, ports, commands, Docker or CI facts, runtime dependencies, and operational constraints when documented.

Avoid vague summaries such as "the project has several tools" or "the API handles requests". Replace them with precise reusable facts.

#### Suggested Local Structure

- Opening idea:
- Main explanation blocks:
- Table, example, or diagram needed:
- Closing transition:

#### Must Avoid

List details that belong in another section, are unsupported by `docs/`, or would create noise.

#### Assumptions And Uncertainties

List assumptions, missing information, and open questions that affect this section.

#### Suggested Length / Depth

State whether the section should be short, medium, or detailed, and give an approximate length when useful.

#### Notes For Writer

Give concrete tone, structure, transition, and clarity advice for this specific section.

#### Local Review Criteria

- [ ] ...

## 8. Style & Formatting Rules

- Tone:
- Language:
- Headings:
- Tables:
- Code blocks:
- Citations/sources:
- Visuals: include a simple codebase or architecture diagram in the introduction or early overview when `docs/` contains enough source-grounded information and the diagram improves comprehension.

## 9. Rendering / Export Requirements

- Source format:
- Final format(s):
- Template/style requirements:
- Assets required:
- Known rendering constraints:

## 10. Review Checklist

- [ ] Objective is clear
- [ ] User requirements are reflected
- [ ] Audience needs are addressed
- [ ] Structure is logical
- [ ] Section instructions contain enough evidence
- [ ] Claims are grounded in `docs/`
- [ ] Open questions are visible
- [ ] Repetition is avoided
- [ ] Tone is consistent
- [ ] Formatting is ready for export

## 11. Execution Phases

### Phase 1: Source consolidation from docs/

### Phase 2: Drafting

### Phase 3: Review
```

## Quality Standards

- Make the plan executable by another writer or agent.
- Capture user preferences explicitly.
- Keep facts, assumptions, and open questions separate.
- Prefer concrete section-level evidence over abstract guidance.
- Use tables when they make the plan easier to execute.
- Require source grounding from `docs/` for technical, legal, financial, or factual claims.
- Do not invent missing facts or convert open questions into documentation requirements.
- Make document quality measurable through explicit review criteria.

## Completion Response

When done, respond with:

1. The plan path.
2. A 3-5 bullet summary of the plan.
3. Any blocking open questions.
4. The recommended next action.

If no file was created, provide the plan directly in the response and state that it was not persisted.
