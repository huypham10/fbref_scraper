"""
Pydantic models to validate data scraped from matches on fbref.
"""

from pydantic.validators import str_validator
from typing import Optional
from schemas import BaseMatchLogModel
from decimal import Decimal
from pydantic import Field

def empty_to_none(v: str) -> Optional[str]:
    if v == '':
        return None
    return v

class EmptyStrToNone(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield empty_to_none

class MatchPlayerSummaryRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from summary table for matches.
    """
    
    goals: int | None = Field(description="Number of goals")
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


class MatchPlayerPassRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from passing table for matches.
    """

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


class MatchPlayerPassTypeRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from passing type table for matches.
    """

    passes_live: int | None
    passes_dead: int | None
    passes_free_kicks: int | None
    through_balls: int | None
    passes_switches: int | None
    crosses: int | None
    throw_ins: int | None
    corner_kicks: int | None
    corner_kicks_in: int | None
    corner_kicks_out: int | None
    corner_kicks_straight: int | None
    passes_offsides: int | None
    passes_blocked: int | None


class MatchPlayerDefensiveRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from defensive table for matches.
    """

    tackles: int | None
    tackles_won: int | None
    tackles_def_3rd: int | None
    tackles_mid_3rd: int | None
    tackles_att_3rd: int | None
    challenge_tackles: int | None
    challenges: int | None
    challenges_lost: int | None
    blocks: int | None
    blocked_shots: int | None
    blocked_passes: int | None
    interceptions: int | None
    tackles_interceptions: int | None
    clearances: int | None
    errors: int | None


class MatchPlayerPossessionRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from possession table for matches.
    """

    touches: int | None
    touches_def_pen_area: int | None
    touches_def_3rd: int | None
    touches_mid_3rd: int | None
    touches_att_3rd: int | None
    touches_att_pen_area: int | None
    touches_live_ball: int | None
    take_ons: int | None
    take_ons_won: int | None
    take_ons_won_pct: Decimal | None
    take_ons_tackled: int | None
    take_ons_tackled_pct: Decimal | None
    carries: int | None
    carries_distance: int | None
    carries_progressive_distance: int | None
    progressive_carries: int | None
    carries_into_final_third: int | None
    carries_into_penalty_area: int | None
    miscontrols: int | None
    dispossessed: int | None
    passes_received: int | None
    progressive_passes_received: int | None


class MatchPlayerMiscRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from miscellaneous table for matches.
    """

    cards_yellow: int | None
    cards_red: int | None
    cards_yellow_red: int | None
    fouls: int | None
    fouled: int | None
    offsides: int | None
    crosses: int | None
    interceptions: int | None
    tackles_won: int | None
    pens_won: int | None
    pens_conceded: int | None
    own_goals: int | None
    ball_recoveries: int | None
    aerials_won: int | None
    aerials_lost: int | None
    aerials_won_pct: Decimal | None
   

class MatchGKRow(BaseMatchLogModel):
    """
    Model to validate each row of data scraped from miscellaneous table for matches.
    """
    gk_shots_on_target_against: int | None
    gk_goals_against: int | None
    gk_saves: int | None
    gk_save_pct: Decimal | None
    gk_psxg: Decimal | None
    gk_passes_completed_launched: int | None
    gk_passes_launched: int | None
    gk_passes_pct_launched: Decimal | None
    gk_passes: int | None
    gk_passes_throws: int | None
    gk_pct_passes_launched: Decimal | None
    gk_passes_length_avg: Decimal | None
    gk_goal_kicks: int | None
    gk_pct_goal_kicks_launched: Decimal | None
    gk_goal_kick_length_avg: Decimal | None
    gk_crosses: int | None
    gk_crosses_stopped: int | None
    gk_crosses_stopped_pct: Decimal | None
    gk_def_actions_outside_pen_area: int | None
    gk_avg_distance_def_actions: Decimal | None