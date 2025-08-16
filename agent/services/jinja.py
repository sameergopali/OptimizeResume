from jinja2 import Environment, FileSystemLoader


class JinjaService:
    def __init__(self, template_dir):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template_dir = template_dir
        
    def render_summary(self, content, template_file='summary.tex.j2'):
        template = self.env.get_template(template_file)
        print("rendering..")
        rendered_tex = template.render({"summary_content":content})
        return rendered_tex
 
