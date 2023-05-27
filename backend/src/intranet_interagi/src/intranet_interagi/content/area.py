from intranet_interagi import _
from plone import api
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer


class IArea(Schema):
    """Uma Área."""

    # Basic info
    title = schema.TextLine(title=_("Nome da área"), required=True)
    description = schema.Text(title=_("Sumário"), required=False)


@implementer(IArea)
class Area(Container):
    """Uma área."""

    @property
    def pessoas(self):
        relations = api.relation.get(target=self, relationship="area")
        return [i.from_object for i in relations]
