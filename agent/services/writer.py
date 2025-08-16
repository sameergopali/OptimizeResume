class WriterService:
    @staticmethod
    def write(tex, output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(tex)
