from UnifiedOrchestrator import UnifiedOrchestrator


def main():
    orchestrator = UnifiedOrchestrator()

    orchestrator.download_fasta_files()

    orchestrator.process_fasta_files()


if __name__ == "__main__":
    main()
