from qube.src.api import persist_db


class friday_demo(persist_db.Document):
    # Primary ID
    id = persist_db.StringField(required=False)

    # friday_demo  model data
    name = persist_db.StringField(required=False)
    description = persist_db.StringField(required=False)

    # Default tracking data
    createdBy = persist_db.StringField(required=False)
    modifiedBy = persist_db.StringField(required=False)
    orgId = persist_db.StringField(required=True)
    tenantId = persist_db.StringField(required=True)
    createdDate = persist_db.StringField(required=False)
    modifiedDate = persist_db.StringField(required=True)
