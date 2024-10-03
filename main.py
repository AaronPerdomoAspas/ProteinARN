from config.Config import Config
from orchestrator.Main_orchestrator import MainOrchestrator


def main() -> None:
    orchestrator = MainOrchestrator(Config)
    orchestrator.execute()


if __name__ == "__main__":
    main()
