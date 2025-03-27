from dataclasses import dataclass
from typing import List, Optional


@dataclass
class NPCResponseDTO:
    """DTO для передачи NPC на уровень представления."""
    id: int
    name: str
    description: str
    health: int
    strength: int
    agility: int
    intelligence: int
    dialogue: List[str]
    is_hostile: bool
    location: Optional[str] = None
