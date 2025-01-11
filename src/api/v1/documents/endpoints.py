from typing import Optional

from fastapi import APIRouter, Depends, Query, UploadFile, status

from common.dependencies.analytics import AnalyticQuery
from common.dependencies.file_info import FileInfo
from schemas.request.document import DocumentRequest
from services.document.abc_document import AbstractDocumentService

router = APIRouter(prefix="/document", tags=["Document actions"])


@router.get("", summary="Get document", description="Get document")
async def get_document(
    title: Optional[str] = None,
    limit: Optional[int] = Query(3, ge=1, le=100),
    document_service: AbstractDocumentService = Depends(),
    analytic=Depends(AnalyticQuery()),
) -> list:
    """
    Get document from database
    Args:
        title: The title of the document
        limit: Limit the number of documents
        document_service: DocumentService
        analytic: Add analytic by query
    Returns:
        DocumentResponse
    """
    return await document_service.get_documents(title=title, limit=limit)


@router.post(
    "",
    summary="Add document",
    description="Add document",
    status_code=status.HTTP_201_CREATED,
)
async def add_document(
    file: UploadFile,
    document_service: AbstractDocumentService = Depends(),
    file_info: DocumentRequest = Depends(FileInfo()),
    analytic=Depends(AnalyticQuery()),
):
    """
    Add document to database
    Args:
        file: The uploaded file
        document_service: DocumentService
        file_info: DocumentRequest
        analytic: Add analytic by query
    """
    await document_service.add_or_update_document(file_info)


@router.delete(
    "",
    summary="Delete document",
    description="Delete document",
    status_code=status.HTTP_200_OK,
)
async def delete_document(
    title: Optional[str],
    document_service: AbstractDocumentService = Depends(),
    analytic=Depends(AnalyticQuery()),
):
    """
    Delete document from database
    Args:
        title: The title of the document
        document_service: DocumentService
        analytic: Add analytic by query
    """
    await document_service.delete_document(title=title)
