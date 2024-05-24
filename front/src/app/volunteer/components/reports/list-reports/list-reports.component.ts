import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Beneficiary, SwalFacade, Volunteer, VolunteerService } from 'src/app/shared';
import { ReportsService } from 'src/app/volunteer/services/reports.service';
import { DateRangeReportsModalComponent } from '../date-range-reports-modal/date-range-reports-modal.component';

@Component({
  selector: 'app-list-reports',
  templateUrl: './list-reports.component.html',
  styleUrls: ['./list-reports.component.css']
})
export class ListReportsComponent implements OnInit {

  constructor(private volunteerService: VolunteerService, private reportsService: ReportsService, private modalService: NgbModal) { }

  ngOnInit(): void {
  }

  /**
   * @description Extrai os dados das voluntárias e então chama no service
   *  o tipo de arquivo escolhido para fazer a extração
   * @param type O tipo do arquivo (PDF ou Excel)
   */
  extractVolunteer(type: string) {
    this.volunteerService.listVolunteer().subscribe({
      next: (volunteers: Volunteer[]) => {
        // Variavéis para o relatorio
        const columns = ['Nome', 'Telefone', 'Cidade', 'Estado', 'País'];
        const rows = volunteers.map(data => [
          data.user?.name,
          data.user?.phone,
          data.city?.name,
          data.city?.state?.name,
          data.city?.state?.country?.name
        ]);
        const name = "Voluntárias"

        if (type == 'pdf') {
          this.reportsService.extractPDF(columns, rows, name)
        } else {
          this.reportsService.extractXLSX(columns, rows, name)
        }
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e)
    })
  }

  /**
   * @description Extrai os dados das beneficiadas e então chama no service
   *  o tipo de arquivo escolhido para fazer a extração
   * @param type O tipo do arquivo (PDF ou Excel)
   */
  extractBeneficiary(type: string) {
    this.volunteerService.listBeneficiary().subscribe({
      next: (beneficiaries: Beneficiary[]) => {
        // Variavéis para o relatorio
        const columns = ['Nome', 'Nº Filhos', 'Estado Civil', 'Renda Familiar', 'Cidade', 'Estado'];
        const rows = beneficiaries.map(data => [
          data.user?.name,
          data.child_count,
          data.marital_status?.name,
          data.monthly_familiar_income,
          data.city?.name,
          data.city?.state?.name
        ]);
        const name = "Beneficiadas"

        if (type == 'pdf') {
          this.reportsService.extractPDF(columns, rows, name)
        } else {
          this.reportsService.extractXLSX(columns, rows, name)
        }
      },
      error: (e) => SwalFacade.error("Ocorreu um erro!", e)
    })
  }

  /**
   * @description Abre um modal para coletar o intervalo de datas no relatório de atendimentos
   * @param type O tipo do arquivo (PDF ou Excel)
   */
  extractAppointments(type: string) {
    let modalRef = this.modalService.open(DateRangeReportsModalComponent, { size: 'xl' })
    modalRef.componentInstance.type = type
    modalRef.componentInstance.object = 'appointments'
  }

  /**
   * @description Abre um modal para coletar o intervalo de datas no relatório de trocas
   * @param type O tipo do arquivo (PDF ou Excel)
   */
  extractSwaps(type: string) {
    let modalRef = this.modalService.open(DateRangeReportsModalComponent, { size: 'xl' })
    modalRef.componentInstance.type = type
    modalRef.componentInstance.object = 'swaps'
  }
}
