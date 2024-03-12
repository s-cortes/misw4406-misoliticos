from uuid import UUID

from propiedades.config.db import db
from propiedades.seedwork.domain.repositories import Repository

from .dtos import Saga as SagaDTO
from .dtos import Transaction as TransactionDTO


class SagaRepository:

    def get_all(self, id: int) -> list[SagaDTO]:
        return db.session.query(SagaDTO).filter_by(id=id).all()

    def get(self, id: int, step: int) -> SagaDTO:
        return db.session.query(SagaDTO).filter_by(id=id, step=step).one()

    def append(self, saga: SagaDTO):
        db.session.add(saga)
        db.session.commit()

    def delete(self):
        pass

    def update(self):
        pass

def initialize_saga():
    repository = SagaRepository()
    if repository.get_all(1): return 

    sagas = [
        SagaDTO(id=1, step=0, event="PropiedadCreada", command="CreateGeoespacialCommand", topic="geoespacial-commands"),
        SagaDTO(id=1, step=1, event="GeoespacialCreado", command="CreateCatastralCommand", topic="catastral-commands"),
        SagaDTO(id=1, step=2, is_last=True, event="CreacionPropiedadSolicitadaDomain"),
    ]
    for saga in sagas:
        repository.append(saga)


class TransactionRepository:

    def get_all(self, correlation_id: str) -> list[TransactionDTO]:
        return (
            db.session.query(TransactionDTO)
            .filter_by(correlation_id=correlation_id)
            .all()
        )

    def get(self, id: int, step: int, correlation_id: str) -> TransactionDTO:
        return (
            db.session.query(SagaDTO)
            .filter_by(
                id=id,
                step=step,
                correlation_id=correlation_id,
            )
            .one()
        )

    def append(self, transaction: TransactionDTO):
        db.session.add(transaction)
        db.session.commit()

    def delete(self):
        pass

    def update(self):
        pass
