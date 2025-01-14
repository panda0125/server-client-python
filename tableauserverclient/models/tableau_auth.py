class TableauAuth(object):
    def __init__(self, username, password, site=None, site_id=None, user_id_to_impersonate=None):
        if site is not None:
            import warnings

            warnings.warn(
                "TableauAuth(..., site=...) is deprecated, " "please use TableauAuth(..., site_id=...) instead.",
                DeprecationWarning,
            )
            site_id = site
        if password is None:
            raise TabError("Must provide a password when using traditional authentication")

        self.user_id_to_impersonate = user_id_to_impersonate
        self.password = password
        self.site_id = site_id if site_id is not None else ""
        self.username = username

    @property
    def site(self):
        import warnings

        warnings.warn(
            "TableauAuth.site is deprecated, use TableauAuth.site_id instead.",
            DeprecationWarning,
        )
        return self.site_id

    @site.setter
    def site(self, value):
        import warnings

        warnings.warn(
            "TableauAuth.site is deprecated, use TableauAuth.site_id instead.",
            DeprecationWarning,
        )
        self.site_id = value

    @property
    def credentials(self):
        return {"name": self.username, "password": self.password}
