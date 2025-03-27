from dataclasses import dataclass
from typing import List, Optional

@dataclass
class NPCCreateDTO:
    """DTO для создания нового NPC."""
    name: str
    description: str
    health: int
    strength: int
    agility: int
    intelligence: int
    dialogue: List[str]
    is_hostile: bool
    location: Optional[str] = None