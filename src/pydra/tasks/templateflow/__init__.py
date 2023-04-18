"""Pydra tasks for TemplateFlow."""

__all__ = ["get_template"]

import functools
import os

from templateflow import api as _api

import pydra


def _get_template(template_id: str, output_queries: dict) -> dict:
    return dict(
        {"template_description": _api.get_metadata(template=template_id)},
        **{output: _api.get(template=template_id, **entities) for output, entities in output_queries.items()},
    )


def get_template(output_queries: dict, **kwargs) -> pydra.engine.task.FunctionTask:
    """Get template using the TemplateFlow Python client.

    Parameters
    ----------
    output_queries : dict
        Mapping of output names to file queries.
    kwargs : dict
        Task parameters.

    Returns
    -------
    pydra.engine.task.FunctionTask
        Pydra task for querying template files.

    Examples
    --------
    >>> task = get_template(template_id="MNI152Lin", output_queries={"t1w": {"resolution": "1", "suffix": "T1w"}})
    >>> result = task()
    >>> result.output.template_description  # doctest: +ELLIPSIS
    {... 'Identifier': 'MNI152Lin', ...}
    >>> result.output.t1w  # doctest: +ELLIPSIS
    PosixPath('.../tpl-MNI152Lin_res-01_T1w.nii.gz')
    """

    output_queries = output_queries or {}

    name = kwargs.pop("name", "get_template")

    input_spec = pydra.specs.SpecInfo(name="Input", fields=[("template_id", str)], bases=(pydra.specs.BaseSpec,))

    output_spec = pydra.specs.SpecInfo(
        name="Output",
        fields=[("template_description", dict)] + [(str(key), os.PathLike) for key in output_queries.keys()],
        bases=(pydra.specs.BaseSpec,),
    )

    return pydra.engine.task.FunctionTask(
        func=functools.partial(_get_template, output_queries=output_queries),
        name=name,
        input_spec=input_spec,
        output_spec=output_spec,
        **kwargs,
    )
