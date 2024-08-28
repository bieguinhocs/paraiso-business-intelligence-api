from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Your Project Admin"
    site_title = "Your Project Admin Portal"
    index_title = "Welcome to the Admin Portal"

    app_ordering = {
        'locations': {
            'AddressDepartment': 1,
            'AddressCity': 2,
            'AddressZoneGroup': 3,
            'AddressDistrict': 4,
            'Address': 5,
        },
    }

    def get_app_list(self, request, app_label=None):
        # Llama al método original de Django para obtener la lista de aplicaciones
        app_list = super().get_app_list(request)

        # Si se ha seleccionado una aplicación específica, filtra solo esa aplicación
        if app_label:
            app_list = [app for app in app_list if app['app_label'] == app_label]

        # Ordena los modelos dentro de cada aplicación según app_ordering
        for app in app_list:
            if app['app_label'] in self.app_ordering:
                ordering = self.app_ordering[app['app_label']]
                app['models'].sort(
                    key=lambda x: ordering.get(x['object_name'], 100)
                )

        # Si app_label es None, ordena las aplicaciones según lo definido en get_app_order
        if app_label is None:
            app_list.sort(key=lambda x: self.get_app_order(x['app_label']))

        return app_list

    def get_app_order(self, app_label):
        app_order = {
            'auth': 1,
            'users': 2,
            'locations': 3,
        }
        return app_order.get(app_label, 100)

# Instancia del AdminSite personalizado
custom_admin_site = MyAdminSite(name='custom_admin')
