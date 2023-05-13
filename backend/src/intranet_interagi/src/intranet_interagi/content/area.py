from intranet_interagi import _
from intranet_interagi.validadores import do_validation
from intranet_interagi.validadores import is_valid_email
from intranet_interagi.validadores import is_valid_ramal
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


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

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        do_validation(data)


@implementer(IArea)
class Area(Container):
    """Uma área."""
