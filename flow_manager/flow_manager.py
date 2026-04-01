from typing import Dict
import logging

from flow_manager.tasks import TASKS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class FlowManager:
    def __init__(self, flow_data: Dict):
        self.flow       = flow_data["flow"]
        self.payload    = flow_data.get("payload", {})
        self.tasks      = {task["name"]: task for task in self.flow["tasks"]}
        self.conditions = self.flow.get("conditions", [])
        self.start_task = self.flow["start_task"]
    
    def get_condition(self, task_name: str):
        for condition in self.conditions:
            if condition["source_task"] == task_name:
                return condition
        return None

    def execute_flow(self):
        current_task = self.start_task
        context = {
            "payload": self.payload
        }
        executed_tasks = []

        while current_task != "end":
            logger.info(f"Running task: {current_task}")

            task_func = TASKS.get(current_task)
            if not task_func:
                raise Exception(f"Task '{current_task}' not found in registry")

            result = task_func(context)

            executed_tasks.append({
                "task": current_task,
                "result": result
            })

            condition = self.get_condition(current_task)

            if not condition:
                final_status = "completed" if result["status"] == "success" else "failed"
                return {
                    "status": final_status,
                    "executed_tasks": executed_tasks,
                    "context": context
                }

            if result["status"] == "success":
                current_task = condition["target_task_success"]
            else:
                current_task = condition["target_task_failure"]

            if current_task == "end":
                final_status = "completed" if result["status"] == "success" else "failed"
                return {
                    "status": final_status,
                    "executed_tasks": executed_tasks,
                    "context": context
                }

        return {
            "status": "completed",
            "executed_tasks": executed_tasks,
            "context": context
        }

    def run():
        pass

if __name__ == "__main__":
    manager = FlowManager()
    manager.run()
