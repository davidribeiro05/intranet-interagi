from intranet_interagi import logger
from intranet_interagi.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent


def _update_exclude_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    predio = obj.predio
    obj.exclude_from_nav = False if predio else True
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_exclude_from_nav(obj)


def updated(obj: Area, event: ObjectAddedEvent):
    """Post updated handler for Area."""
    _update_exclude_from_nav(obj)
