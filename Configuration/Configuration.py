class Configuration:

    class __Configuration:
        def __init__(self):
            self.configuration = {}


    __instance = None
    def __new__(cls):
        if not Configuration.__instance:
            Configuration.__instance = Configuration.__Configuration()
        return Configuration.__instance