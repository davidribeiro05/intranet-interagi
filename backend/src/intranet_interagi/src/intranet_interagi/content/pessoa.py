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


class IPessoa(Schema):
    """Uma Pessoa."""

    model.fieldset(
        "default",
        _("Default"),
        fields=["title", "email", "ramal"],
    )

    # Basic info
    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Bio"), required=False)
    email = Email(title=_("Email"), required=False, constraint=is_valid_email)
    ramal = schema.TextLine(title=_("Ramal"), required=False, constraint=is_valid_ramal)

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        do_validation(data)


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa."""
