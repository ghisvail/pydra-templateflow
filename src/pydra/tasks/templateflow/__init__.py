"""Pydra tasks for TemplateFlow."""

__all__ = ["get_template"]

from templateflow import api as _api

import pydra


@pydra.mark.task
def get_template(template_id: str, output_queries: dict) -> dict:
    """Get template using the TemplateFlow Python client.

    Parameters
    ----------
    template_id : str
        Template identifier to download.
    output_queries : dict
        Mapping of output names to file queries.

    Returns
    -------
    template_description : dict
        Metadata associated with the template.
    **output_names : path-like
        Path to the downloaded file for each query.

    Examples
    --------
    >>> task = get_template(template_id="MNI152Lin")
    >>> task()  # doctest: +ELLIPSIS
    Result(...)
    """

    output_queries = output_queries or {}

    return dict(
        {"template_description": _api.get_metadata(template=template_id)},
        **{
            output: _api.get(template=template_id, **entities)
            for output, entities in output_queries.items()
        }
    )
