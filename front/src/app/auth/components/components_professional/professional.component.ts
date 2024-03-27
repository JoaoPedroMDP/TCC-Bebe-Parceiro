import { NgIfContext } from '@angular/common';
import { Component, OnInit, TemplateRef } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth';
import { SwalFacade, UserToken } from 'src/app/shared';
import { Professional, Speciality } from 'src/app/shared/models/professional';


@Component({
  selector: 'app-professional',
  templateUrl: './professional.component.html',
  styleUrls: ['./professional.component.css']
})
export class ProfessionalComponent implements OnInit {


  user!: UserToken;
  form: any;
  professional!: Professional;
  specialties!: Speciality[];
  showSuccess = false;


  

  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    this.user = this.authService.getUser();
  }
  
  /**
   * @Description Realiza o logout do usuário e retorna a página de login
   */
  logout() {
    this.authService.logout().subscribe({
      next: () => SwalFacade.success("Usuário desconectado","Redirecionando ao login"),
      error: () => SwalFacade.error("Ocorreu um erro","Não foi possível fazer o logout"),
      complete: () => this.router.navigate(['/login'])
    });
  }

  save() {
    if (this.professional.acceptTerms) {
      console.log('Dados do voluntário:', this.professional);
      
    } else {
      alert('Por favor, aceite os termos de voluntariado para continuar.');
    }
    this.showSuccess=true;
    console.log(this.showSuccess)
  }


}
