from intranet_interagi import logger
from intranet_interagi.content.area import Area
from plone import api
from zope.lifecycleevent import ObjectAddedEvent


def _create_group(obj: Area):
    """Create user groups for the new Area."""
    uid = api.content.get_uuid(obj)
    title = obj.title
    payload = {
        "groupname": f"{uid}_editors",
        "title": f"Editores para {title}",
        "description": f"Students for the {title} session",
    }
    editors = api.group.create(**payload)
    api.group.grant_roles(group=editors, roles=["Editor"], obj=obj)
    logger.info(
        f"Granted role of Editor to {uid}_editors group on {obj.absolute_url()}"
    )


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Group."""
    _create_group(obj)


def updated(obj: Area, event: ObjectAddedEvent):
    """Post updated handler for Group."""
    _create_group(obj)
