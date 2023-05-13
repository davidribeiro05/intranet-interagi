from intranet_interagi import _
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer

import re


def is_valid_ramal(value: str) -> bool:
    """Validar se o ramal tem 4 dígitos númericos."""
    return re.match(r"^\d{4}$", value) if value else True


def is_valid_email(value: str) -> bool:
    """Validar se o email é @plone.org."""
    return value.endswith("@plone.org") if value else True


class IArea(Schema):
    """Uma Área."""

    model.fieldset(
        "default",
        _("Default"),
        fields=["email", "ramal"],
    )

    # Basic info
    ramal = schema.TextLine(title=_("Ramal"), required=False, constraint=is_valid_ramal)
    email = Email(title=_("Email"), required=False, constraint=is_valid_email)


@implementer(IArea)
class Area(Container):
    """Uma área."""
