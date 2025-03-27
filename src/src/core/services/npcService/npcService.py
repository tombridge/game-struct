from typing import List, Optional

from src.core.repositories.npcRepository.dto import NPCResponseDTO, NPCCreateDTO, NPCUpdateDTO
from src.core.repositories.npcRepository.npcRepository import NPCRepository


class NPCService:
    """Сервис для работы с NPC, содержащий бизнес-логику."""

    def __init__(self, repository: NPCRepository):
        self.repository = repository

    async def get_npc(self, npc_id: int) -> Optional[NPCResponseDTO]:
        """Получает NPC по ID."""
        return await self.repository.get_by_id(npc_id)

    async def get_all_npcs(self) -> List[NPCResponseDTO]:
        """Получает список всех NPC."""
        return await self.repository.get_all()

    async def get_npcs_by_location(self, location: str) -> List[NPCResponseDTO]:
        """Получает всех NPC в указанной локации."""
        return await self.repository.get_by_location(location)

    async def create_npc(self, npc_dto: NPCCreateDTO) -> NPCResponseDTO:
        """Создаёт нового NPC, проверяя корректность данных."""
        if npc_dto.health <= 0:
            raise ValueError("Здоровье NPC должно быть больше 0")
        return await self.repository.create(npc_dto)

    async def update_npc(self, npc_dto: NPCUpdateDTO) -> Optional[NPCResponseDTO]:
        """Обновляет NPC, если он существует."""
        existing_npc = await self.repository.get_by_id(npc_dto.id)
        if not existing_npc:
            return None  # Можно выбрасывать исключение, если нужен строгий контроль
        return await self.repository.update(npc_dto)

    async def delete_npc(self, npc_id: int) -> bool:
        """Удаляет NPC, если он существует."""
        existing_npc = await self.repository.get_by_id(npc_id)
        if not existing_npc:
            return False
        await self.repository.delete(npc_id)
        return True

    async def move_npc(self, npc_id: int, new_location: str) -> Optional[NPCResponseDTO]:
        """Перемещает NPC в новую локацию, если он существует."""
        existing_npc = await self.repository.get_by_id(npc_id)
        if not existing_npc:
            return None
        return await self.repository.set_location(npc_id, new_location)

    async def apply_damage(self, npc_id: int, damage: int) -> Optional[NPCResponseDTO]:
        """Наносит урон NPC. Если здоровье опускается до 0, NPC считается 'мертвым'."""
        npc = await self.repository.get_by_id(npc_id)
        if not npc:
            return None

        new_health = max(0, npc.health - damage)
        return await self.repository.set_health(npc_id, new_health)
