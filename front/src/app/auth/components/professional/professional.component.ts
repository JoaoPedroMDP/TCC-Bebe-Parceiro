import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { SwalFacade, UserToken } from 'src/app/shared';
import { Professional, Speciality } from 'src/app/shared/models/professional';
import { ProfessionalService } from '../../services/professional.service';


@Component({
  selector: 'app-professional',
  templateUrl: './professional.component.html',
  styleUrls: ['./professional.component.css']
})
export class ProfessionalComponent implements OnInit {

  @ViewChild('form') form!: NgForm;
  professional!: Professional;
  specialities!: Speciality[];
  showSuccess = false;

  constructor(private ProfessionalService: ProfessionalService) { }

  ngOnInit(): void {
    this.professional = new Professional();
    this.listSpecialities();
  }

  /**
   * @description Lista as especialidades do profissional para realizar o cadastro
   */
  listSpecialities() {
    this.ProfessionalService.getSpecialities().subscribe({
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

  save() {
    if (this.professional.accepted_volunteer_terms) {
      this.ProfessionalService.saveProfessional(this.professional)
        .subscribe({
          next: () => this.showSuccess = true,
          error: (e) => SwalFacade.error("Ocorreu um erro!", e)
        })
    } else {
      SwalFacade.alert('Por favor, aceite os termos de voluntariado para continuar.')
    }
  }
}



