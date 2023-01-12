## Flake8 Declarative Dict
This was a experimental flake8 plugin to enforce the use of declarative dicts in Python.

## Use case
```python
// Wrong
a = {
    "a":1,
    "b":2
    "c":3
}

// Right
a = {}
a["a"] = 1
a["b"] = 2
a["c"] = 3
```

## Disclaimer
I didn't come up with this rule, just created the plugin. I don't know the pourpose of this rule