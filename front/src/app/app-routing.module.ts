import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutoCadastroComponent, CodigoAcessoComponent, LoginComponent, PageNotFoundComponent, ValidCodeGuard } from './auth';
import { AdminRouting } from './admin/admin-routing.module';
import { BenefitedRouting } from './benefited/benefited-routing.module';
import { VolunteerRouting } from './volunteer/volunteer-routing.module';


const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'autocadastro', component: CodigoAcessoComponent },
  { path: 'autocadastro/dados/:codigoAcesso', component: AutoCadastroComponent, canActivate: [ValidCodeGuard] },
  // { path: 'voluntario', component: ProfissionalComponent},
  ...AdminRouting,
  ...BenefitedRouting,
  ...VolunteerRouting,
  { path: '**', pathMatch: 'full', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
