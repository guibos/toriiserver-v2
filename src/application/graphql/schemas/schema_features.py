from graphql import ResolveInfo


class SchemaFeatures:
    @staticmethod
    def _get_session(*, info: ResolveInfo):
        return info.context['session']
