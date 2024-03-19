import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutoCadastroComponent, CodigoAcessoComponent, LoginComponent, PageNotFoundComponent, SucessoCadastroComponent, ValidCodeGuard } from './auth';
import { AdminRouting } from './admin/admin-routing.module';

const routes: Routes = [
  // No futuro fazer cada modulo ter seu routing separado assim como é no module e atualizar tudo aqui
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'autocadastro', component: CodigoAcessoComponent},
  { path: 'autocadastro/dados/:codigoAcesso', component: AutoCadastroComponent, canActivate: [ValidCodeGuard]},
  ...AdminRouting,
  // ...BenefitedRouting,
  // ...VolunteerRouting,
  { path: '**', pathMatch: 'full', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
