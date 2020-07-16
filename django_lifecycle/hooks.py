BEFORE_SAVE = "before_save"
AFTER_SAVE = "after_save"
AFTER_SAVE_RELATED = "after_save_related"

BEFORE_CREATE = "before_create"
AFTER_CREATE = "after_create"

BEFORE_UPDATE = "before_update"
AFTER_UPDATE = "after_update"
AFTER_UPDATE_RELATED = "after_update_related"

BEFORE_DELETE = "before_delete"
AFTER_DELETE = "after_delete"


VALID_HOOKS = (
    BEFORE_SAVE,
    AFTER_SAVE,
    AFTER_SAVE_RELATED,
    BEFORE_CREATE,
    AFTER_CREATE,
    BEFORE_UPDATE,
    AFTER_UPDATE,
    AFTER_UPDATE_RELATED,
    BEFORE_DELETE,
    AFTER_DELETE
)
