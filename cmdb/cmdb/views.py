from prototypes import viewsets


class AppRootView(viewsets.RootView):

    url_list = {
        'Inventory': 'inventory-root',
        'Change Management': 'change-root',
        'Core': 'core-root',
    }

