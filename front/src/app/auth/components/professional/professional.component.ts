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
  specialities!: Speciality[];
  showSuccess = false;
  specialitySelected!: number | undefined;
  speciality: any;



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
    this.professional.speciality= this.specialitySelected;
    if (this.professional.acceptTerms) {
      console.log('Dados do voluntário:', this.professional);
      
    } else {
      alert('Por favor, aceite os termos de voluntariado para continuar.');
    }
    this.showSuccess=true;
    console.log(this.showSuccess)
  }


}
