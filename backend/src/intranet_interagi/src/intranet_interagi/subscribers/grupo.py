from intranet_interagi import logger
from intranet_interagi.content.area import Area
from plone import api
from zope.lifecycleevent import ObjectAddedEvent


def _create_group(obj: Area):
    """Create group after create Área."""
    title = "{}_editors".format(obj.title)
    groupname = "{}_editors".format(obj.UID())

    group = api.group.create(
        groupname=groupname,
        title=title,
        description="Just a description",
        roles=[
            "Editor",
        ],
        groups=[
            "Editors",
        ],
    )

    logger.info(f"Novo grupo criado para {title} - {groupname}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Group."""
    _create_group(obj)


def updated(obj: Area, event: ObjectAddedEvent):
    """Post updated handler for Group."""
    _create_group(obj)
