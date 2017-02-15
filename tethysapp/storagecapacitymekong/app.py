from tethys_sdk.base import TethysAppBase, url_map_maker


class MekongStorageCapcity(TethysAppBase):
    """
    Tethys app class for Mekong Storage Capcity.
    """

    name = 'Mekong Storage Capacity'
    index = 'storagecapacitymekong:home'
    icon = 'storagecapacitymekong/images/dam.svg'
    package = 'storagecapacitymekong'
    root_url = 'storagecapacitymekong'
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
                           url='storagecapacitymekong',
                           controller='storagecapacitymekong.controllers.home'),
        )

        return url_maps