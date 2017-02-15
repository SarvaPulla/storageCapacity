from tethys_sdk.base import TethysAppBase, url_map_maker


class MekongStorageCapcity(TethysAppBase):
    """
    Tethys app class for Mekong Storage Capcity.
    """

    name = 'Mekong Storage Capacity'
    index = 'scm:home'
    icon = 'storagecapacitymekong/images/dam.svg'
    package = 'storagecapacitymekong'
    root_url = 'scm'
    color = 'blue'
    description = 'Storage Capacity'
    tags = 'StorageCapacity'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='scm',
                           controller='storagecapacitymekong.controllers.home'),
        )

        return url_maps