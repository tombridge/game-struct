from dataclasses import dataclass
from typing import List, Optional


@dataclass
class NPCUpdateDTO:
    """DTO для обновления существующего NPC."""
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    health: Optional[int] = None
    strength: Optional[int] = None
    agility: Optional[int] = None
    intelligence: Optional[int] = None
    dialogue: Optional[List[str]] = None
    is_hostile: Optional[bool] = None
    location: Optional[str] = None