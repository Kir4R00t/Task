import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class FlowManager:
    def __init__(self):
        pass
    
    def parse_flow_data(self):
        """
        After receiving json from POST rqst:
        get flow id -> get flow tasks -> get flow conditions
        """
        pass

    def execute_flow(self):
        """
        parse_flow_data() -> run task -> check result with conditions -> go to next task / end flow
        """
        pass

    def run():
        pass

if __name__ == "__main__":
    manager = FlowManager()
    manager.run()
