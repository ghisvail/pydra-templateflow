# pydra-templateflow

----

Pydra tasks for TemplateFlow.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[TemplateFlow][templateflow] provides a framework
for publicly hosting and distributing neuroimaging templates
for human and nonhuman brains.

** Table of contents **

- [Available tasks](#available-tasks)
- [Installation](#installation)
- [Development](#development)
- [License](#license)

## Available tasks

This package provides a `get_template` task, which takes a mandatory `template_id` argument
and an optional `output_entities` mapping from output names to their respective query entities.

The following example showcases using `get_template` to download the template image,
brain and head masks for the Linear ICBM Average Brain (ICBM152).

```python
from pydra.tasks import templateflow

task = templateflow.get_template(
    template_id="MNI152Lin",
    output_entities={
        "brain_mask": {"resolution": "1", "suffix": "mask", "desc": "head"},
        "head_mask": {"resolution": 1, "suffix": "mask", "desc": "brain"},
        "t1w_image": {"resolution": "1", "suffix": "T1w"},
    },
)

result = task()
```

Please check the list of available templates [here][templateflow-browse].  

## Installation

```console
pip install pydra-templateflow
```

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test
```

To fix linting issues:

```console
hatch run lint:fix
```

## License

This project is distributed under the terms of the [Apache License, Version 2.0][license].

[pydra]: https://pydra.readthedocs.io/
[templateflow]: https://www.templateflow.org/
[templateflow-browse]: https://www.templateflow.org/browse/
[hatch]: https://hatch.pypa.io/
[license]: https://spdx.org/licenses/Apache-2.0.html
