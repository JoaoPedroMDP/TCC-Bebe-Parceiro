import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminRouting } from './admin/admin-routing.module';
import { AutoCadastroComponent, CodigoAcessoComponent, ErrorComponent, LoginComponent, LoginRedirectGuard, ValidCodeGuard, ProfessionalComponent } from './auth';
import { BenefitedRouting } from './benefited/benefited-routing.module';
import { VolunteerRouting } from './volunteer/volunteer-routing.module';



const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent, canActivate: [LoginRedirectGuard]},
  { path: 'autocadastro', component: CodigoAcessoComponent },
  { path: 'autocadastro/dados/:codigoAcesso', component: AutoCadastroComponent, canActivate: [ValidCodeGuard] },
  { path: 'professional', component: ProfessionalComponent},
  ...AdminRouting,
  ...BenefitedRouting,
  ...VolunteerRouting,
  
  { 
    path: 'unauthorized', pathMatch: 'full', component: ErrorComponent, 
    data: { errorType: 'Acesso não autorizado', errorMessage: ' O usuário não possui as permissões necessárias para acessar esta página!' } 
  },
  { 
    path: '**', pathMatch: 'full', component: ErrorComponent, 
    data: { errorType: 'Página não encontrada', errorMessage: 'A página selecionada não foi encontrada, verifique se o endereço do site está digitado corretamente.' } 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
