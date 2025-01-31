from pydantic.validators import str_validator
from typing import Optional
from schemas import BaseMatchLogModel
from decimal import Decimal

def empty_to_none(v: str) -> Optional[str]:
    if v == '':
        return None
    return v

class EmptyStrToNone(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield empty_to_none

class MatchPlayerPassRow(BaseMatchLogModel):

    passes_completed: int | None
    passes: int | None
    passes_pct: Decimal | None
    passes_total_distance: int | None
    passes_progressive_distance: int | None
    passes_completed_short: int | None
    passes_short: int | None
    passes_pct_short: Decimal | None
    passes_completed_medium: int | None
    passes_medium: int | None
    passes_pct_medium: Decimal | None
    passes_completed_long: int | None
    passes_long: int | None
    passes_pct_long: Decimal | None
    assists: int | None
    xg_assist: Decimal | None
    pass_xa: Decimal | None
    assisted_shots: int | None
    passes_into_final_third: int | None
    passes_into_penalty_area: int | None
    crosses_into_penalty_area: int | None
    progressive_passes: int | None