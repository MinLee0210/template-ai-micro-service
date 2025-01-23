from app.core.config import settings
from app.schemas import ServiceRequest, ServiceResponse
from app.common import setup_logger

logger = setup_logger("[AI_SERVICE]")


class Pipeline:
    def invoke(self, data: ServiceRequest) -> ServiceResponse:
        pass

    def get_info(self):
        data_send = {"ip": settings.HOST, "port": str(settings.PORT), "data": {}}
        return data_send
