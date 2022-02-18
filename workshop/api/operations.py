from typing import Optional

from fastapi import APIRouter, Depends, Response, status
from workshop.service.auth import get_current_user

from ..models.auth import User
from ..models.operations import (Operation, OperationCreate, OperationKind,
                                 OperationUpdate)
from ..service.operations import OperationsService

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=list[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        user: User = Depends(get_current_user),
        service: OperationsService = Depends(),
):
    """
    Getting a list of operation.

    - **kind**: Filter by operation type

    \f
    :param kind;
    :param user;
    :param service;
    :return;
    """
    return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):

    return service.create(user_id=user.id, operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.get(user_id=user.id, operation_id=operation_id)


@router.patch('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):

    return service.update(
        user_id=user.id,
        operation_id=operation_id,
        operation_data=operation_data
    )


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    service.delete(user_id=user.id, operation_id=operation_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
