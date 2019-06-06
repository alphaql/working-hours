from api.general.views import GeneralViewSet


class GameViewSet(GeneralViewSet):
    def list(self, request, *args, **kwargs):

        path_file = 'resources/json/test-1.json'

        self.set_file_path(path_file)
        # self.set_d    ata_from_str('{"test":1}')

        return super(GameViewSet, self).list(request, args, kwargs)

