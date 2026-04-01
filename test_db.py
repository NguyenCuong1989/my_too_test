import sys
import os
sys.path.append(os.path.abspath("balancehub"))

from balancehub.app.core.db import SessionLocal, init_db
from balancehub.app.services.gssi_service import compute_system_health
from balancehub.app.core.models import ConnectorCatalog
from sqlalchemy import select

try:
    init_db()
    print("init_db OK")
    db = SessionLocal()
    res = db.execute(select(ConnectorCatalog)).scalars().all()
    print("Queries OK. Found", len(res), "catalogs.")
    health = compute_system_health(db)
    print("Health OK:", health)
except Exception as e:
    import traceback
    traceback.print_exc()
