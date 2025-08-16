from services.writer import WriterService
import subprocess
import os
import shutil

class PDFService:
    
    def __init__(self, outdir, inputdir):
        self.outdir = outdir
        self.inputdir = inputdir
        
    def add_summary(self, summarytex):
        summaryfile = os.path.join(self.inputdir, "summary.tex")
        with open(summaryfile,'w') as f:
            f.write(summarytex) 
        self.compile_latex()
        
        
    def compile_latex(self,tex_file="main.tex", jobname="resume"):
        os.makedirs(self.outdir, exist_ok=True)
        subprocess.run([
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={os.path.abspath(self.outdir)}",
            f"-jobname={jobname}",
            tex_file
            ], cwd=self.inputdir, check=True)

        # Cleanup auxiliary files (keep only PDF)
        extensions_to_remove = [".aux", ".log", ".out", ".toc"]
        for ext in extensions_to_remove:
            fpath = os.path.join(self.outdir, jobname + ext)
            if os.path.exists(fpath):
                os.remove(fpath)




