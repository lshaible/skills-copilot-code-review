"""
Endpoints for announcements.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Optional

from fastapi import APIRouter

from ..database import announcements_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


@router.get("/active", response_model=Optional[Dict[str, Any]])
def get_active_announcement() -> Optional[Dict[str, Any]]:
    """Get the announcement that has not expired."""
    announcement = announcements_collection.find_one(
        {"expires_at": {"$gt": datetime.now(timezone.utc)}},
        {"_id": 0}
    )
    return announcement
