"""
Define a base model for all data validation models.
"""

from enum import Enum
from pathlib import Path, PurePath
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, computed_field


# ------------- Custom types -----------------------------------

class BaseMatchLogModel(BaseModel):
    """
    Base Matchlog model for validating input data.
    """
    player_id: str
    team_id: str
    match_id: str
    minutes: int

    model_config = ConfigDict(extra='forbid')
