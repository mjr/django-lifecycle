from .hooks import AFTER_SAVE_RELATED, AFTER_UPDATE_RELATED


class LifecycleSerializerMixin(object):
    def create(self, validated_data):
        instance = super(LifecycleSerializerMixin, self).create(validated_data)

        instance._run_hooked_methods(AFTER_SAVE_RELATED)

        return instance


    def update(self, instance, validated_data):
        instance = super(LifecycleSerializerMixin, self).update(instance, validated_data,)

        instance._run_hooked_methods(AFTER_UPDATE_RELATED)

        return instance
