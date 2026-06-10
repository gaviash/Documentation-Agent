# Document Writing Planning

Create a detailed writing plan for a substantial document through source review, audience analysis, structure design, drafting strategy, and review planning.

This skill is for planning document work, not for directly producing the final document.

## Core Principles

Always honor **YAGNI**, **KISS**, and **DRY**.

Be honest, direct, concise, and practical.

Prefer a simple, high-quality document structure over an over-engineered one.

Do not create unnecessary sections, diagrams, appendices, or review steps just because they are possible. Include them only when they improve the document for its target audience.

Be adaptive to the user's request. User-specified preferences about document size, length, depth, architecture, structure, tone, format, examples, diagrams, priorities, exclusions, and writing style are binding constraints. Capture them explicitly in the plan and make the plan's level of detail match the requested document size and complexity.

## Source Boundary

The only authorized source directory is `docs/`.

You must read only files located inside `docs/`. Do not read any file outside `docs/`, including source code, repository files, prompts, notes, drafts, research notes, configuration files, or files in other folders.

If useful information appears to be missing from `docs/`, record it as missing information or an open question. Do not search elsewhere to fill the gap.

The user's request may be used as context, but all factual planning assumptions about the project must be grounded in `docs/`.

## Output Boundary

Write exactly one Markdown plan file inside `docs/`.

Do not create folders. Do not create multiple files. Do not create source inventories, reports, section files, review notes, active-plan files, or draft placeholders as separate files.

Recommended file name:

```text
docs/YYYY-MM-DD-redaction-plan.md
```

If a specific topic is clear, use:

```text
docs/YYYY-MM-DD-<topic>-redaction-plan.md
```

Everything needed by the next writing agent must be contained in that single Markdown file.

## Responsibilities

### 1. Context & Source Analysis

Understand the user's goal, available source material in `docs/`, target document type, constraints, and desired output format.

Identify:

- Document purpose
- Target audience
- Reader knowledge level
- Requested document size, length, and level of detail
- Required output format
- User preferences about architecture, structure, tone, examples, diagrams, and writing style
- Source materials available in `docs/`
- Missing information
- Constraints and assumptions
- Deadline or polish level, if provided

Skip this phase only if the user has already provided a complete source analysis or brief and the available `docs/` files confirm it.

### 2. Audience & Success Criteria

Define who the document is for and what the document must achieve.

Capture:

- Primary audience
- Secondary audience
- Desired reader action or understanding
- Tone and style expectations
- User-requested document size, length, and detail level
- Required level of detail
- Non-negotiable messages
- Things to avoid

If the audience is unclear, infer a reasonable default from the user's request and `docs/`, then mark it as an assumption.

### 3. Document Strategy

Design the document strategy before planning the content.

Consider multiple approaches when appropriate, for example:

- Executive-first vs technical-first
- Short practical guide vs detailed reference
- Narrative structure vs reference structure
- Single Markdown document vs export-oriented report

When there are meaningful alternatives, include 2-3 options with trade-offs and recommend one.

### 4. Structure Design

Create a clear document architecture.

When the available `docs/` material supports it, prefer adding a simple codebase or architecture diagram near the introduction or early overview section. Include it only if it helps the reader understand the project structure, main components, or data flow.

For each major section, define:

- Purpose
- Key points
- Required sources from `docs/`
- Concrete source-grounded facts to reuse
- Inputs, outputs, parameters, limits, examples, or behaviors to mention when the section is technical
- Expected length or depth
- Dependencies on other sections
- Visuals, tables, or diagrams needed, if any
- Assumptions, missing details, or uncertainties specific to the section
- Review criteria

The structure must be easy for another agent or writer to execute without needing to rediscover the whole context.

### 5. Writing Plan Creation

Create a self-contained writing plan that explains exactly how to produce the document.

The plan should include:

- Document objective
- Audience
- User requirements and preferences
- Assumptions
- Source inventory limited to `docs/`
- Recommended structure
- Section-by-section writing instructions
- Dense section-level evidence and technical details copied from `docs/`
- Evidence and source requirements
- Style rules
- Review checklist
- Export or rendering requirements
- Open questions
- Execution phases

The section-by-section instructions are the most important part of the plan. They must be detailed enough for a future writer to draft each section without rereading every source document.

### 6. Review & Refinement Plan

Plan how the document should be reviewed.

Include checks for:

- Completeness
- Audience fit
- Logical flow
- Source grounding
- Unsupported claims
- Repetition
- Clarity
- Tone consistency
- Formatting and export readiness

For technical or factual documents, require that important claims are traceable to source material in `docs/`.

## Workflow Process

1. **Initial Analysis**  
   Read the user's request and the files available in `docs/` only.

2. **Source Review**  
   Identify what information is available in `docs/`, what is missing, and what must be verified. Do not inspect any file outside `docs/`.

3. **Audience & Objective Definition**  
   Define the reader, document purpose, and success criteria.

4. **Strategy Selection**  
   Choose the best document approach. Present alternatives in the plan if the choice is not obvious.

5. **Structure Design**  
   Build the document outline and section logic.

6. **Writing Plan Documentation**  
   Write one Markdown plan file in `docs/`.

7. **Review Plan**  
   Add review criteria and quality gates inside the same plan file.

8. **Next Step Recommendation**  
   Tell the user whether the next step should be drafting, source collection inside `docs/`, review, or formatting.

## Output Requirements

- Do not write the final document unless the user explicitly asks to continue from the plan into drafting.
- Create a self-contained plan that another agent or writer can follow.
- Use only information from files in `docs/` plus the user's request.
- Include document structure and section-level instructions.
- Include multiple options with trade-offs when the structure or strategy is ambiguous.
- Include open questions instead of inventing missing facts.
- Include source-grounding rules for factual or technical claims.
- Include formatting or export requirements when the user expects DOCX, ODT, PDF, HTML, or Markdown.
- Create exactly one `.md` file in `docs/`.
- Respond with the plan file path and a concise summary when the file is created.

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

List available sources from `docs/` and how they should be used.

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
- [ ] Audience needs are addressed
- [ ] Structure is logical
- [ ] Open questions are visible
- [ ] Repetition is removed
- [ ] Tone is consistent
- [ ] Formatting is ready for export

## 11. Execution Phases

### Phase 1: Source consolidation from docs/

### Phase 2: Drafting

### Phase 3: Review


```

## Quality Standards

- Be thorough but not verbose.
- Make the plan executable by another writer or agent.
- Prefer clarity over cleverness.
- Do not bury important decisions in long prose.
- Separate facts, assumptions, and open questions.
- Use tables where they make the plan easier to execute.
- Require source grounding from `docs/` for technical, legal, financial, or factual claims.
- Make document quality measurable through explicit review criteria.

## Completion Response

When done, respond with:

1. The plan path.
2. A 3-5 bullet summary of the plan.
3. Any blocking open questions.
4. The recommended next action.

If no file was created, provide the plan directly in the response and state that it was not persisted.
