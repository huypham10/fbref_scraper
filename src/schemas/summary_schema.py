from schemas import BaseMatchLogModel
from decimal import Decimal

class MatchPlayerSummaryRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from summary table in fbref.
    """
    
    goals: int | None
    assists: int | None
    pens_made: int | None
    pens_att: int | None
    shots: int | None
    shots_on_target: int | None
    cards_yellow: int | None
    cards_red: int | None
    touches: int | None
    tackles: int | None
    interceptions: int | None
    blocks: int | None
    xg: Decimal | None
    npxg: Decimal | None
    xg_assist: Decimal | None
    sca: int | None
    gca: int | None
    passes_completed: int | None
    passes: int | None
    passes_pct: Decimal | None
    progressive_passes: int | None
    carries: int | None
    progressive_carries: int | None
    take_ons: int | None
    take_ons_won: int | None