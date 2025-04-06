# Project Workflow Prompts

## TASK SPECIFIC

- CHANGE THE TASK SPECIFIC PROMPT TO THE TASK YOU ARE CURRENTLY WORKING ON.

```xml
<task>
    <start="RERUN_15" priority="high">Utilize Textuals verbose platform and its best practises.</start>
        <ref type="context" source="Textual-Moc.md">If you need documentation for context, use <Textual-Moc.md>. It will lead you to more context and examples in the <Textual-Docs> directory.</ref>
</task>
```

## EAP WORKFLOW

- CHANGE THE TASK `<start="RERUN_15"` FOR THE CORRECT STEP

```xml
<task>
    <start="EAP-8" priority="high">Initiate Corrections, Utilize Textuals verbose platform and its best practises.</start>
        <ref type="context" source="Textual-Moc.md">If you need documentation for context, use <Textual-Moc.md>. It will lead you to more context and examples in the <Textual-Docs> directory.</ref>
</task>
```
