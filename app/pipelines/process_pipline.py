from app.core.config import settings
from app.schemas import ServiceRequest, ServiceResponse
from app.common import setup_logger
from app.common.utils.utils import get_ipv4_address

logger = setup_logger("[AI_SERVICE]")


class Pipeline:
    def invoke(self, data: ServiceRequest) -> ServiceResponse:
        pass

    def get_info(self):
        data_send = {"ip": get_ipv4_address(), "port": str(settings.PORT), "data": {}}
        return data_send
