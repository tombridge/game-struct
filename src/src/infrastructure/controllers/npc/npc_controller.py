from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional

from src.core.repositories.npcRepository.dto import NPCResponseDTO, NPCCreateDTO, NPCUpdateDTO
from src.core.repositories.npcRepository.npcRepository import NPCRepository
from src.core.services.npcService.npcService import NPCService

router = APIRouter(prefix="/npc", tags=["NPC"])

# Зависимость для получения сервиса (можно заменить на DI)
def get_npc_service() -> NPCService:
    repository = NPCRepository()
    return NPCService(repository)


@router.get("/{npc_id}", response_model=Optional[NPCResponseDTO])
async def get_npc(npc_id: int, service: NPCService = Depends(get_npc_service)):
    """Получить NPC по ID."""
    npc = await service.get_npc(npc_id)
    if not npc:
        raise HTTPException(status_code=404, detail="NPC не найден")
    return npc


@router.get("/", response_model=List[NPCResponseDTO])
async def get_all_npcs(service: NPCService = Depends(get_npc_service)):
    """Получить список всех NPC."""
    return await service.get_all_npcs()


@router.get("/location/{location}", response_model=List[NPCResponseDTO])
async def get_npcs_by_location(location: str, service: NPCService = Depends(get_npc_service)):
    """Получить всех NPC в указанной локации."""
    return await service.get_npcs_by_location(location)


@router.post("/", response_model=NPCResponseDTO)
async def create_npc(npc_dto: NPCCreateDTO, service: NPCService = Depends(get_npc_service)):
    """Создать нового NPC."""
    return await service.create_npc(npc_dto)


@router.put("/", response_model=Optional[NPCResponseDTO])
async def update_npc(npc_dto: NPCUpdateDTO, service: NPCService = Depends(get_npc_service)):
    """Обновить NPC по ID."""
    updated_npc = await service.update_npc(npc_dto)
    if not updated_npc:
        raise HTTPException(status_code=404, detail="NPC не найден")
    return updated_npc


@router.delete("/{npc_id}")
async def delete_npc(npc_id: int, service: NPCService = Depends(get_npc_service)):
    """Удалить NPC по ID."""
    deleted = await service.delete_npc(npc_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="NPC не найден")
    return {"message": "NPC удален"}


@router.patch("/{npc_id}/move", response_model=Optional[NPCResponseDTO])
async def move_npc(npc_id: int, new_location: str, service: NPCService = Depends(get_npc_service)):
    """Переместить NPC в новую локацию."""
    npc = await service.move_npc(npc_id, new_location)
    if not npc:
        raise HTTPException(status_code=404, detail="NPC не найден")
    return npc


@router.patch("/{npc_id}/damage", response_model=Optional[NPCResponseDTO])
async def apply_damage(npc_id: int, damage: int, service: NPCService = Depends(get_npc_service)):
    """Нанести урон NPC."""
    npc = await service.apply_damage(npc_id, damage)
    if not npc:
        raise HTTPException(status_code=404, detail="NPC не найден")
    return npc
