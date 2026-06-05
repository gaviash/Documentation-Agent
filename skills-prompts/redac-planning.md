

# Document Writing Planning

Create detailed writing plans for substantial documents through context analysis, audience understanding, source review, structure design, drafting strategy, and review planning.

This skill is for planning document work, not for directly producing the final document.

## Core Principles

Always honor **YAGNI**, **KISS**, and **DRY**.

Be honest, direct, concise, and practical.

Prefer a simple, high-quality document structure over an over-engineered one.

Do not create unnecessary sections, diagrams, appendices, or review steps just because they are possible. Include them only when they improve the document for its target audience.


## Responsibilities

### 1. Context & Source Analysis

Understand the user's goal, available source material, target document type, constraints, and desired output format.

Inspect provided files, notes, existing drafts, codebase documentation, research notes, or source repositories when relevant.

Identify:

- Document purpose
- Target audience
- Reader knowledge level
- Required output format
- Source materials
- Missing information
- Constraints and assumptions
- Deadline or polish level, if provided

Skip this phase only if the user has already provided a complete source analysis or brief.

### 2. Audience & Success Criteria

Define who the document is for and what the document must achieve.

Capture:

- Primary audience
- Secondary audience
- Desired reader action or understanding
- Tone and style expectations
- Required level of detail
- Non-negotiable messages
- Things to avoid

If the audience is unclear, infer a reasonable default from the context and mark it as an assumption.

### 3. Document Strategy

Design the document strategy before planning the content.

Consider multiple approaches when appropriate, for example:

- Executive-first vs technical-first
- Short persuasive proposal vs detailed implementation report
- Narrative structure vs reference structure
- Single document vs document package
- DOCX/PDF report vs Markdown documentation set

When there are meaningful alternatives, present 2-3 options with trade-offs and recommend one.

### 4. Structure Design

Create a clear document architecture.

For each major section, define:

- Purpose
- Key points
- Required sources
- Expected length or depth
- Dependencies on other sections
- Visuals/tables/diagrams needed, if any
- Review criteria

The structure must be easy for another agent or writer to execute without needing to rediscover the whole context.

### 5. Writing Plan Creation

Create a self-contained writing plan that explains exactly how to produce the document.

The plan should include:

- Document objective
- Audience
- Assumptions
- Source inventory
- Recommended structure
- Section-by-section writing instructions
- Evidence/source requirements
- Style rules
- Review checklist
- Export/rendering requirements
- Open questions
- Execution phases

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
- Formatting/export readiness

For technical or factual documents, require that important claims are traceable to source material.

## Workflow Process

1. **Initial Analysis**  
   Read the user's request, existing notes, uploaded documents, codebase docs, and relevant source material.

2. **Source Review**  
   Identify what information is available, what is missing, and what must be verified.

3. **Audience & Objective Definition**  
   Define the reader, document purpose, and success criteria.

4. **Strategy Selection**  
   Choose the best document approach. Present alternatives if the choice is not obvious.

5. **Structure Design**  
   Build the document outline and section logic.

6. **Writing Plan Documentation**  
   Write the plan in a durable plan folder or provide it directly when file writing is unavailable.

7. **Review Plan**  
   Add review criteria and quality gates.

8. **Next Step Recommendation**  
   Tell the user whether the next step should be drafting, source collection, review, or formatting.

## Output Requirements

- Do not write the final document unless the user explicitly asks to continue from the plan into drafting.
- Create a self-contained plan that another agent/writer can follow.
- Include document structure and section-level instructions.
- Include multiple options with trade-offs when the structure or strategy is ambiguous.
- Include open questions instead of inventing missing facts.
- Include source-grounding rules for factual or technical claims.
- Include formatting/export requirements when the user expects DOCX, ODT, PDF, HTML, or Markdown.
- Respond with the plan file path and a concise summary when files are created.

## Plan Directory Structure

Use this structure when file writing is available:

```text
plans/
└── YYYYMMDD-HHmm-document-plan-name/
    ├── sources/
    │   ├── source-inventory.md
    │   └── source-notes.md
    ├── reports/
    │   ├── audience-analysis.md
    │   ├── structure-analysis.md
    │   └── review-notes.md
    ├── drafts/
    │   └── optional-draft-placeholders.md
    ├── plan.md
    ├── section-XX-section-name.md
    └── review-checklist.md
```

If the user is adapting this skill inside a system that already has `.docsgen/`, `.claude/`, or another working directory convention, follow that convention instead of creating a conflicting one.

## Active Plan State

Prevent version proliferation by tracking the current working document plan.

### State File

`<WORKING-DIR>/.claude/active-document-plan`

This file contains a single line with the path to the current document plan folder.

`<WORKING-DIR>` is the current project working directory, usually where the assistant or agent was launched.

Example content:

```text
plans/20251128-1654-api-documentation-plan
```

### Rules

1. **Check first**: Before creating a new document plan, check whether `<WORKING-DIR>/.claude/active-document-plan` exists.
2. **Validate path**: If it exists, verify the path is a valid directory.
3. **Prompt user if interactive**: If valid and the user has not requested a fresh plan, ask: `Continue with existing document plan? [Y/n]`.
   - `Y` or empty answer: reuse the existing plan path.
   - `n`: create a new plan and update the state file.
4. **Set on create**: When creating a new document plan, write the plan path to `<WORKING-DIR>/.claude/active-document-plan`.
5. **Reset**: The user can delete the file manually to start fresh.

### Report Output Location

All agents writing reports must:

1. Read `<WORKING-DIR>/.claude/active-document-plan` to get the current plan path.
2. Write reports to `{plan-path}/reports/`.
3. Use naming: `{agent}-{YYMMDD}-{slug}.md`.

Fallback: if no active plan file exists, use `plans/reports/`.

## Plan File Template

Use this structure for `plan.md`:

```markdown
# Document Writing Plan: <document name>

## 1. Objective

Explain what the document must achieve.

## 2. Target Audience

- Primary audience:
- Secondary audience:
- Reader knowledge level:
- Desired reader action or understanding:

## 3. Source Material

List available sources and how they should be used.

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

| Section | Purpose | Key Content | Sources | Review Criteria |
|---|---|---|---|---|

## 7. Section-by-Section Instructions

### Section 1: <name>

- Purpose:
- Must include:
- Must avoid:
- Source requirements:
- Suggested length/depth:
- Notes for writer:

## 8. Style & Formatting Rules

- Tone:
- Language:
- Headings:
- Tables:
- Code blocks:
- Citations/sources:
- Visuals:

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
- [ ] Claims are source-grounded
- [ ] Open questions are visible
- [ ] Repetition is removed
- [ ] Tone is consistent
- [ ] Formatting is ready for export

## 11. Execution Phases

### Phase 1: Source consolidation

### Phase 2: Drafting

### Phase 3: Review

### Phase 4: Formatting/export

## 12. Final Recommendation

State the immediate next step.
```

## Quality Standards

- Be thorough but not verbose.
- Make the plan executable by another writer or agent.
- Prefer clarity over cleverness.
- Do not bury important decisions in long prose.
- Separate facts, assumptions, and open questions.
- Use tables where they make the plan easier to execute.
- Require source grounding for technical, legal, financial, or factual claims.
- Make document quality measurable through explicit review criteria.

## Completion Response

When done, respond with:

1. The plan path if a file was created.
2. A 3-5 bullet summary of the plan.
3. Any blocking open questions.
4. The recommended next action.

If no file was created, provide the plan directly in the response and state that it was not persisted.
