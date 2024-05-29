import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SwalFacade, Swap } from 'src/app/shared';
import { Appointment } from 'src/app/shared/models/appointment/appointment.model';
import { ReportsService } from 'src/app/volunteer/services/reports.service';

@Component({
  selector: 'app-date-range-reports-modal',
  templateUrl: './date-range-reports-modal.component.html',
  styleUrls: ['./date-range-reports-modal.component.css']
})
export class DateRangeReportsModalComponent implements OnInit {

  @Input() type!: string; // PDF ou Excel
  @Input() object!: string; // Trocas ou Atendimentos
  startDate!: Date;
  endDate!: Date;

  constructor(public activeModal: NgbActiveModal, private reportsService: ReportsService) { }

  ngOnInit(): void {
    this.startDate = new Date();
    this.endDate = new Date();
  }

  /**
   * @description Verifica se as datas estão válidas e então a depender se o `type` (excel/PDF)
   * e o `object` (Trocas/Atendimentos) gera um relatório com o filtro das datas
   */
  save() {
    // Valida as datas
    if (this.startDate < this.endDate) {
      if (this.object === "swaps") {
        this.reportsService.listSwapsForReport(this.startDate, this.endDate).subscribe({
          next: (swaps: Swap[]) => {
            if (swaps.length > 0) {
              // Só faz a extração se houver dados na data selecionada

              // Variavéis para o relatorio
              const columns = ['Beneficiada', 'Criança', 'Tamanho Roupa', 'Data', 'Status'];
              const rows = swaps.map(data => [
                data.beneficiary?.user?.name,
                data.child?.name,
                data.cloth_size?.name,
                new Date(data.created_at!).toLocaleDateString(),  // dd/mm/yyyy
                data.status?.name
              ]);
              const name = "Trocas"

              if (this.type == 'pdf') {
                this.reportsService.extractPDF(columns, rows, name)
              } else {
                this.reportsService.extractXLSX(columns, rows, name)
              }
            } else {
              SwalFacade.alert("Nenhuma troca foi encontrada.")
            }
          },
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        })
      } else {
        this.reportsService.listAppointmentsForReport(this.startDate, this.endDate).subscribe({
          next: (appointment: Appointment[]) => {
            if (appointment.length > 0) {
              // Só faz a extração se houver dados na data selecionada

              // Variavéis para o relatorio
              const columns = ['Beneficiada', 'Voluntária', 'Profissional', 'Especialidade', 'Data', 'Status'];
              const rows = appointment.map(data => [
                data.beneficiary?.user?.name,
                data.volunteer?.user?.name,
                data.professional?.name || 'Não',
                data.speciality?.name || 'Não',
                data.datetime ? new Date(data.datetime).toLocaleDateString() : new Date(), // dd/mm/yyyy
                data.status?.name
              ]);
              const name = "Atendimentos"

              if (this.type == 'pdf') {
                this.reportsService.extractPDF(columns, rows, name)
              } else {
                this.reportsService.extractXLSX(columns, rows, name)
              }
            } else {
              SwalFacade.alert("Nenhum atendimento foi encontrado.")
            }
          },
          error: (e) => SwalFacade.error("Ocorreu um erro!", e),
          complete: () => this.activeModal.close()
        })
      }
    } else {
      SwalFacade.alert("As datas devem ser válidas", "A data inicial não pode ser maior ou igual a data final")
    }
  }
}
