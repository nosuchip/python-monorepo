# Python monorepo experiments

This branch contains pdm-related experiments. Each package/app initialized with `pdm init`, packages make installabel/buildable.

# Dependencies

- apps1:
  - fastapi
  - pkg-database
- app2:
  - fastapi
  - pkg-requests
- app3:
  - fastapi
  - pkg-settings

# NOTES

Failed to add editable dependency from package to package

```
$ pdm add -p packages/pkg-database -e ./packages/pkg-settings
[PdmUsageError]: Cannot add editables to the default or optional dependency group
```

same

```
$ pdm add -p packages/pkg-database -e ./packages/pkg-settings -G dev-dependencies
[PdmUsageError]: Cannot add editables to the default or optional dependency group
```
