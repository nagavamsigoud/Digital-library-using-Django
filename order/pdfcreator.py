from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_pdf_bytes(template_name, context=None):
    html = get_template(template_name).render(context or {})
    output = BytesIO()
    result = pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=output, encoding="utf-8")
    return None if result.err else output.getvalue()
