from abc import ABC, abstractmethod
from typing import List, Optional

class NPCRepository(ABC):
    """Интерфейс репозитория для работы с NPC."""

    @abstractmethod
    async def get_by_id(self, npc_id: int) -> Optional[NPCResponseDTO]:
        """Получает NPC по его ID."""
        pass

    @abstractmethod
    async def get_all(self) -> List[NPCResponseDTO]:
        """Получает список всех NPC."""
        pass

    @abstractmethod
    async def get_by_location(self, location: str) -> List[NPCResponseDTO]:
        """Получает всех NPC в заданной локации."""
        pass

    @abstractmethod
    async def create(self, npc_dto: NPCCreateDTO) -> NPCResponseDTO:
        """Создаёт нового NPC и возвращает его данные."""
        pass

    @abstractmethod
    async def update(self, npc_dto: NPCUpdateDTO) -> Optional[NPCResponseDTO]:
        """Обновляет существующего NPC и возвращает обновлённые данные."""
        pass

    @abstractmethod
    async def delete(self, npc_id: int) -> None:
        """Удаляет NPC по ID."""
        pass

    @abstractmethod
    async def set_location(self, npc_id: int, location: str) -> Optional[NPCResponseDTO]:
        """Изменяет локацию NPC."""
        pass

    @abstractmethod
    async def set_health(self, npc_id: int, health: int) -> Optional[NPCResponseDTO]:
        """Обновляет здоровье NPC."""
        pass