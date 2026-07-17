# Plugins

Distributions register entry points under `medical_imaging_dashboard.plugins`.
A plugin exposes `name`, `version`, `description`, and `render()`. Prediction and
feature backends implement protocols in `integrations/contracts.py`. Plugins
should catch model-specific failures and return serializable, provenance-rich
results.

```toml
[project.entry-points."medical_imaging_dashboard.plugins"]
example = "example_plugin:ExamplePlugin"
```

