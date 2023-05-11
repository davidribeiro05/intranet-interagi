"""Portal settings tests."""
from plone import api


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    def test_portal_title(self, portal):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Intranet Interagi - Modificado"
        assert value == expected
    
    def test_portal_timezone(self, portal):
        """Test Timezone"""
        value = api.portal.get_registry_record("plone.available_timezones")[0]
        expected = "America/Sao_Paulo"
        assert value == expected
    
    def test_portal_email(self, portal):
        """Test E-mail has changed"""
        value = api.portal.get_registry_record("plone.email_from_name")
        expected = "Intranet Interagi"
        assert value == expected

    def test_portal_twitter_name(self, portal):
        """Test Twitter Name"""
        value = api.portal.get_registry_record("plone.twitter_username")
        expected = "devdavidribeiro05"
        assert value == expected
    
    def test_portal_sitemap(self, portal):
        """Test Sitemap"""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        assert value is True