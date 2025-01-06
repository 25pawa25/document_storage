from typing import Optional

from fastapi import APIRouter, Depends, Query, UploadFile, status

from common.dependencies.analytics import AnalyticQuery
from common.dependencies.file_info import FileInfo
from schemas.request.document import DocumentRequest
from schemas.response.document import DocumentResponse
from services.document.abc_document import AbstractDocumentService

router = APIRouter(prefix="/document", tags=["Document actions"])


@router.get("", summary="Get document", description="Get document")
async def get_document(
    title: Optional[str],
    file_type: Optional[str] = Query(None, alias="file_type"),
    document_service: AbstractDocumentService = Depends(),
    analytic=Depends(AnalyticQuery()),
) -> DocumentResponse:
    """
    Get document from database
    Args:
        title: The title of the document
        file_type: The file type of the document
        document_service: DocumentService
        analytic: Add analytic by query
    Returns:
        DocumentResponse
    """
    return await document_service.get_document(title=title, file_type=file_type)


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
    await document_service.create_document(file_info)
