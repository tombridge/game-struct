from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from typing import Optional, List

from src.core.repositories.npcRepository.dto import NPCResponseDTO, NPCCreateDTO, NPCUpdateDTO
from src.infrastructure.db.enttities.npc import NPCModel


class NPCRepositoryImpl(INPCRepository):
    """Реализация репозитория NPC, работающая с базой данных."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_npc(self, npc_id: int) -> Optional[NPCResponseDTO]:
        """Получает NPC по ID."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.id == npc_id))
        npc = result.scalars().first()
        return NPCResponseDTO.from_orm(npc) if npc else None

    async def get_all_npcs(self) -> List[NPCResponseDTO]:
        """Возвращает список всех NPC."""
        result = await self.session.execute(select(NPCModel))
        npcs = result.scalars().all()
        return [NPCResponseDTO.from_orm(npc) for npc in npcs]

    async def get_npcs_by_location(self, location: str) -> List[NPCResponseDTO]:
        """Возвращает всех NPC в указанной локации."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.location == location))
        npcs = result.scalars().all()
        return [NPCResponseDTO.from_orm(npc) for npc in npcs]

    async def create_npc(self, npc_dto: NPCCreateDTO) -> NPCResponseDTO:
        """Создает нового NPC."""
        new_npc = NPCModel(**npc_dto.dict())
        self.session.add(new_npc)
        await self.session.commit()
        await self.session.refresh(new_npc)
        return NPCResponseDTO.from_orm(new_npc)

    async def update_npc(self, npc_dto: NPCUpdateDTO) -> Optional[NPCResponseDTO]:
        """Обновляет NPC по ID."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.id == npc_dto.id))
        npc = result.scalars().first()
        if not npc:
            return None

        for key, value in npc_dto.dict(exclude_unset=True).items():
            setattr(npc, key, value)

        await self.session.commit()
        await self.session.refresh(npc)
        return NPCResponseDTO.from_orm(npc)

    async def delete_npc(self, npc_id: int) -> bool:
        """Удаляет NPC по ID."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.id == npc_id))
        npc = result.scalars().first()
        if not npc:
            return False

        await self.session.delete(npc)
        await self.session.commit()
        return True

    async def move_npc(self, npc_id: int, new_location: str) -> Optional[NPCResponseDTO]:
        """Перемещает NPC в новую локацию."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.id == npc_id))
        npc = result.scalars().first()
        if not npc:
            return None

        npc.location = new_location
        await self.session.commit()
        await self.session.refresh(npc)
        return NPCResponseDTO.from_orm(npc)

    async def apply_damage(self, npc_id: int, damage: int) -> Optional[NPCResponseDTO]:
        """Применяет урон к NPC и обновляет его здоровье."""
        result = await self.session.execute(select(NPCModel).where(NPCModel.id == npc_id))
        npc = result.scalars().first()
        if not npc:
            return None

        npc.health = max(0, npc.health - damage)  # Не допускаем отрицательного здоровья
        await self.session.commit()
        await self.session.refresh(npc)
        return NPCResponseDTO.from_orm(npc)
