import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import 'jspdf-autotable';
import { Observable, catchError, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { environment } from 'src/environments/environment';
import * as XLSX from 'xlsx';

@Injectable({
  providedIn: 'root'
})
export class ReportsService {

  private baseURL: string;

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  listAppointmentsForReport(startDate: Date, endDate: Date): Observable<any> {
    return this.http.get(`${this.baseURL}appointments/reports?start_date=${startDate}&end_date=${endDate}`, {
      headers: this.authService.getHeaders()
    }).pipe(
      catchError(error => {
        return throwError(() => new Error(`${error.status} - ${error.error.message}`));
      })
    );
  }

  listSwapsForReport(startDate: Date, endDate: Date): Observable<any> {
    return this.http.get(`${this.baseURL}swaps/reports?start_date=${startDate}&end_date=${endDate}`, {
      headers: this.authService.getHeaders()
    }).pipe(
      catchError(error => {
        return throwError(() => new Error(`${error.status} - ${error.error.message}`));
      })
    );
  }

  /**
 * @description Salva um arquivo PDF
 * @param columns Os colunas do cabeçalho
 * @param rows Os valores para irem no body da tabela
 * @param name Nome do arquivo / Nome do relatório
 */
  extractPDF(columns: any[], rows: any[], name: string) {
    // Garante que o jsPDF foi importado e instancia um objeto novo
    const { jsPDF } = require("jspdf");
    const pdf = new jsPDF();
    const now = new Date();

    // Imagem de fundo
    const imgData = environment.pdfBackgroundImageBase64;
    if (imgData) {
      // Caso a imagem for carregada corretamente, adiciona ela no relatório
      const imgWidth = 108;
      const imgHeight = 64;
      const pageWidth = pdf.internal.pageSize.getWidth();
      const pageHeight = pdf.internal.pageSize.getHeight();
      const imgX = (pageWidth - imgWidth) / 2;
      const imgY = (pageHeight - imgHeight) / 2;
      const opacity = 0.15; // Opacidade (15%)
      // Adiciona a imagem de fundo com opacidade
      pdf.setGState(new pdf.GState({ opacity: opacity }));
      pdf.addImage(imgData, 'JPEG', imgX, imgY, imgWidth, imgHeight);
      pdf.setGState(new pdf.GState({ opacity: 1 })); // Reseta a opacidade para 1 (100%) para o texto e tabela
    }

    // Criação do relatório
    pdf.setFontSize(20).setFont(undefined, 'bold');
    pdf.setbo
    pdf.text(`Bebê Parceiro - Relatório de ${name}`, 15, 20);
    pdf.setFontSize(10).setFont(undefined, 'normal');
    pdf.text('Relatório Feito em:  ' + now.toLocaleString(), 15, 26);
    pdf.autoTable({
      head: [columns],
      body: rows,
      theme: 'plain',
      startY: 35,
    });
    pdf.save(`Relatorio${name}.pdf`);
  }

  /**
   * @description Salva um arquivo XLSX - Excel
   * @param columns Os colunas do cabeçalho
   * @param rows Os valores para irem no body da tabela
   * @param name Nome do arquivo
   */
  extractXLSX(columns: any[], rows: any[], name: string) {
    const worksheet = XLSX.utils.aoa_to_sheet([columns, ...rows]);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
    XLSX.writeFile(workbook, `Relatorio${name}.xlsx`);
  }
}
