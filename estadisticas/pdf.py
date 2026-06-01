from io import BytesIO
from datetime import datetime

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors

from incidentes.models import Incidente


def generar_reporte_pdf(request):
    """Genera un PDF con los últimos incidentes reportados"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Encabezado
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1,
    )
    elements.append(Paragraph("REPORTE DE INCIDENTES", title_style))
    elements.append(Paragraph(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}", styles['Normal']))
    elements.append(Spacer(1, 0.3 * inch))
    
    # Tabla de incidentes
    incidentes = Incidente.objects.all().order_by('-fecha_hora')[:50]
    
    data = [['Título', 'Sector', 'Tipo', 'Fecha', 'Reportado por']]
    for inc in incidentes:
        data.append([
            inc.titulo[:30],
            str(inc.sector)[:15],
            str(inc.tipo)[:15],
            inc.fecha_hora.strftime('%d/%m/%Y'),
            str(inc.reporte_por)[:15] if inc.reporte_por else 'Anónimo',
        ])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    elements.append(table)
    
    # Pie de página
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(
        f"<b>Total de incidentes:</b> {len(incidentes)}", 
        styles['Normal']
    ))
    
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_incidentes_{datetime.now().strftime("%Y%m%d")}.pdf"'
    return response
