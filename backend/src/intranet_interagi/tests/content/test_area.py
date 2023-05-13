from intranet_interagi.content.area import Area
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component import createObject
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def payload() -> dict:
    """Payload to create a new Área."""
    return {
        "type": CONTENT_TYPE,
        "email": "limi@plone.org",
        "ramal": "1975",
        "id": "alex-limi",
        "title": "Alex Limi"
    }


class TestArea:
    @pytest.fixture(autouse=True)
    def _fti(self, get_fti, integration):
        self.fti = get_fti(CONTENT_TYPE)

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    def test_create(self, portal, payload):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Area)

    def test_review_state(self, portal, payload):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        assert api.content.get_state(content) == "internal"

    def test_transition_editor_cannot_publish_internally(self, portal, payload):
        with api.env.adopt_roles(["Editor"]):
            content = api.content.create(container=portal, **payload)
            with pytest.raises(api.exc.InvalidParameterError) as exc:
                api.content.transition(content, "publish_internally")
        assert api.content.get_state(content) == "internal"

    def test_transition_reviewer_can_publish_internally(self, portal, payload):
        with api.env.adopt_roles(["Manager"]):
            content = api.content.create(container=portal, **payload)
        with api.env.adopt_roles(["Reviewer", "Member"]):
            api.content.transition(content, "publish_internally")
        assert api.content.get_state(content) == "internally_published"

    def test_subscriber_added_with_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                predio="sede",
                ramal="2022",
            )
        assert area.exclude_from_nav is False

    def test_subscriber_added_without_predio_value(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                ramal="2022",
            )
        assert area.exclude_from_nav is True

    def test_subscriber_moddified_is_changing_excluded_from_nav_status(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                ramal="2022",
            )

        assert area.exclude_from_nav is True

        area.predio = "Sede"
        # Area é o objeto que foi modificado
        notify(ObjectModifiedEvent(area))

        assert area.exclude_from_nav is False

    def test_subscriber_group_creating_new_group_when_is_created_area(self, portal):
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=portal,
                type=CONTENT_TYPE,
                title="Marketing",
                description="Área de Marketing",
                email="mktg@plone.org",
                ramal="2022",
            )
            groupname = '{}_editors'.format(area.UID())
            roles = api.group.get_roles(
                groupname=groupname,
                obj=area
            )
        assert "Editor" in roles
