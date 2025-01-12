from common.exceptions import AppException
from common.exceptions.base import IntegrityDataError, ObjectDoesNotExist


class DocumentException(AppException):
    """Base document exception"""


class DocumentDoesNotExist(ObjectDoesNotExist):
    """Document does not exist"""


class InvalidDocument(IntegrityDataError):
    """Invalid document"""
