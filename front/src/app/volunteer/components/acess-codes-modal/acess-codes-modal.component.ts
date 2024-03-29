import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { AccessCode, SwalFacade } from 'src/app/shared';
import { VolunteerService } from '../../services/volunteer.service';

@Component({
  selector: 'app-acess-codes-modal',
  templateUrl: './acess-codes-modal.component.html',
  styleUrls: ['./acess-codes-modal.component.css']
})
export class AcessCodesModalComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  showSuccess!: boolean;
  accessCodes!: AccessCode[];

  constructor(public activeModal: NgbActiveModal, private volunteerService: VolunteerService) { }

  ngOnInit(): void {
    // Caso já exista algum código de acesso então vamos optar por já mostrar eles ao usuário
    // Antes dele criar novos códigos
    this.volunteerService.listAccessCodes().subscribe({
      next: (codes) => {
        // Só pega os 10 primeiros códigos, para não ficar muito bagunçado e cheio de dados
        this.accessCodes = codes.slice(0, 10);
      },
      error: (e) => { SwalFacade.error("Ocorreu um erro!", e) },
      complete: () => {
        if (this.accessCodes.length > 0) {
          // Existe códigos salvos então mostra eles antes
          this.showSuccess = true;
        } else {
          // Não existe nenhum código aqui então abre direto para cadastrar
          this.showSuccess = false;
        }
      }
    })

  }

  /**
   * @description cria códigos de acesso
   */
  generateCodes() {
    // Garantir que mesmo sem valor possa ser gerado códigos
    let amount: number = this.form.value.amount >= 1 ? this.form.value.amount : 1

    this.volunteerService.createAccessCodes(amount).subscribe({
      next: (codes) => {
        this.showSuccess = true;
        SwalFacade.success("Códigos criados com sucesso!", `${amount} novos códigos de acesso`)
        this.accessCodes.push(...codes); // Adiciona os novos códigos ao atributo
        this.accessCodes.slice(0, 10); // Remove da visualização o resto e mantém somente 10 códigos
      },
      error: (e) => { SwalFacade.error("Ocorreu um erro!", e) },
    })
  }

  /**
   * @description Método para alterar a flag e mudar os componentes para listar ou gerar códigos
   */
  toggleGenerateAndListCodes() {
    this.showSuccess = !this.showSuccess;
  }

}
