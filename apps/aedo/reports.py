from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, LEGAL, landscape
from reportlab.lib.pagesizes import A4

from reportlab.platypus import Table
from io import BytesIO

from django.http import HttpResponse
from .models import *
import datetime
import xlwt

def reporte_general(request, report_id):
    file_name = "reporte general"
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Libro1')
    default_style = xlwt.Style.default_style
    estilo_cabecera = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;'
                          'font: colour white, bold True;')


    reporte = Report.objects.get(pk=report_id)
    gestores = UserReport.objects.filter(report=reporte)
    entregas = Delivery.objects.filter(deliver_date=reporte.date)


    titulos = ['ID ENTREGA','CLIENTE', 'CIUDAD', 'COSTO DEL SERVICIO', 'COMISION GESTOR', 'COMISION AEDO', 'COMISION CLIENTE', 'TOTAL', 'COBRADO POR GESTOR', 'COBRADO POR AEDO', 'TOTAL COBRADO', 'PENDIENTE', 'ESTADO DE LA ENTREGA', 'ESTADO DE PAGO', 'OBSERVACIONES']
    linea = 0
    for gestor in gestores:
        list_values = []

        for entrega in entregas.filter(employee=gestor.employee):
            list_values.append([
                entrega.id,
                entrega.company.name, 
                entrega.city.name, 
                entrega.service_amount, 
                entrega.employee_amount, 
                entrega.aedo_amount,
                entrega.get_company_amount(),
                entrega.get_total(),
                entrega.received,
                entrega.received2,
                entrega.get_received(),
                entrega.get_pending(),
                entrega.get_state_display(),
                entrega.get_state2_display(),
                entrega.comment
            ])

        for col, datos in enumerate(titulos):
            sheet.write(linea, col, datos, style=estilo_cabecera)


        inicio = linea + 2
        for row, rowdata in enumerate(list_values):
            linea = linea+1
            for col, val in enumerate(rowdata):
                style = default_style
                sheet.write(linea, col, val, style=style)

        fin = linea +1
        linea = linea + 1

        print("inicio", inicio)
        print("fin", fin)
        sheet.write(linea, 0, "SUMAS:")
        sheet.write(linea, 4, xlwt.Formula("SUM($E$%d:$E$%d)"%(inicio, fin)))
        sheet.write(linea, 5, xlwt.Formula("SUM($F$%d:$F$%d)"%(inicio, fin)))
        sheet.write(linea, 6, xlwt.Formula("SUM($G$%d:$G$%d)"%(inicio, fin)))
        sheet.write(linea, 7, xlwt.Formula("SUM($H$%d:$H$%d)"%(inicio, fin)))
        sheet.write(linea, 8, xlwt.Formula("SUM($I$%d:$I$%d)"%(inicio, fin)))
        sheet.write(linea, 9, xlwt.Formula("SUM($J$%d:$J$%d)"%(inicio, fin)))
        sheet.write(linea, 10, xlwt.Formula("SUM($K$%d:$K$%d)"%(inicio, fin)))
        sheet.write(linea, 11, xlwt.Formula("SUM($L$%d:$L$%d)"%(inicio, fin)))

        linea = linea + 2
        sheet.write(linea, 0, "GESTOR:")
        sheet.write(linea, 1, gestor.employee.get_full_name())

        linea = linea +1
        sheet.write(linea, 0, "BASE:")
        sheet.write(linea, 1, gestor.base_amount)

        linea = linea + 1
        sheet.write(linea, 0, "TOTAL GESTOR:")
        sheet.write(linea, 1, xlwt.Formula("$E$%d + $B$%d"%(linea-3, linea)))

        linea = linea + 1
        sheet.write(linea, 0, "TOTAL AEDO:")
        sheet.write(linea, 1, xlwt.Formula("$F$%d - $B$%d"%(linea-4, linea-1)))

        linea = linea + 1
        sheet.write(linea, 0, "TOTAL A RENDIR:")
        sheet.write(linea, 1, xlwt.Formula("$I$%d - $E$%d - $B$%d"%(linea-5, linea-5, linea-2)))

        linea = linea + 3

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+file_name+'-'+datetime.datetime.now().strftime('%Y-%m-%d')+'.xls'
    book.save(response)
    return response

def reporte_gestor(request, gestor_id):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "reporte_gestor"+ datetime.datetime.now().strftime('%Y-%m-%d') + '.pdf' 
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name.replace(" ","_")
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=(A4),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    reporte = []

    styles = getSampleStyleSheet()
    header = Paragraph("Resumen del dia", styles['Title'])
    reporte.append(header)

    datos = [("ID", "Fecha entrega", "Estado", "Comision", "Cobrado")]
    fecha_actual = datetime.date.today()
    print(fecha_actual)

    entregas = Delivery.objects.filter(employee_id=gestor_id, deliver_date=fecha_actual)
    total_recaudado = 0
    total_comision = 0
    for entrega in entregas:
        total_comision = total_comision + entrega.employee_amount
        total_recaudado = total_recaudado + entrega.received
        datos = datos + [(
            Paragraph( str(entrega.id), styles['Normal']),
            Paragraph(entrega.deliver_date.strftime("%d/%m/%Y") if (entrega.deliver_date != None) else '', styles['Normal']),
            Paragraph(entrega.get_state_display(), styles['Normal']),
            Paragraph( str(entrega.employee_amount), styles['Normal']),
            Paragraph( str(entrega.received), styles['Normal']),
        )]
    total_rendir = total_recaudado - total_comision


    #t = Table(datos, colWidths=(100*mm,25*mm, 35*mm, 35*mm))

    t = Table(datos)
    t.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN',(4,1),(4,-1),'RIGHT'),
            ('VALIGN',(0, 0), (-1, -1),'MIDDLE'),
            ('ALIGN',(0, 0), (-1, 0),'CENTER'),

        ]
    ))
    reporte.append(t)
    reporte.append( Paragraph("TOTAL RECAUDADO: %d" % (total_recaudado), styles['Normal'] ) )
    reporte.append( Paragraph("TOTAL COMISION: %d" % (total_comision), styles['Normal'] ) )
    reporte.append( Paragraph("TOTAL A RENDIR: %d" % (total_rendir), styles['Normal'] ) )
    reporte.append( Paragraph("PD: descontar la base", styles['Normal']) )

    doc.build(reporte)
    response.write(buff.getvalue())
    buff.close()
    return response