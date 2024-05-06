import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { SwalFacade } from 'src/app/shared';
import { Professional, ProfessionalPOST, Speciality } from 'src/app/shared/models/professional';
import { ProfessionalService } from 'src/app/volunteer';
import { SpecialityService } from 'src/app/volunteer/services/speciality.service';
import { environment } from 'src/environments/environment';


@Component({
  selector: 'app-professional',
  templateUrl: './professional.component.html',
  styleUrls: ['./professional.component.css']
})
export class ProfessionalComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  professional!: ProfessionalPOST;
  specialities!: Speciality[];
  showSuccess = false;
  captchaResponse!: string;
  siteKey!: string;

  constructor(private ProfessionalService: ProfessionalService, private specialityService: SpecialityService) { }

  ngOnInit(): void {
    this.siteKey = environment.recaptchaSiteKey;
    this.professional = new ProfessionalPOST();
    this.listSpecialities();
  }

  /**
   * @description Lista as especialidades do profissional para realizar o cadastro
   */
  listSpecialities() {
    this.specialityService.listSpecialities().subscribe({
      next: (data: Speciality[]) => {
        if (data == null) {
          this.specialities = [];
        } else {
          this.specialities = data;
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de Especialidades', e)
    })
  }

  /**
   * @description Armazena a resposta do reCAPTCHA em uma variável de instância local
   * @param response Token de resposta do reCAPTCHA
   */
  resolvedCaptcha(response: string): void {
    this.captchaResponse = response;
  }

  /**
   * @description Verifica se o profissional preencheu todos os campos e 
   * executa o método do service.
   */
  save() {
    this.professional.approved = false;
    if (this.professional.accepted_volunteer_terms && this.captchaResponse) {
      this.ProfessionalService.createProfessional(this.professional)
        .subscribe({
          next: () => this.showSuccess = true,
          error: (e) => SwalFacade.error("Ocorreu um erro!", e)
        })
    } else {
      SwalFacade.alert('Aceite os termos de voluntariado e campo "Não sou robô" para continuar.')
    }
  }
}



