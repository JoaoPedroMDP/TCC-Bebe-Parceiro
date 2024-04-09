import { Component, OnInit, TemplateRef } from '@angular/core';
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

  user!: UserToken;
  professional!: Professional;
  showSuccess = false;
  specialitySelected!: number | undefined;
  specialities!: Speciality[];
  



  constructor(private ProfessionalService: ProfessionalService, private router: Router) { }

  ngOnInit(): void {
    this.professional = new Professional();
    this.listSpecialities();
  }


  
  listSpecialities() {
    this.ProfessionalService.getSpecialities().subscribe({
      next: (data: Speciality[]) => {
        if (data == null) {
          this.specialities = [];
        } else {
          this.specialities = data;
        }
      },
      error: () => SwalFacade.error('Erro ao listar os dados de Especialidades')
    })
  }


 

  save() {
    // Atualiza os dados da beneficiada com as informações selecionadas
    this.professional.speciality= this.specialitySelected;
    if (this.professional.accepted_volunteer_terms) {
      this.ProfessionalService.saveProfessional(this.professional)
        .subscribe({
          next: () => this.showSuccess = true,
          error: (e) => { SwalFacade.error("Erro ao salvar!", e) }
        });
        this.showSuccess=true;
      } else {
        alert('Por favor, aceite os termos de voluntariado para continuar.');
      }
     
    }
  }



