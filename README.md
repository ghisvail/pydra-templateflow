# pydra-templateflow

[![PyPI - Version][pypi-version]][pypi-project]
[![PyPI - Python Version][pypi-pyversions]][pypi-project]
[![PyPI - Downloads][pypi-downloads]][pypi-project]
![][status-test]

----

Pydra tasks for TemplateFlow.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[TemplateFlow][templateflow] provides a framework
for publicly hosting and distributing neuroimaging templates
for human and nonhuman brains.

**Table of contents**

- [Available tasks](#available-tasks)
- [Installation](#installation)
- [Development](#development)
- [License](#license)

## Available tasks

This package provides a `get_template` task, which takes a `template_id` argument
and a `output_queries` mapping from output names to their respective file queries.

The following example showcases using `get_template` to download the template image,
brain and head masks for the Linear ICBM Average Brain (ICBM152).

```python
from pydra.tasks import templateflow

task = templateflow.get_template(
    template_id="MNI152Lin",
    output_queries={
        "brain_mask": {"resolution": "1", "suffix": "mask", "desc": "head"},
        "head_mask": {"resolution": "1", "suffix": "mask", "desc": "brain"},
        "t1w_image": {"resolution": "1", "suffix": "T1w"},
    },
)

result = task()

# result.output.brain_mask
# result.output.head_mask
# result.output.t1w_image
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

[pypi-project]: https://pypi.org/project/pydra-templateflow/
[pypi-version]: https://img.shields.io/pypi/v/pydra-templateflow.svg
[pypi-pyversions]: https://img.shields.io/pypi/pyversions/pydra-templateflow.svg
[pypi-downloads]: https://static.pepy.tech/badge/pydra-templateflow
[status-test]: https://github.com/ghisvail/pydra-templateflow/actions/workflows/test.yaml/badge.svg
[pydra]: https://pydra.readthedocs.io/
[templateflow]: https://www.templateflow.org/
[templateflow-browse]: https://www.templateflow.org/browse/
[hatch]: https://hatch.pypa.io/
[license]: https://spdx.org/licenses/Apache-2.0.html
