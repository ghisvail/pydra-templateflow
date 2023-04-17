"""Pydra tasks for TemplateFlow.

>>> from pydra.tasks import templateflow 
"""

__all__ = ["get_template"]

from templateflow import api as _api

import pydra


@pydra.mark.task
def get_template(template_id: str, output_queries: dict) -> dict:
    """Get template using the TemplateFlow Python client."""

    output_queries = output_queries or {}

    return dict(
        {"template_description": _api.get_metadata(template=template_id)},
        **{
            output: _api.get(template=template_id, **entities)
            for output, entities in output_queries.items()
        }
    )
